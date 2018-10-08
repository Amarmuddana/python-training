Formatters
# .formats in strings
print("ravi has {} balloons.".format(5))

string = "ravi loves {}."
print(string.format("python"))

string = "ravi loves {} {}."                      
print(string.format("open-source", "software"))

string = "ravi loves {} {}, and has {} {}."                      
print(string.format("open-source", "software", 5, "balloons"))

print("ravi the {} has a pet {}!".format("boy", " bull dog"))

print("ravi the {0} has a pet {1}!".format("boy", "bull dog"))

#f strings

name = "Ravi"
age = 24
print (f"Hello, {name} You are {age}.")

#f and using string lower case

name = "RAVI"
age = 24
print (f"{name.lower()} you are {age}.")

#f and using string Upper case

name = "ravi"
age = 24
print (f"{name.upper()} you are {age}.")