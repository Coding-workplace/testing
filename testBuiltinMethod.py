#eval(expression,globals=None,locals=None)
x = 10
y = 20

# Simple arithmetic expression
result = eval('x + y')
print(result)  # Output: 30

# Using globals and locals
globals_dict = {'x': 5, 'y': 8}
locals_dict = {'z': 3}
result = eval('x + y + z', globals_dict, locals_dict)
print(result)  # Output: 16

#exec(source,globals=None,locals=None)
# Example 1: Executing a simple statement
x = 10
exec('y = x + 5')
print(y)  # Output: 15

# Example 2: Executing multiple statements
code_to_execute = """
for i in range(5):
    print(i)
"""
exec(code_to_execute)
# Output:
# 0
# 1
# 2
# 3
# 4


#hash(obj)
print(hash(5))  #5
print(hash("d"))#hash number
#Two objects that compare equal must also have the same hash value, but the 
#reverse is not necessarily true.

#id(obj)
a=5
print(id(a)) #an id of object
#This is guaranteed to be unique among simultaneously existing objects.
#(CPython uses the object's memory address.)

#int()
print(int())
print(int("121",base=10))


#filter(function_or_none,iterable)
fobj=filter(lambda x: x%2==0,[1,2,3,4]) #return filter obj
print([i for i in fobj])

#map(func,iterable)
print(list(map(lambda x: x+1,[1,2,3,4,5])))
print(list(map(lambda x,y: x+y,[1,2,3,4,5],[6,7,8,9,10])))


#reversed
print(list(reversed([1,2,3,4,5])))

#slice
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_slice = slice(2, 7, 2)

sliced_result = my_list[my_slice]
print(sliced_result)

#zip
l=[(a,b,c) for a,b,c in zip("darshil",range(7),"solanki")]
print(l)
#[('d', 0, 's'), ('a', 1, 'o'), ('r', 2, 'l'), ('s', 3, 'a'),
# ('h', 4, 'n'), ('i', 5, 'k'), ('l', 6, 'i')]

#iter
l=[ i for i in iter("darshil")]
print(l)
#['d', 'a', 'r', 's', 'h', 'i', 'l']

#print
f=open("demo.txt",'w')
print("Writing to file using print function",file=f)

#FORMAT
#Accessing arguments’ attributes:
c = 3-5j
('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.').format(c)
#The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.

#Accessing arguments’ items:
coord = (3, 5)
'X: {0[0]};  Y: {0[1]}'.format(coord)
# X: 3;  Y: 5

#Replacing "%s" and "%r":
"repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
#"repr() shows quotes: 'test1'; str() doesn't: test2"

#Aligning the text and specifying a width:
'{:<30}'.format('left aligned')
#'left aligned                  '
'{:>30}'.format('right aligned')
#'                 right aligned'
'{:^30}'.format('centered')
#'           centered           '
'{:*^30}'.format('centered')  # use '*' as a fill char
#'***********centered***********'

#Replacing "%+f", "%-f", and "% f" and specifying a sign:
'{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
#'+3.140000; -3.140000'
'{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
#' 3.140000; -3.140000'
'{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
#'3.140000; -3.140000'

#Replacing "%x" and "%o" and converting the value to different bases:
# format also supports binary numbers
"int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
#'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
# with 0x, 0o, or 0b as prefix:
"int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
#'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

#Using the comma as a thousands separator:
'{:,}'.format(1234567890)
#'1,234,567,890'

#Expressing a percentage:
points = 19
total = 22
'Correct answers: {:.2%}'.format(points/total)
#'Correct answers: 86.36%'

#Using type-specific formatting:
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
'{:%Y-%m-%d %H:%M:%S}'.format(d)
#'2010-07-04 12:15:58'

# the ellipsis (...) is a literal notation that represents an ellipsis object.
# This object is often used as a placeholder or to indicate incomplete code or data structures. 
def my_function():
    ...
def my_function() -> ...:
    pass
def my_function() -> ...:
    pass

#local variable
print(locals())
#global variable
print(globals())

#vars
print(vars())#same as locals()
print(vars(bool))#same as obj.__dict__()

#memoryview
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view[7])  # Output: 119 (ASCII value of 'w')
view[7] = ord('W')  # Change 'w' to 'W'
print(data)  # Output: bytearray(b'Hello, World!')


#isinstance
print(isinstance(5,str)) #False
print(isinstance(5,(str,int))) #True


#super 
class A:
    def age(self):
        print("Age is 21")
class B:
    def age(self):
        print("Age is 23")
class C(A, B):
    def age(self):
        super(C, self).age()
     
c = C()
print(C.__mro__)
print(C.mro())
c.age() #call to A age methood print Age is 21

#classmethod
class D:
    @classmethod
    def display(cls):
        print(cls)

d=D()
d.display()
D.display()

class E:
    @staticmethod
    def display():
        print("static method")

e=E()
e.display()
E.display()


#property
class MyClass:
    def __init__(self):
        self._x = None
    def get_x(self):
        return self._x
    def set_x(self, value):
        self._x = value
    def del_x(self):
        del self._x
    # Define property
    x = property(get_x, set_x, del_x, "This is the 'x' property.")

# Usage
obj = MyClass()
obj.x = 10  # Calls set_x
print(obj.x)  # Calls get_x
del obj.x    # Calls del_x

class MyClass1:
    def __init__(self):
        self._x = None
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    @x.deleter
    def x(self):
        del self._x
# Usage
obj = MyClass1()
obj.x = 10  # Calls x.setter
print(obj.x)  # Calls x getter
del obj.x    # Calls x deleter
