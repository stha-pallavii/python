"""# - weight for weight - 6kyu
def order_weight(strng):
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
    print(result)

#don't give me five! (4kyu)
for i in range:
	i --> string
	'5' in string? == False
	i
return len()


def rang(a,b):
    for i in range(a,b+1):
        if '5' not in str(i):
            list.append(i)
    return (len(list))

rang = range(1,9)
p

x = list(filter(lambda x:(x%5==0), *range(1,9)))




"""
#weight for weight -- proposed solution

x = len(list(filter(lambda x: '5' not in str(x) , [*range(1, 16)])))
print(x)

#weight for weight -- solution

def order_weight(strng):
    list = sorted(strng.split(' '))
    sort_after_sum = sorted(list, key=addition)
    return " ".join(sort_after_sum)

def addition(n):
  return sum([int(item) for item in n])

#moving zeros to the end
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

#simple pig latin

"""string
split string to form list
for each item in the list,
    move index[0] item to index[-1]
    add 'ay' to index[-1]
convert the list to string"""

x = 'Pig latin is cool'
def pig(latin):
    st_list = list(latin.split(' '))
    result=''
    for item in st_list:
        newst=''
        newst = item[1:] + item[0] +'ay'
        result = result + ' ' + newst
    return result.strip();

#reversing words in string
def reverse(st):
    list_st = list(st.split(' '))
    list_st.reverse()
    result= ''
    for i in list_st:
        result = result + ' ' + i
    return result.strip()


#Next bigger number with the same digits
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

print(next_big(513))






