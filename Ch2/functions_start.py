#
# Example file for working with functions
#
import math
# define a basic function
def func1():
    print("I am a function")

#function that takes arguements
def func2(arg1, arg2):
    print(arg1, " ", arg2)

#function that returns value
def cube(x):
    return (x*x*x)

#function with defautl value for arguements - this function is to print the power of number if x is 3 it will print cube of num
def power(num, x=4):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable numbers of arguments
def multi_add(*y):
    result = 0
    for x in y:
        result = result + x
    return result



#to call the function
func1()
#call the function and also print again
print (func1())
#if did not give any brackets it will give an error,
#even for functions which dont take arguments
print (func1)

#function with arguements. While calling need to give arguements
func2(10, 20)
print(func2(10, 20))

#function with a return value
print (cube(3))

#Function with a defualt value for arguements
print (power(3))
#changing the x value from the actual function
print (power(2,3))
#reversing the variables mentioned in the function
print (power(x=3, num=2))

# function with variable number of arguements
print (multi_add(1,1,1,1,1,1,1,1,1,1,1,1,1,1))