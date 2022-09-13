#solutions

#8kyu   #Grasshopper - Messi goals function
"""
Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions
Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.

For example:

5, 10, 2  -->  17
"""
def goals(laLiga, copaDelRey, championsLeague):
    total_goals = laLiga + copaDelRey + championsLeague
    return total_goals

#8kyu   #Grasshopper - Grade book
"""
Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'
Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
"""
def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3)/3
    if average>=90 and average<=100:
        return 'A'
    if average>=80 and average<90:
        return 'B'
    if average>=70 and average<80:
        return 'C'
    if average>=60 and average<70:
        return 'D'
    if average>=0 and average<60:
        return 'F'

#8kyu   #Beginner Series #1 School Paperwork
"""
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

Example:
n= 5, m=5: 25
n=-5, m=5:  0
"""
def paperwork(n, m):
    if n<0 or m<0:
        return 0
    else:
        return n * m

#8kyu   #Basic Mathematical Operations
"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
"""
def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1-value2
    elif operator == '*':
        return value1*value2
    elif operator == '/':
        return value1/value2

#8kyu   #Grasshopper - Personalized Message
"""
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

case	return
name equals owner	'Hello boss'
otherwise	'Hello guest'
"""
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'

#8kyu   #Simple multiplication
"""
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""
def simple_multiplication(number) :
    if number%2==0:
        return number*8
    else:
        return number*9

#8kyu   #Reversing Words in a String
"""
DESCRIPTION:
You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
"""
def reverse(st):
    return " ".join(w for w in st.split()[::-1])

"""
def reverse(st):
    list_st = list(st.split(' '))
    list_st.reverse()
    result= ''
    for i in list_st:
        result = result + ' ' + i
    return result.strip()
    """

#5kyu   #Weight for weight
"""
My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.

Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 

"100 180 90 56 65 74 68 86 99"
When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:

180 is before 90 since, having the same "weight" (9), it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.
"""
def order_weight(strng):
    list = sorted(strng.split(' '))
    sort_after_sum = sorted(list, key=addition)
    return " ".join(sort_after_sum)

def addition(n):
  return sum([int(item) for item in n])

"""
x = len(list(filter(lambda x: '5' not in str(x) , [*range(1, 16)])))
print(x)
"""

"""def order_weight(strng):
    sl = sorted(strng.split(" "))
    d={}
    for key in sl:
        sum=0
        for a in key:
            sum = sum + int(a)
        d[key]=sum
    result=""
    for w in (sorted(d, key=d.get, reverse=False)):
        result= result + " " + w
    print(result)"""

#5kyu   #Moving Zeros To The End
"""
DESCRIPTION:
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""
def move_zeros(lst):
    list1 = []
    list2 = []
    for item in lst:
        if item==0:
            list1.append(item)
        else:
            list2.append(item)
    lst = list2 + list1
    return lst

#5kyu   #Simple Pig Latin
"""
DESCRIPTION:
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""
def pig_it(text):
    st_list = list(text.split(' '))
    result=''
    for item in st_list:
        newst=''
        asic_v = ord(item[0])
        if((asic_v>=65 and asic_v<=90) or (asic_v>=97 and asic_v<=122)):
            newst = item[1:] + item[0] +'ay'
            result = result + ' ' + newst
        else:
            result = result + ' ' + item[0]
    return result.strip();


#4kyu   #Next bigger number with the same digits
"""
DESCRIPTION:
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
"""
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1

"""
def next_big(num):
    num2=num
    if(num2<10):
        return -1
    while(num2>9):
        lastd=num2%10
        num2=num2//10
        last2d=num2%10
        if(lastd>last2d):
            result = (num2//10)*10+lastd
            return result*10+last2d
            """

#4kyu   #Don't give me five! Really!
"""
DESCRIPTION:
This kata is the performance version of Don't give me five by user5036852.

Your mission, should you accept it, is to return the count of all integers in a given range which do not contain the digit 5 (in base 10 representation).
You are given the start and the end of the integer range. The start and the end are both inclusive.

Examples:

1,9 -> 1,2,3,4,6,7,8,9 -> return 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> return 12
The result may contain fives. ;-)
The start will always be smaller than the end. Both numbers can be also negative.

The regions can be very large and there will be a large number of test cases. So brute force solutions will certainly time out!
"""
def rang(a,b):
    for i in range(a,b+1):
        if '5' not in str(i):
            list.append(i)
    return (len(list))



