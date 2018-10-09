# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed datatypes like integers, floating point and string
my_list = [1, "Hello", 3.4]

#indexing

my_list = ['p','r','o','b','e']

print(my_list[0])
# Output: p

print(my_list[2])
#Output: o

print(my_list[4])
# Output: e

#Negative indexing
my_list = ['p','r','o','b','e']

print(my_list[-1])
# Output: e

print(my_list[-5])
# Output: p

#slicing lists
my_list = ['p','r','o','g','r','a','m','a','r']

# elements 3rd to 5th
print(my_list[2:5])
#output: o g r a

# elements beginning to 4th
print(my_list[:-5])
#output: p r o

# elements 6th to end
print(my_list[5:])
#output: m a r

# elements beginning to end
print(my_list[:])
#output: p r o g r a m a r

#apend
odd = [1, 3, 5]
odd.append(7)
print(odd)
# Output: [1, 3, 5, 7]


odd.extend([9, 11, 13])
print(odd)
# Output: [1, 3, 5, 7, 9, 11, 13]

#pop
# programming language list
language = ['Python', 'Java', 'C++', 'C#', 'C']

# Return value from pop()
# When 3 is passed
return_value = language.pop(3)
print('Return Value')

#output 'Python', 'Java', 'C++', 'C'

#sort
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort()

# print vowels
print('Sorted list:', vowels)

#output Sorted list: ['a', 'e', 'i', 'o', 'u']

#Reverse a list
# Operating System List
os = ['Windows', 'macOS', 'Linux']
print('Original List:', os)

# List Reverse
os.reverse()

# updated list
print('Updated List:', os)

#out put:
#Original List: ['Windows', 'macOS', 'Linux']
#Updated List: ['Linux', 'macOS', 'Windows']

