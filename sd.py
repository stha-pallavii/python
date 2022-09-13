#python SET and DICTIONARY

#SET

fruits = {'apple', 'mango','banana','kiwi'}
print(fruits)
print(type(fruits))

#try to create a set with duplicate items
fruits = {'apple', 'mango', 'kiwi','banana','kiwi','melon','melon'}
print(fruits)
#output = {'melon', 'mango', 'banana', 'apple', 'kiwi'}     duplicate items are removed

#create an empty set
setname = set()
print(type(setname))    #class = set

#if we run
newset = {}
print(type(newset))     #class = dict

#creating a set from a list /  converting a list into a set
veggies = set(['potato', 'tomato','okra','gourd','cucumber'])
print(veggies)
print(type(veggies))

#or
mylist = ['potato', 'tomato','okra','gourd','cucumber']
vegset = set(mylist)
print(vegset)

#add items to a set
vegset = {'tomato', 'potato', 'cucumber', 'okra', 'gourd'}
vegset.add("pepper")
print(vegset)

#add other iterables to a set       # 'update' method
vegetables = {'tomato','potato','okra','carrot','cucumber'}             #set
roots = ['radish','carrot','turnip']                #list
cucurbits = ('cucumber','gourds','pumpkin')         #tuple
spices = {'cumin','coriander'}                      #another set

#adding all elements of #list roots to #set vegetables
vegetables.update(roots)
print(vegetables)               #'carrot' isn't added because it already exists

#passing multiple iterables to the update method
vegetables.update(cucurbits, spices, ['onion', 'garlic'], ('tomato'))
print(vegetables)
#all elements from different iterables are added; duplicate items are removed


#remove an item from a set  #discard or remove or clear
spices.discard('cumin')
print(spices)

roots.remove('carrot')
print(roots)

#delete all items in a set  #clear
vegetables.clear()
print(vegetables)       #output = set() i.e. empty set

#set membership test    #in keyword
fruits = {'apple','mango','banana','peach'}
print('peach' in fruits)

#look through items in a set    #for loop
for fruit in fruits:
    print(fruit)


#python set operations      #union and intersection

#intersection
fruits = {'apple','mango','banana', 'jackfruit', 'tomato'}
vegs = {'potato','tomato','jackfruit','lettuce'}

food = fruits.union(vegs)
print(food)

#union using pipe '|' operator
y = fruits | vegs
print(y)

fruit_veg = fruits.intersection(vegs)
print(fruit_veg)

#intersection using ampersand '&' operator
x = fruits & vegs
print(x)

result = {1,5,10} & {100,10,3,5}
print("1.", result)                     #output = 1. {10, 5}

#SET difference     A - B  or  B - A

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

#using minus operator
print(set1 - set2)
print(set2 - set1)

#using .difference() function
set3 = set1.difference(set2)
print(set3)

print(set2.difference(set1))

#symmetric difference   (^ operator or symmetric_difference() )     # (A-B) union (B-A)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

#using ^ operator
print(set1 ^ set2)

#using symmetric_difference()
set3 = set1.symmetric_difference(set2)
print(set3)

#make a copy of a set
a = {2,3,5,7,8}
print(a.copy())

# difference_update()
# intersection_update()
# isdisjoint()
# issubset()
# issuperset()
# pop()
# symmetric_difference_update()


#frozenset
a = frozenset([2,3,4,5,6])
b = frozenset([5,6,7,8,9])

#------------------------------------------------------------------------------------------------------

# DICTIONARY

#create empty dictionary
a = {}
print(type(a))

mydict = {"name":"Ram", "age":25}
print(mydict)

#change keys of dictionary
mydict = {10: 'Ram', ('age'):25}
mydict = {'name':'Harry', 'age':30}

#access dictionary elements
"""keys are used as indices
eg: To get 'Ram',"""
print(mydict["name"])

"""To get 25,"""
print(mydict["age"])

#when we try to search a key that's not present in a dictionary --> error
#  print(mydict['address'])    #KeyError

#get() method #search if a key is present in a dictionary without getting error
print(mydict.get("address"))    #prints None

#passing a second argument to the get() method
#if the key being searched for doesn't exist, it will return the default value (passed in the second argument) instead of None
print(mydict.get("address", ['Ktm', 'Bagmati', 'Nepal']))

#add and change dictionary elements
person1 = {'name':'Jack','age':25, 'address': 'Ktm'}
#change the name to Jill
person1['name'] = 'Jill'
print(person1)

#add new item to a dictionary
person1['hobbies'] = ['dancing','fishing']
print(person1)      #new key i.e. hobbies created and ['dancing','fishing'] added

#remove elements from dictionary        #pop() method
person1.pop("name")
print(person1)

#to print the value of the item being removed, use print
print(person1.pop('hobbies'))

#remove an arbitrary item
print(mydict.popitem())
mydict.popitem()

#remove all items
mydict.clear()
print(mydict)

#delete the dictionary itself
del mydict


#iterating through dictionary       #for loop
person1 = {'name':'Jack','age':25, 'address': 'Ktm'}

for key in person1:
    print (key)

#print values of the dictionary in each iteration of the loop
for key in person1:
    print(person1[key])

#from python 3.7, order of items in dictionary is preserved
#when we iterate, we get the keys in the order in which they are in the dictionary

# Dictionary Comprehension
squares = {x: x*x for x in range(6)}

print(squares)                  #output = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}









