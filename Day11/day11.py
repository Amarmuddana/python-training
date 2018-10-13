# how to create a set
# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

#output
1,2,3
1.0, Hello (1,2,3)

#How to change a set in Python
my_set = {1,3}
print(my_set)

#add
my_set.add(2)
print(my_set)

#update
my_set.update([2,3,4])
print(my_set)

my_set.update([4,5], {1,6,7})
print(my_set)

#output
{1, 3}
{1, 2, 3}
{1, 2, 3, 4}
{1, 2, 3, 4, 5, 6, 7}


#booleans in python
#How bool() works


test = []
print(test,'is',bool(test))

test = [0]
print(test,'is',bool(test))

test = 0.0
print(test,'is',bool(test))

test = None
print(test,'is',bool(test))

test = True
print(test,'is',bool(test))

test = 'Easy string'
print(test,'is',bool(test))

# Outpout
[] is False
[0] is True
0.0 is False
None is False
True is True
Easy string is True
