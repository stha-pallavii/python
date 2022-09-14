#Advanced Python        #Iterators

numbers = [1,4,9]

print(dir(numbers))             #gives the methods in list
value = numbers.__iter__()
print(value)
print(list(value))



nums = [1,4,9]
value = nums.__iter__()     #variable 'value' is an iterator

#we can get each element of this iterator using the __next__() method

# __next__()  method
item1 = value.__next__()
print(item1)

item2 = value.__next__()
print(item2)

item3 = value.__next__()
print(item3)

#alternatively,     nums.__iter__()  =  iter(nums)
                  # value.__next__() =  next(value)

numbers= [1,2,3,4]
val = iter(numbers)

item1 = next(val)
print(item1)

item2 = next(val)
print(item2)

item3 = next(val)
print(item3)

item4 = next(val)
print(item4)

"""item5 = next(val)
print(item5)"""            #raises StopIteration exception


#working of for loops
num_list = [1,3,5]

iter_obj = iter(num_list)          #created iterator object named iter_obj from the list num_list using the iter() function

#create an infinite while loop
while(True):
    try:
        element = next(iter_obj)        #next method used inside th while loop to get the next element in the sequence
        print(element)
    except StopIteration:               #when all items of the iterator are iterated, the try block raises StopIteration exception and we break out of the loop
        break

#doing the same thing using for-loop
num_list = [1,3,5]
for element in num_list:
    print(element)


#Creating Custom Iterators
#create a program that will generate a sequence of even numbers (0,2,4,6,8,.....)

class even:
    def __init__(self, max):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n = self.n + 2
            return result
        else:
            raise StopIteration

numbers = even(10)
print(next(numbers))    #0
print(next(numbers))    #2
print(next(numbers))    #4
print(next(numbers))    #6
print(next(numbers))    #8
print(next(numbers))    #10
# print(next(numbers))  #raises StopIteration error (because max = 10)

nums = even(6)
print("first even number: ", next(nums))
print("second even number: ", nums.__next__())
print("third even number: ", next(nums))
print("fourth even number: ", next(nums))
# print("fifth even number: ", next(nums))      #StopIteration


#create a program that will generate a sequence of odd numbers (1,3,5,7,.....)

class Odd:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self.num
            self.num += 2
            return result
        except:
            return "StopIteration"

num = Odd()
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))








