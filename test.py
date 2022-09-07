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

#data types
#numbers: int, float, complex
a=10
b = 5.5
c = 2+5j

#use type() function to know the data type
print(a, "is of type ", type(a))
print(b, "is of type ", type(b))
print(c, "is of type ", type(c))

#use ininstance() to check in an object belongs to a particular class
m = 5
print(isinstance(5, complex))   #result: False
print(isinstance(m, int))       #result: True
print("is", m, "a floating point number?", "Ans: ", isinstance(m,float))

#list - mutable, square bracket
#create a list
countries = ["Nepal", "India", "USA", "UK"]
print(countries)
#add an item to the end of list
countries.append("Japan")
print(countries)
#add an item at specific position in the list
countries.insert(2, "China")    #China will be inserted at 3rd position
print(countries)

#remove an item from the list
countries.remove("India")
print(countries)

#remove an item from specific position
countries.pop(1)    #item at 2nd position will be removed
print(countries)
#remove the last item from the list
countries.pop()
print(countries)

#list can include items of different data types
list1 = [2, 3.5, 2+3j, 'hello', "world"]
print(list1)

#extract certain items from list
print(list1[1])     #prints item of 2nd position
print(list1[0:2])   #prints items from 1st to 2nd position
print(list1[3:])    #prints items from 4th position to the last position

#change the value of elements of a list
even_no = [0,2,4,6,8,10]
even_no[3] = 12         #4th position = 6 will be replaced by 12
print(even_no)

#Tuple - immutable, round brackets
subject = ('math', 'science', 'english', 'gk', 'accounts')
print(type(subject))

tuple1 = (1, 2.5, 1+2j, 'python')
print(tuple1)

#extract elements from a tuple
print(tuple1[2])     #prints 3rd element of tuple

print(subject[1:4])     #from science to gk i.e. index 1 to 3

#merge/join two tuples
tuple2 = subject + tuple1
print(tuple2)

#python set - curly brackets
p = {1,3,6,7,4,12,25,7}
print(p)
q= set((2,5,6,7,8))
print(q)
print(type(q))

#join two sets  set 3 = set1.union(set2)
r = p.union(q)
print(r)

#Python Dictionary - curly brackets, key value pairs
fruits = {
    1: 'apple',
    2: 'mango',
    3: 'orange',
    4: 'kiwi',
    5: 'pear'
}
print(type(fruits))
print(fruits)

#retrieve value using key
print(fruits[2])    #here, 2 is not index, its the key

#python strings
a = "I am a string"
print(a)

b = """I am a multiline string
I have two lines"""
print(b)

#extracting components of string using slicing operator [ ]
print(a[5])
x = 'apple'
print(x)
print("The fourth letter of", x, "is ", x[3])

#Type Conversion
print(float(2))
print(int(5.25))        #prints 5 (no round up)

set_name = set((1,2,3,5))
print(type(set_name))
print(set_name)

list_name = list('hello')
print(type(list_name))
print(list_name)

#converting string number into integer (explicit conversion/type casting)
num = "234"
print(num)
print(type(num))

num = int(num)
print(num)
print(type(num))

#implicit conversion
a = 2
b =5.6
c = a + b
print(type(c))

#range
x = range(5)
print(x)

#looping through a string
for x in "nepal":
    print(x)

#length of string
x = "nepal"
print(len(x))

#check if a certain phrase or character is present in a string
string = "Nepal is a country of himalayas."
print("country" in string)

if "country" in string:
    print("Yes, 'country' is present")
print('himalayas' not in string)

if "Nepal" not in string:
    print("No, 'Nepal' is not present in string")

#slicing strings
x = "Today is Tuesday"
print(x)
print(x[:7])        #slice from beginning to 6th index(7th position)
print(x[2:8])       #slice from 2nd to 7th index
print(x[4:])        #slice from 4th to last index

#negative indexing
y = "Namaste Nepal"
print(y[-4:-2])     #negative index starts from -1
                    #-4:-2 means -4 and -3 (-2 isn't included) = ep

#uppercase, lowercase
x = "Namaste Nepal"
print(x.upper())
print(x.lower())

#remove spaces from beginning and end of string
x = "  Hello World  "
print(x)
print(x.strip())

#replace string
x = "Hello World"
print(x.replace("World", "Nepal"))
print(x.replace("Hello", "Hi,"))

#split string
p = "Good morning, friend, have a nice day"
print(p.split(","))

#concatenate strings
x = "Hello"
y = "World"
z = "Good Morning"
a = x+y+z
print(a)

#adding space between variables
x = "Hello"
y = "World"
z = "Good Morning"
a = x + " " + y + " " + z
print(a)

#insert number into string using format()
age = 25
string = "My name is Pallavi, and I am {}"
print(string.format(age))

quantity = 4
price = 500
amount = quantity * price
text = "For {0} pieces costing Rs. {1} each, the total amount will be {2}."
print(text.format(quantity, price, amount))

#escape character \"
string = "Nepal is the birthplace of \"Gautam Buddha\""

#boolean values
print(5>4)
print(5==4)
print(4<5)

x = 400
y = 500
if x>y:
    print("x is greater than y")
else:
    print("x is less than y")

#evaluate values and variables using bool() function
print(bool("apple"))
print(bool(20))
print(bool(2.67))

print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print({})



























