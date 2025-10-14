from abc import ABC, ABCMeta, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    
    def habitat(self):
        return "Domestic"

# This raises an error
# dog = Dog()


class AbstractClass(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, other):
        print('subclass hook:', other)
        hookmethod = getattr(other, 'hookmethod', None)
        return callable(hookmethod)

class SubClass(object):
    def hookmethod(self):
        pass

class NormalClass(object):
    hookmethod = 'hook'


print(issubclass(SubClass, AbstractClass))
print(issubclass(NormalClass, AbstractClass))
