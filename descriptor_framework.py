from __future__ import annotations
import threading
import weakref
from typing import Any, Callable, Optional, Dict, Tuple
import time

class ValidationError(ValueError):
    pass

class _PerInstanceStore:
    """
    Weak-key dictionary wrapper storing (value, locked_flag) per-instance.
    Thread-safe per-descriptor using an internal lock.
    """
    def __init__(self):
        self._data: "weakref.WeakKeyDictionary[object, Tuple[Any, bool]]" = weakref.WeakKeyDictionary()
        self._lock = threading.RLock()

    def get(self, inst: object) -> Tuple[bool, Any]:
        with self._lock:
            if inst in self._data:
                val, cached = self._data[inst]
                return True, (val, cached)
            return False, (None, False)

    def set(self, inst: object, value: Any, cached: bool):
        with self._lock:
            self._data[inst] = (value, cached)

    def pop(self, inst: object):
        with self._lock:
            if inst in self._data:
                del self._data[inst]

    def items(self):
        with self._lock:
            return list(self._data.items())

class Descriptor:
    """
    Advanced reusable descriptor supporting:
    - validator: callable(value) -> value or raise ValidationError
    - default: callable() -> value (factory) or None
    - readonly: if True, value cannot be changed after first assignment
    - caching: stores per-instance computed/default value until invalidated
    Storage is weakref-backed to avoid memory leaks.
    """
    def __init__(self,
                 *,
                 validator: Optional[Callable[[Any], Any]] = None,
                 default: Optional[Callable[[], Any]] = None,
                 readonly: bool = False):
        self.validator = validator
        self.default = default
        self.readonly = readonly

        # storage holds per-instance (value, cached_flag)
        self._store = _PerInstanceStore()
        self._name: Optional[str] = None
        self._global_lock = threading.RLock()  # guards descriptor-level mutations

    def __set_name__(self, owner, name):
        # records assigned attribute name (useful for introspection)
        self._name = name

    def _run_validator(self, value):
        if self.validator is None:
            return value
        rv = self.validator(value)
        return rv

    def __get__(self, instance, owner=None):
        if instance is None:
            return self  # access on class returns descriptor itself

        found, (val, cached) = self._store.get(instance)
        if found:
            return val

        # Not found: compute default if available
        if self.default is not None:
            # default may be callable factory; call under lock to avoid races
            with self._global_lock:
                # Double-check after acquiring lock
                found2, (val2, cached2) = self._store.get(instance)
                if found2:
                    return val2
                value = self.default()
                value = self._run_validator(value)
                # cache default result
                self._store.set(instance, value, True)
                return value

        # No default and no stored value -> AttributeError as usual
        raise AttributeError(f"'{type(instance).__name__}' object has no attribute '{self._name or 'unknown'}'")

    def __set__(self, instance, value):
        with self._global_lock:
            found, (old, cached) = self._store.get(instance)
            if self.readonly and found:
                raise AttributeError(f"Attribute '{self._name or 'unknown'}' is read-only")
            value = self._run_validator(value)
            # store validated value, mark as cached (explicitly set)
            self._store.set(instance, value, True)

    def __delete__(self, instance):
        # allow deletion to remove stored value and allow re-computation from default
        self._store.pop(instance)

    def invalidate(self, instance):
        """Explicitly invalidate cached value for one instance (keeps no stored value)."""
        self._store.pop(instance)

    # Additional convenience for bulk initialization: called by owner to pre-populate defaults
    def _bulk_init_for(self, instance):
        "Compute and cache default for instance if default exists; no-op otherwise."
        if self.default is None:
            return
        found, _ = self._store.get(instance)
        if found:
            return
        # compute under lock to avoid duplicated factories
        with self._global_lock:
            found2, _ = self._store.get(instance)
            if found2:
                return
            value = self.default()
            value = self._run_validator(value)
            self._store.set(instance, value, True)
