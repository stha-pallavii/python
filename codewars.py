#solutions

#8kyu   #Grasshopper - Messi goals function
def goals(laLiga, copaDelRey, championsLeague):
    total_goals = laLiga + copaDelRey + championsLeague
    return total_goals

#8kyu   #Grasshopper - Grade book
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
def paperwork(n, m):
    if n<0 or m<0:
        return 0
    else:
        return n * m

#8kyu   #Basic Mathematical Operations
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
def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'

#8kyu   #Simple multiplication
def simple_multiplication(number) :
    if number%2==0:
        return number*8
    else:
        return number*9

#5kyu   #Weight for weight
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

#8kyu   #Reversing Words in a String
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

#4kyu   #Next bigger number with the same digits
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

#4kyu   #Don't give me five!
"""
def rang(a,b):
    for i in range(a,b+1):
        if '5' not in str(i):
            list.append(i)
    return (len(list))
    """

