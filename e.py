#Advanced Python
#Exception Handling

numerator = 5
denominator = 0
# print(numerator/denominator)      #ZeroDivisionError: division by zero
                                    #here, exception = ZeroDivisionError

#handling exceptions = responding to exceptions in a custom way during program execution

#try.....except
#syntax:
try:
    #code that may cause exception
    pass
except:
    #code to run in case exception occurs
    pass

#example
try:
    numerator = int(input("Enter numerator:"))
    denominator = int(input("Enter denominator:"))

    result = numerator/denominator
    print(result)

except:
    print("Denominator cannot be zero. Please try again")

print("end")

#handling specific exception    #specify type of exception after the 'except' keyword
#useful when try block can raise more than 1 type of exception
try:
    numerator = int(input("Enter numerator:"))
    denominator = int(input("Enter denominator:"))

    result = numerator/denominator
    print(result)

except ZeroDivisionError:
    print("Denominator cannot be zero. Please try again")

print("end")

#example: try block that may raise both ZeroDivisionError and IndexError
try:
    numerator = int(input("Enter numerator:"))
    denominator = int(input("Enter denominator:"))

    result = numerator/denominator
    print(result)

    num_list = [4,5,6,7]
    i = int(input("Enter index: "))         #if user enters index outside the num_list, raises IndexError (here num_list = [4,5,6,7] --> index = 0,1,2,3
    print(num_list[i])

except ZeroDivisionError:
    print("Denominator cannot be zero. Please try again")
except IndexError:
    print("Index cannot be greater than the size of the list")

print("end")

# try.........finally       #finally block - executed regardless exception raise
try:
    print(1/0)
except:
    print("denominator can\'t be zero")
finally:
    print("finally block is always printed")

try:
    print(10/5)
except:
    print("denominator can\'t be zero")
finally:
    print("finally block is always printed")




