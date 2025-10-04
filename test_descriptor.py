import threading
import time
import gc
import pytest
from descriptor_framework import Descriptor, ValidationError

# Helper descriptors
def int_validator(v):
    if not isinstance(v, int):
        raise ValidationError("must be int")
    return v

def range_validator_factory(lo, hi):
    def v(x):
        if not (lo <= x <= hi):
            raise ValidationError(f"value {x} not in [{lo},{hi}]")
        return x
    return v

class MyModel:
    count = Descriptor(validator=int_validator, default=lambda: 0)
    percent = Descriptor(validator=range_validator_factory(0, 100), default=lambda: 50)
    tag = Descriptor(default=lambda: "x", readonly=False)
    frozen = Descriptor(default=lambda: "initial", readonly=True)

    # For bulk init test, we will dynamically add descriptors

def test_type_checking_and_default():
    m = MyModel()
    assert m.count == 0
    m.count = 5
    assert m.count == 5
    with pytest.raises(ValidationError):
        m.count = "nope"

def test_range_checking():
    m = MyModel()
    assert m.percent == 50
    m.percent = 100
    with pytest.raises(ValidationError):
        m.percent = 101

def test_readonly_descriptor():
    m = MyModel()
    assert m.frozen == "initial"
    with pytest.raises(AttributeError):
        m.frozen = "changed"
    # but mutable other descriptor works
    m.tag = "ok"
    assert m.tag == "ok"

def test_per_instance_caching_and_invalidation():
    m = MyModel()
    calls = []
    d = Descriptor(default=lambda: calls.append("gen") or 42)
    class C: val = d
    c = C()
    assert c.val == 42
    assert calls == ["gen"]
    # subsequent access doesn't call default
    assert c.val == 42
    assert calls == ["gen"]
    # invalidate and access -> regenerates
    d.invalidate(c)
    assert c.val == 42
    assert calls == ["gen", "gen"]

def test_weakref_cleanup():
    d = Descriptor(default=lambda: "temp")
    class C: val = d
    c = C()
    assert c.val == "temp"
    ref = weakref.ref(c)
    # delete instance and force GC
    del c
    gc.collect()
    assert ref() is None
    # descriptor internal store should not retain dead instance
    # inspect internal items
    items = d._store.items()
    assert all(k is not None for k, _ in items)  # weakdict drops dead entries

def test_thread_safety():
    d = Descriptor(validator=int_validator, default=lambda: 0)
    class C: val = d
    inst = C()
    errs = []

    def setter(i):
        try:
            d.__set__(inst, i)
        except Exception as e:
            errs.append(e)

    threads = [threading.Thread(target=setter, args=(i,)) for i in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    # last set should be some int; no exceptions
    assert not errs
    assert isinstance(inst.val, int)

def test_bulk_init_performance():
    # Create a class with many descriptors and time instantiation
    N = 500
    descriptors = {f'f{i}': Descriptor(default=lambda: 0, validator=int_validator) for i in range(N)}
    Large = type("Large", (), descriptors)
    # Warm-up
    obj = Large()
    t0 = time.perf_counter()
    obj2 = Large()
    t1 = time.perf_counter()
    elapsed = t1 - t0
    # Acceptable per-descriptor time: e.g., < 400 microseconds per descriptor on typical machine
    per_descriptor = elapsed / N
    assert per_descriptor < 0.0005, f"Per-descriptor init too slow: {per_descriptor:.6f}s"
