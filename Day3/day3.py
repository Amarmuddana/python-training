#undrestanding about variables 
#Assining x to be an integer
x = 76
print(x)

#Reassining x to be a string
x = "Sammy"
print(x)

#Creating a global variable, outside of a function
glb_var = "global"

#Defining a function
def var_function():
    lcl_var = "local" #Create a local variable, inside function
    print(lcl_var)

#Calling function to print local variable
var_function()

#Printing global variable outside function
print(glb_var)