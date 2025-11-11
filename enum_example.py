from enum import Enum, auto, IntEnum, Flag, unique
import json

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Access
print(Color.RED)           # Color.RED
print(Color.RED.name)      # 'RED'
print(Color.RED.value)     # 1

# Lookup by name or value
print(Color['RED'])       # Color.RED
print(Color(1))           # Color.RED

for c in Color:
    print(c.name, c.value)



class State(Enum):
    START = auto()
    RUNNING = auto()
    STOPPED = auto()

print(State.START.name, State.START.value)
print(State.RUNNING.name, State.RUNNING.value)
print(State.STOPPED.name, State.STOPPED.value)

# auto() assigns increasing integer values starting at 1.

class ErrorCode(IntEnum):
    OK = 0
    NOT_FOUND = 404
    SERVER_ERROR = 500

# IntEnum members are subclasses of int -> usable where ints are required:
assert isinstance(ErrorCode.OK, int)

# Use Flag/IntFlag for bitwise combinable flags (permissions, options).
class Permission(Flag):
    NONE = 0
    READ = auto()    # 1
    WRITE = auto()   # 2
    EXECUTE = auto() # 4
    ADMIN = READ | WRITE | EXECUTE

def has_write(perm):
    return bool(perm & Permission.WRITE)


# Combine
rw = Permission.READ | Permission.WRITE
print(rw & Permission.WRITE)   # Permission.WRITE
print(Permission.READ in rw)    # TypeError: use bitwise ops or comparison
# Test inclusion:
print(bool(rw & Permission.WRITE))    # True

# IntFlag behaves like int for bitwise ops and arithmetic if needed.


# Custom values, methods, and properties

class Status(Enum):
    NEW = (1, "New item")
    IN_PROGRESS = (2, "Being worked on")
    DONE = (3, "Finished")

    def __init__(self, code, description):
        self._code = code
        self.description = description

    @property
    def code(self):
        return self._code


print(Status.NEW.code)         # 1
print(Status.NEW.description)  # "New item"


# Alternative (customizing __new__ when you want numeric behavior):
class Priority(IntEnum):
    LOW = 1
    MEDIUM = 5
    HIGH = 10

# IntEnum can be used in arithmetic contexts.


# creating enums dynamically
Color2 = Enum('Color2', ['RED','GREEN','BLUE'])
print(Color2.BLUE, Color2.RED, Color2.GREEN)


# Uniqueness, aliases, and @unique
# By default, multiple names can map to identical values (aliases).

class Example(Enum):
    A = 1
    B = 1   # B is an alias of A

@unique
class Strict(Enum):
    A = 1
    B = 2
    # C = 1 # raise ValueError

# When aliasing occurs, only the first name appears in iteration and __members__.
print(list(Strict))



# Serialization JSON and Pickle
# Enums are pickable by default; unpickling returns the same singleton.


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return {'__enum__': str(obj)}  # "Color.RED"
        return json.JSONEncoder.default(self, obj)

def as_enum(d):
    if '__enum__' in d:
        name = d['__enum__']
        cls_name, member = name.split('.')
        # map cls_name to actual Enum class, e.g., via globals()
        return globals()[cls_name][member]
    return d

print(as_enum(MyEncoder().default(Color.RED)))


# Advanced: customizing auto() via _generate_next_value_

class Letters(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name.lower()
    A = auto()   # 'a'
    B = auto()   # 'b'


print(list(Letters))


# Mixins: combining behavior
# Combine Enum with mixins (str, int) carefully and order matters:

class StrEnum(str, Enum):
    def __str__(self):
        return self.value

class Color(StrEnum):
    RED = "red"
    GREEN = "green"

assert isinstance(Color.RED, str)


# When mixing, place mixin first (str, int) then Enum.