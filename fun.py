#Python Functions

#defining a function
def greet():                    #greet is name of function
    print("Namaste")
    print("How are you?")       #nothing is printed here because the function is just defined, and not called

#calling the function defined above
greet()         #Namaste How are you? is printed now after the function is called

#Passing an argument to a function
def greet(name):
    print("Hello", name)
    print("How do you do?")
greet("Pallavi")
greet("John")

#passing multiple arguments to a function
def add_numbers(num1, num2):
    result = num1 + num2
    print("sum = ", result)

add_numbers(3,5)

a = 11.8
b = 3.9
add_numbers(a, b)

#function to calculate average score
def find_avg_score(score):
    sum_of_scores = sum(score)
    total_subjects = len(score)
    avg_score = sum_of_scores / total_subjects
    return avg_score

score = [60, 70, 65, 80, 75, 57, 83]
average = find_avg_score(score)             #average is just a variable name
print("You got an average score of ", average)

#function to find out grade from average score
def find_grade(average):        #average calculated by above code
    if average>=80:
        grade = 'A'
    elif average>=60:
        grade = 'B'
    elif average>=50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

score = [60, 70, 65, 80, 75, 57, 83]
average = find_avg_score(score)
print("You got an average score of ", average)

grade = find_grade(average)
print("Your grade is ", grade)

#using same function with different values
student1_marks = [80, 90, 79, 78, 69, 84, 82]
student1_average = find_avg_score(student1_marks)
print("You got an average score of ", student1_average)
student1_grade = find_grade(student1_average)
print("Your grade is ", student1_grade)

#program to add and multiply two numbers

def add_numbers(n1, n2):
    sum = n1 + n2
    return sum

def multiply_numbers(n1, n2):
    product = n1 * n2
    return product

print(add_numbers(145, 230))
print(multiply_numbers(20, 7))

#using docstring to describe what the function does
def greet(name):
    """This function greets to the person whose name is passed in the argument"""
    print("Hello, ", name)

#calling the function multiple times
greet("Ram")
greet("Sita")
greet("Ayush")

#return statement
def absolute_value(number):
    """This function returns the absolute value of a number"""
    if number>=0:
        return number
    else:
        return -(number)

print(absolute_value(3))

print(absolute_value(-5))

#testing scope and lifetime of variables defined inside and outside a function
x=20                    #this variable x has global scope
def func():
    x = 5               #this variable x has local scope
    print("inside function, x =", x)
func()
print("outside function, x =", x)

def give_name(first_name, last_name):
    return(first_name + " " + last_name)    #here if we use print instead of return, it will print 'My name is None'

name = give_name("Pallavi", "Shrestha")
print("My name is", name)

#when the number of arguments to be passed isn't known:

def add_nums(*num_list):
    result = sum(*num_list)
    return result

x = add_nums([2,3,4,5,6])
print("The sum is ", x)

y = add_nums([2,4,6,7,9,3,0,7])
print("The sum is ", y)

list1 = [20,34,56,78,90,23,-12,-50,-100]
print("The sum is ", add_nums(list1))

#arguments with key=value syntax
def nums(num1, num2, num3):
    print("The smallest number is ", min(num1, num2, num3))

nums(num1 = 2, num2 = 4, num3 = 1)

nums(4,5,6)

nums(35, -50, 46)

#when we dont know how many keyword arguments will be passed into the function:
#use **         #arbitrary arguments
def function(**students):
    print("His name is " + students["name"])
    print("His rank is " + students["roll_number"])

function(name = "Peter Parker", address = "London, UK", roll_number = "ten", rank = 4 )


#passing a list as an argument
def get_movie_name(movie):
    for i in movie:
        print("I have watched " + i)

marvel_movies = ["Ironman", "Dr Strange", "Thor: Love and Thunder", "Avengers: Endgame"]
anime_movies = ["Your Name", "Weathering with You", "Spirited Away"]
get_movie_name(marvel_movies)
get_movie_name(anime_movies)

#recursive function
def recursive_func(a):
    if a>0:
        result = a + recursive_func(a-1)
        print(result)
    else:
        result = 0
    return result
print(recursive_func(5))


def factorial(x):
    """recursive function to calculate the factorial of an integer"""
    if x == 1:          #base condition that stops the recursion
        return 1
    else:
        return (x * factorial(x-1))

x = 4
print("The factorial of ", x, "is", factorial(x))


#positional, keywords, and default arguments in python
#default parameter value
def get_country(country = "Nepal"):     #setting "Nepal" as default value
    print("I am from " + country)

get_country("India")
get_country("China")
get_country()                           #here, Nepal is printed

def add_numbers(n1 = 20, n2=30):
    sum = n1 + n2
    return sum

#here n1 and n2 are positional arguments
print(add_numbers(10, 15))      #10+15 = 25
print(add_numbers(45))          # 45 + 30 = 75  (n2 isn't given, so default value = 30 is used)
print(add_numbers())            # 20 + 30 = 50  (both n1 and n2 not given; default values used)

#keyword arguments
def greet(greeting, name):
    print(greeting, ",", name, ".")

greet(name = 'Peter', greeting = "Hello")

# ---------------------------------------------------------------------------------------------------------------------
# anonymous function / Lambda function
square = lambda num: num**2
print(square(5))

#this is the same as:
def square(num):
    squared_result = num**2
    return squared_result
print(square(5))

#using filter() function
numbers = [1,4,2,4,6,7,4,3,8,6,8,9]
"""function to get a list with even numbers only"""
new_numbers = list(filter(lambda x: (x%2 ==0), numbers))

print(new_numbers)