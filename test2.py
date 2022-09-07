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
x = 10
y = 4

print(x & y)
print (x | y)
print(~x)
print(x ^ y)
print(x >> y)
print(x << y)

#assignment operators

#identity operators










