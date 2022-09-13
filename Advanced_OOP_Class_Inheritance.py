#Advanced Python
#Object Oriented Programming    #Class  #Inheritance

class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

student1 = Student()
student1.name = 'Jane'
student1.marks = 50
passed = student1.check_pass_fail()

print(student1.name)
print(student1.marks)

print(passed)                   #returns True


#another object
student2 = Student()
student2.name = 'Megan'
student2.marks = 35
passed = student2.check_pass_fail()
print(passed)                           #returns False"""

#adding attributes manually after defining the object isn't a good practice
#use the  __init__()    method

# __init__() method     #example 1

class movie:
    def check_rating(self):
        if self.rating >= 7:
            return 'Very good'
        elif self.rating >=5:
            return 'Average'
        else:
            return 'Poor'

    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating

movie1 = movie("Avengers", 'sci-fi', 8)
print(movie1.name)
print(movie1.genre)
print(movie1.rating)
print(movie1.check_rating())

movie2 = movie("Conjuring", "horror", 6)
print(movie2.name)
print(movie2.genre)
print(movie2.rating)
print(movie2.check_rating())

#example 2
#creating class with atributes using __init__() method
class fruit:
    def __init__(self, name, color, climate):
        self.name = name
        self.color = color
        self.climate = climate

fruit1 = fruit("apple", "red", "temperate")
print(fruit1.name)
print(fruit1.color)
print(fruit1.climate)


#example 3
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def results(self):
        if self.marks >= 60:
            return 'First Division'
        elif self.marks >= 40:
            return 'Second Division'
        else:
            return 'Failed'


student1 = student("Amy", 35)
student2 = student("Jack", 60)
student3 = student("Benedict", 50)
exam_result = student1.results()
print(exam_result)
exam_result = student2.results()
print(exam_result)
exam_result = student3.results()
print(exam_result)


#adding two complex numbers
#example 4
class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag


    def add(self, number):
        real = self.real + number.real
        imag = self.imag + number.imag
        result = complex(real, imag)
        return result

#create objects
num1 = complex(5,6)
num2 = complex(-4,2)

result = num1.add(num2)     #num1 = self    num2 = number
print("real = ", result.real)
print("imag = ", result.imag)


#programming task   #example 5
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def find_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter

t1 = Triangle(3,4,5)
perimeter = t1.find_perimeter()
print("Perimeter of Triangle t1 = ", perimeter, 'cm')

t2 = Triangle(6,8,10)
print(t2.find_perimeter())


#example 6
class Cereal_Crop:
    #class attribute
    family = "Poaceae"

    #instance(object) attributes
    def __init__(self, common, genus, species, chromosome):
        self.common = common
        self.genus = genus
        self.species = species
        self.chromosome = chromosome

#define objects/instances of Cereal_Crop class
rice = Cereal_Crop("rice", "Oryza", "sativa", 24)
wheat = Cereal_Crop("wheat", "Triticum", "aestivum", 42)
maize = Cereal_Crop("maize", "Zea", "mays", 20)

#access the attributes of the class     #use    __class__.attributename

print("Rice belongs to family {}".format(rice.__class__.family))
print("Wheat is also a member of the family {}".format(wheat.__class__.family))
print("Maize also belongs to family {}".format(maize.__class__.family))

#access the attributes of the objects       #use    objectname.attributename
print("{} {} has {} chromosomes".format(rice.genus, rice.species, rice.chromosome))
print("{} {} has {} chromosomes".format(wheat.genus, wheat.species, wheat.chromosome))
print("{} {} has {} chromosomes".format(maize.genus, maize.species, maize.chromosome))

#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

#methods (functions defined inside the body of a class)
class Flower:
    def __init__(self, id, name, color):        #instance attributes
        self.id = id
        self.name = name
        self.color = color

    def symbol(self, meaning):                  #instance method
        return "{} {} symbolizes {}".format(self.color, self.name, meaning)

    def stock(self, number):                    #instance method
        if number == 0:
            return "We do not have any {} available.".format(self.name)
        elif number == 1:
            return "We have only one {} available.".format(self.name)
        else:
            return "We have {} {}s available.".format(number, self.name)

#defining objects in the class Flower
f1 = Flower(1, "rose", "red")
f2 = Flower(2, "rose", "yellow")
f3 = Flower(3, "lily", "white")

#printing objects with their attributes
print(f1.id, '.', f1.color, f1.name)
print(f2.id, '.', f1.color, f1.name)
print(f3.id, '.', f1.color, f1.name)

#printing method 'symbol'
print(f1.symbol('love'))
print(f2.symbol('friendship'))
print(f3.symbol('purity'))

#printing method 'stock'
print(f1.stock(20))
print(f2.stock(0))
print(f3.stock(1))

#--------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------

# INHERITANCE

#define parent class
class Animal:

    def __init__(self):
        print("Animals are lovely")

    def type(self):
        print("Domestic Animal")

    def foodtype(self):
        print("Herbivorous")

#create child class from parent class 'Animal'
class Panda(Animal):

    def __init__(self):
        #call super() function      #super() function allows us to run the __init__() method of the parent class inside child class
        super().__init__()
        print("Pandas are lovely")

    def type(self):
        print("Wild Animal")

    def eat(self):
        print("bamboo")

panda1 = Panda()
panda1.type()
panda1.eat()
panda1.foodtype()   #foodtype() function isn't defined inside child class but it works because
                    #child class inherits the functions of parent class


#--------------------------------------------------------------------------------------------------------------------------------------------

# Encapsulation