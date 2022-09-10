#Python data types in detail (List, Dictionary, Tuple, Set, Strings)

#number (int, float, complex)

x = 4
print(type(x))                  # class 'int'

print(float(x))                 # 4.0

y = 1 + 2j
print(y + 5)                    # 6 + 2j

print(isinstance(y, complex))   # True
print(isinstance(x, float))     # False

#converting values from different number systems to decimal (base 10)
print(0b1011)       # 11
print(0xFA)         # 250
print(0o17)         # 15

print(0b11011 + 0xFB + 0o15)    # 291

print(0.1+0.2)                  # output = 0.30000000000000004

#import decimal module to make decimal calculations more accurate
import decimal

from decimal import Decimal as D

print(D('0.1') + D('0.2'))      # output = 0.3


#python fractions module
"""import fractions
print(fractions.Fraction(1.5))     #output = 3/2"""

#python math module
import math

print(math.pi)                  #output = 3.141592653589793
print(math.exp(10))             #output = 22026.465794806718
print(math.log10(20))           #output = 1.3010299956639813
print(math.factorial(5))        #output = 120
print(math.sinh(0.5))           #output = 0.5210953054937474
print(math.cos(math.pi))        #output = -1.0

#------------------------------------------------------------------------------------------------------

#python LIST

#creating empty list
list1 = []

#list with mixed data types
list2 = [1, 'apple', 3.50, 2+3j]

#list index
dragons = ['drogon', 'syrax', 'caraxes', 'viserion', 'rhaegal', 'vhagar']
print(dragons[2])
print(dragons[0])       #prints the first element of the list

#negative indexing
print(dragons[-4])
print(dragons[-1])      #prints the last element of the list

#nested indexing
print(dragons[2][5])    #output = e
#dragons[2] = caraxes
#caraxes[5] = e

#list slicing
print(dragons[0:2])
print(dragons[:1])
print(dragons[3:])

print(dragons[-4:-1])
print(dragons[-3:])
print(dragons[:-2])

#add elements to the end of a list      #append

dragons.append('balerion')
print(dragons)

#extending lists
dragons.extend(['Tyraxes', 'Morghul', 'Shyrkos'])
print("extended list = ", dragons)

#add element at specific position       #insert
dragons.insert(2, 'rhaenyra')
print(dragons)

#concatenating lists
shinobi = ['naruto', 'sasuke', 'hinata', 'sakura', 'shikamaru']
sannin = ['jiraiya', 'tsunade', 'orochimaru']

print(shinobi + sannin)

#repeating lists
print(["re"]*3)
print(sannin *3)        #all elements of the list are repeated thrice

#delete one item from specific position of a list
del sannin[1]
print(sannin)

#delete multiple items
del shinobi[1:4]

#delete entire list
del sannin

#empty the contents of a list (without deleting the list)
shinobi.clear()
print(shinobi)      #prints empty list

#delete element from specific index     #pop
dragons.pop(2)
print(dragons)

#delete specific element    #remove
list = [1,2,3,4,5,3,6]
list.remove(4)
print(list)

list.remove(3)
print(list)         #removes first 3

#sorting lists
#sort a list in alphabetical order
slayers = ['Tanjiro', 'Zenitsu', 'Inosuke', 'Giyu', 'Kanao', 'Shinobu', 'Rengoku', 'Uzui']
slayers.sort()
print(slayers)

#sort a list in ascending order
nums = [4,2,6,7,3,2,6,8,9,10]
nums.sort()
print(nums)

#reverse the order of items in the list
print("nums before reversing: ", nums)
nums.reverse()
print("nums after reversing: ", nums)

#sort an unsorted list in descending order
numbers = [10,23,31,56,89,14,17,43,58]

numbers.sort()
numbers.reverse()
print(numbers)

#find the position (index) of an element
list = [4,2,6,7,3,2,6,8,9,10, 23,5,6]

print(list.index(3))
#prints the index of first occurrence of 3 i.e. 4

#find the count of an element in a list
list = [4,2,6,7,3,2,6,8,9,10,3,5,6]
print(list.count(2))

#list comprehension
#creating new list from an existing list

new_list = [x*3 for x in range(5)]          #takes the list [0,1,2,3,4]
print(new_list)                             #output = [0, 3, 6, 9, 12]

#if statement in list comprehension
odd_list = [x for x in range(20) if x%2 == 1]
print(odd_list)

even_list = [n for n in range(20) if n%2==0]
print(even_list)

#------------------------------------------------------------------------------------------------------

#python TUPLES

#create an empty tuple
tuple1 = ()
print(tuple1)

# create tuple having single data type
tuple2 = (1,2,3,4,5,34)
tuple3 = ('a', 'b', 'c', 'd')
print (tuple2); print(tuple3)

#tuple having mixed data types
tuple4 = (10, 2.68, 'powder', 3+5j)

#nested tuple
tuple5 = ("Harry", (2,3), [3.7, 8.9])
print(tuple5)                        #output = ('Harry', (2, 3), [3.7, 8.9])

#tuple packing
tuple6 = 1, 6.7, 23, 'pallavi'
print(tuple6)

#tuple unpacking
a,b,c,d = tuple6
print(a)
print(b)
print(c)
print(d)

#a trailing comma indicates tuple
a = ("hello")
print(type(a))      #output = <class 'str'>

a = ("hello",)      #the trailing comma makes this a tuple
print(type(a))      #output = <class 'tuple'>

a = "hello",        #comma makes it a tuple despite lacking parentheses
print(type(a))      ##output = <class 'tuple'>

















