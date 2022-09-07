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
print('The value of p is %3.2f' %p)

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




