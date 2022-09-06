#python syntax
print("Hello, World!")
if 5>2:
    print ("5 is greater than 2")

#multiline comments
""" This is a 
multiline
comment """

#docstrings
def double(num):
    """Function to double the value"""
    return 2*num
print(double.__doc__)


#variables
x= 5
y=10
print(x+y)

y = 'John' #data type of y changed to str
x=float(5)  #data type of x changed to float
print(x)
print(y)
print(type(x))  #to get data type of variable x
print(type(y))

#assigning multiple values to multiple variables at once
x,y,z = 2, 'apple', 5.6
print(x)
print(y)
print(z)

#assign same value to multiple variables
a=b=c=d=10
print(a)
print(b)
print(c)
print(d)

#literals
#numeric literals
x = 0b10010010      #binary literals
y = 200             #decimal
z = 0o310           #octal
h = 0x12c           #hexadecimal
f1 = 1.3            #float
f2 = 1.5e2          #float: 1.5 x 10^2
c = 2.58j           #complex

print(x,y,z,h)
print(f1,f2)
print(c, c.imag, c.real)

#string literals
str = "Welcome to Fusemachines"
char = "A"
multi_str = """Welcome to Fusemachines
                Data Engineering Team"""
raw_str = r"raw\n string"
unicode= u"\fdjfdfds"

print(str)
print(char)
print(multi_str)
print(raw_str)
print(unicode)

#BooleanLiterals

a = (1 == False)
b = (0 == False)
x = True + 5
y = False +6
print("a is ", a)
print("b is ", b)
print("x: ", x)
print("y: ", y)

#special literals
drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

#literal collections
#list
veg = ["potato", "cabbage", "tomato", "okra"]
print(veg)

#tuple
integers = (1,2,3,-2,-4)
print(integers)

#dictionary
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'}
print(alphabets)

#set
animals = {'cat', 'dog', 'lion', 'cow'}
print(animals)






