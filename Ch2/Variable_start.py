#
# Example File for variables
#

# Declare a variable and initialize it
f=0
print (f)

#Re-declaring the variable works
f="abc"
print(f)

#Error: variables of different types cannot be combined. to combine a string and a number use the function called str for number 
# to convert to string
print("string" + str(123))

# Global vs local Variables in functions
def somefunction():
# global will get even update the variable (with the same name) which is outside the function
    global f
    f="def"
    print(f)

somefunction()
print(f)

# del is used to unassing a value to a variable
del f
print(f)