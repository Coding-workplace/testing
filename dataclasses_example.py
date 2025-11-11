from dataclasses import dataclass, field, InitVar, asdict
from typing import ClassVar

@dataclass
class Point:
    x: float
    y: float = 0.0

p = Point(12, 13.5)

@dataclass
class Bag:
    items: list[int] = field(default_factory=list) # safe: unique per instance



@dataclass
class Person:
    name: str
    nickname: InitVar[str] = None

    def __post_init__(self, nickname):
        self.nickname = nickname or self.name[:3]


@dataclass
class C:
    VERSION: ClassVar[str] = '1.0'


@dataclass(order=True)
class Item:
    sort_index: int = field(init=False, repr=False)
    name: str
    priority: int

    def __post_init__(self):
        self.sort_index = -self.priority


@dataclass
class Circle:
    r: float
    area: float = field(init=False)

    def __post_init__(self):
        self.area = 3.14159 * self.r * self.r

c = Circle(5)
print(c)

# Use functools.cached_property (or manual caching)

# Nested dataclasses with asdict/from-dict helper

@dataclass
class Address:
    city: str
    zip: str

@dataclass
class Person:
    name: str
    address: Address

p = Person("Alice", Address("NYC", "10001"))
d = asdict(p) # {'name': 'Alice', 'address': {'city': 'NYC', 'zip': '10001'}}
print(d)

# Reconstruct manually:
p2 = Person(name=d['name'], address=Address(**d['address']))
print(p)
print(p2)


# inheritance


# parent class
@dataclass
class Staff:
    name: str
    emp_id: str
    age: int

# child class
@dataclass
class employee(Staff):
    salary: int


emp = employee("Satyam", "ksatyam858", 21, 60000)
print(emp)

