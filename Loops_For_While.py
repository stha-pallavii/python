#for and while loops

#program to find the product of all numbers in a list
nums = [1,2,3,4,5,6,7,8]
product = 1
for num in nums:
    product = product * num
print("The product is ", product)

#program to find the sum of all numbers in a list
nums = [1,2,3,4,5,6,7,8]
sum = 0
for num in nums:
    sum = sum + num
print(sum)

#range() function
print(range(6))             #output = range(0,6)
print(list(range(6)))       #output = [0,1,2,3,4,5]
print(range(3,7))           #output = range(3,7)
print(list(range(3,7)))     #output = [3,4,5,6]
print(range(2,15,4))
print(list(range(2,15,4)))

#range(start, stop, step_size)
a = range(2,12,2)
print(list(a))      #[2, 4, 6, 8, 10]

b = range(0,13,3)
print(list(b))      #[0,3,6,9,12]

#iterate through a list using indexing
heroes = ['ironman', 'spiderman', 'captain america', 'antman', 'thor', 'hulk']
for hero in range(len(heroes)):
    print('My fav superhero is', heroes[hero])

#for loop with else
nums = [1,5,7,8,9]
for i in nums:
    print(i)
else:
    print("loop terminated")

#for loop with if..else and break
patient_name = 'Tom'

record = {'John':100, 'Laura':101, 'Steve':103, 'Rick':104}

for patient in record:
    if patient == patient_name:
        print(record[patient])
        break
else:
    print('No record with that name found')

"""
patient_name = input('Enter patient name: ')

record = {'John':100, 'Laura':101, 'Steve':103, 'Rick':104}

for patient in record:
    if patient == patient_name:
        print(record[patient])
        break
else:
    print('No record with that name found')
"""

#nested loops
color = ['red', 'pink', 'white', 'yellow']
clothing = ['dress', 'skirt', 'shirt', 'gown']

for x in color:
    for item in clothing:
        print(x, item)

#-------------------------------------------------------------------------------------------------------
# WHILE LOOP

"""count = 0        #this loop runs infinitely because there is no condition when the test statement becomes false

while count<4:
    print()
    """

a = 10

sum = 0
i = 1

while i<=a:
    sum = sum + i
    i = i+1             #if this isn't done, loop will be infinite
print(sum)

#multiplication table of a number using while loop
"""number = int(input("Enter a number: "))

multiplier = 1
while multiplier <=10:
    product = number * multiplier
    print(number, "x", multiplier, "=", product)
    multiplier = multiplier + 1"""

#program to get multiplication table from 10 to 1
"""number = int(input("Enter a number: "))

multiplier = 10
while 0<multiplier<=10:
    product = number * multiplier
    print(number, "x", multiplier, "=", product)
    multiplier = multiplier - 1"""

#while loop with else
number = 0

while number <5:
    print(number)
    number = number + 1
else:
    print("numbers exhausted")      #as long as number<5, (while condition = True) body of while is executed
                                    #when number>=5 (while condition = False), else statement is executed

#break and continue
for num in range(2,8):
    print(num)
    break                 #gives only one output i.e. 2 and loop breaks

for num in range(1,10):
    if num == 4:
        break             #prints 1,2,3 and when num==4, loop is broken and prints nothing
    print(num)
print("completed")        #printed after getting out of the loop

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)      #prints apple only (loop breaks when x == banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break       #prints apple and banana (because break comes after printing x


"""
while True:
    number = int(input("Enter a number: "))
    if number<0:
        break
    print("You entered ", number)
"""

"""while True:
    number = int(input("Enter a number: "))
    if number<0:
        continue
    print("You entered: ", number)"""

"""for i in range(6):
    number = int(input("Enter a number: "))

    if number < 0:
        continue
    print(number)"""       #This will give "enter a number:" 6 times

#avoiding undefined values during division using continue
num = [2,4,5,0,7,5]

for i in num:
    if i==0:
        break
    ans = 20/i          #prints 20/2=10, 20/4=5, 20/5=4
    print(ans)          #when i==0, breaks

for i in num:
    if i==0:
        continue
    ans = 20/i
    print(ans)          #prints 20/all values of i  skipping the one when i==0

#pass
nums = [2,34,5,4,3]
for i in nums:
    pass

def fun(a):
    pass

class fruit:
    pass























