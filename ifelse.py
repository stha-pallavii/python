#Python if...else statement

x = 5
#program to know if x is positive, negative or zero
if x>0:
    print(x, "is a positive number")
elif x==0:
    print(x, "=0")
else:
    print(x, "is a negative number")

"""
a = int(input("Enter a number: "))
if a>0:
    print(a, "is positive")
elif a<0:
    print(a, "is negative")
else:
    print(a, "is zero")
"""

x = 10
y = 12
if x>y:
    print(x, "is greater than", y)
elif x==y:
    print(x, "is equal to", y)
else:
    print(x, "is less than", y)

#short hand if
a = 2
b = 3
if a<b: print("a is smaller than b")  #if only one statement, it can be put on the same line as the if statement

#short hand if...else
print("a is greater") if a>b else print("b is greater")

#multiple else statements on same line
a = 10
b = 15
print(a, "is greater") if a>b else print(a, "=", b) if a==b else print(b, "is greater")

#if..else with 'and'
x = 10
y = 15
z = 20
if x<y and y<z:
    print(y, "is greater than", x, "but less than", z)

#if..else with 'or'
if x>y or y>z:
    print("At least one of the conditions is True")
else:
    print("Both conditions are False")

#Nested If
a = int(input("Enter a number: "))
if a>=5:
    print(a, "is greater than or equal to 5")
    if a>10:
        print("and also greater than 10")
        if a>15:
            print("and also greater than 15")
        else:
            print("but not greater than 15")
else:
    print(a, "is less than 5")

#pass statement
x = 10
y = 15
if x==y:
    pass        #doesn't give any error even when we leave an if statement without content






