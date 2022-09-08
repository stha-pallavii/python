#Python input, output and import
print('testing output data')

#changing separator
print('a', 'b','c','d')
print('a', 'b','c','d', sep='#')
print('a','b','c','d', sep='*', end = '%')

#output formatting   str.format()
a = 4; b = 6
print('The value of a is {} and that of b is {}'.format(a,b))

print('{0} and {1} wins the race'.format('slow', 'steady'))
print('I love listening to {0}, {1}, and {2}'.format('beatles','bob marley', 'taylor swift'))

#using keyword arguments to format the string output
print('{title} {name} is the {position} of our company.'.format(title='Mr.', name='Ram Shrestha',position='CEO'))
print('{title} {name} is the {position} of our company.'.format(title='Mr.',name='Sam Karki',position='Manager'))
print('{title} {name} is the {position} of our company.'.format(title='Miss.', name='Sweta Gurung',position='Accountant'))

#formatting strings using % operator
p = 10.56876
print('The value of p is %3.2f' %p)     #In 3.2f, f means floating point number
                                                 #2 means 2 digits after decimal
                                                 #3 means minimum 3 digits(in total) such that len(str(p)) = 3  -- decimal sign (.) is also counted
print('%7.2f' %p)   #prints '  10.57' i.e. total length = 7 (by adding spaces at first)


#Input function
#code = input('Enter the code: ')
#print(code)         #here, the value will be a string despite entering a number

#eval() function
print(eval('10+2+6'))

#Python Import Keyword  #import a module (constant)
import constant
print(constant.CONSTANT1)
print(constant.CONSTANT_2)

#import specific attributes and functions using 'from' keyword
from constant import CONSTANT1
print(CONSTANT1)

#--------------------------------------------------------------------------------------
#python operators
#arithmetic operators

x = 5
y = 3
z = 20

print(x+y+z)
print('x+y-z = ', x+y-z)

print('x times y is ', x*y)

print(z/y)
print('The modulus of x/y is ', x%y)

print(z//y)
print(x**3)

#Comparison operators   #return True or False
a = 10
b = 15
c = 20

print(a>b)
print('c > b is ', c>b)

print(a*b == b*c - a*b)
print('a <=b is', a <= b)

#logical operators
A = True; B = False
print('A and B is', A and B)
print('A or B is', A or B)
print('not A is ', not A)
print('not B is ', not B)

#bitwise operators
x = 10  #binary: x = 0000 1010
y = 4   #binary: y = 0000 0100

print(x & y)    #1 & 1 = 1, rest all combinations = 0   #result = 0000 0000 = 0
print (x | y)   #1 & 1 = 1, 1 & 0 = 1, 0 & 1 = 1, 0 & 0 = 0     #result= 0000 1110 = 14
print(~x)       # ~x = -(x+1) = -(1010 + 1) = -1011 = -11
print(x ^ y)    #xor returns 1 when only one operand is 1 i.e.
                # 0 & 1 = 1, 1& 0 = 1, 1 & 1 = 0, 0 & 0 = 0
                #x^y = 0000 1110 = 14
print(x>>1)     #right shift >> removes digit/s from right i.e.
                # x >> = 0000 1010>> = 0000 0101 = 5
print(x<<1)     #removes digit/s from left and adds zero at the right end
                # x << = 0000 1010<<  =  0000 0100 = 20
print(x>>2)     #removes 2 digits from right and puts 00 at front(left)
                #x>>2 = 0000 1010 >>2 = 0000 0010 = 2


#assignment operators
x = 5
x += 5;  print(x)       #x = x+5 = 5+5 = 10
x -= 5; print(x)        #x = x-5 =10-5 = 5
x *= 2; print(x)        #x = x*2 = 5*2 = 10
x /= 2.5; print (x)     #x = x/2.5 = 10/2.5 = 4.o
x %= 3; print(x)        #x = x % 3 = 4.0 % 3 = 1.0
x //= 2; print(x)       #x = x//2 = 1.0//2 = 0.5 = 0.0
x **=2; print(x)        #x = x**2 = 0.0**2 = 0.0

x=6                     #x = 6
x&=5; print(x)          #x = x&5 = 6&5 = 0000 0110  & 0000 0101 = 0000 0100  =4
x |= 5; print(x)        #x = x|5  = 4|5 = 0000 0100  |  0000 0101  = 0000 0101  =5
x ^=2; print(x)         #x = x^2  = 5^2 = 0000 0101 ^ 0000 0010    = 0000 0111  =7
x>>=3; print(x)         #x = x>>3 = 7>>3    =0000 0010 >> 3 =0000 0000 =0

x=11
x<<=3; print(x)         #x<<3 = 11<<3   =0000 1011 <<3  =0101 1000  =88


#identity operators
a = 3
b = 3
c = 'apple'
d = 'apple'
e = ('x', 'y', 'z')
f = ('x', 'y', 'z')
print(a is b)           #True
print(c is not d)       #False
print(a is c)           #False
print(e is f)           #True

#membership operators
a = 'Mount Everest'
print('M' in a)             #True
print('Eve' in a)           #True
print('eve' in a)           #False
print('rest' not in a)      #False

b = {'key1':'river', 'key2':'lake', 'key3':'sea', 'key4':'ocean'}
print('key1' in b)          #True
print('sea' in b)           #False (because in dictionary, we can only test the presence of key - not value.

#python namespace and scope
#get the address of objects using id()
a = 5
print(id(a))
print(id(5))
#same address is obtained

a = 5
print('address of a = ', id(a))             #2062299758960

a = a+1
print('address of a = ', id(a))             #2062299758992  = new address
print(print('address of 6 = ', id(6)))      #same as above

b = 10
print(id(b))
print(id(10))           #same

#name of function
def fun1():
    print("Hi")
x = fun1
x()

#scope and namespace in python
def outer_function():
    x = 5                       #variable x is in local namespace of outer_function()
    def inner_function():
        y = 10                  #variable y is in the nested local namespace of inner_function()
z = 15                          #variable z is in global namespace


def outer_function():
    x = 10

    def inner_function():
        x = 20
        print(x)                #prints 20
    inner_function()
    print(x)                    #prints 10
x = 30
outer_function()
print(x)                        #prints 30

#using keyword global
def outer_function():
    global x
    x = 10

    def inner_function():
        global x
        x = 20
        print(x)            #prints 20

    inner_function()
    print(x)                #prints 20

x = 30
outer_function()
print(x)                    #prints 20
#due to use of keyword 'global', all references and assignments are to the global x









