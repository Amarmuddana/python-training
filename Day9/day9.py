#How to create a dictionary
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'text1', 2: 'text2'}

# dictionary with mixed keys
my_dict = {'name': 'ram', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])



#access elements from a dictionary
my_dict = {'name':'ravi', 'age': 26}
print(my_dict['name'])
print(my_dict.get('age'))

output:
ravi 26



#change or add elements in a dictionary
my_dict = {'name':'ravi', 'age': 26}

# update value
my_dict['age'] = 27

# add item
my_dict['address'] = 'Downtown'  

print(my_dict)

output:
{'name': 'ravi', 'age': 27, 'address': 'Downtown'}



#Dictionary Comprehension
squares = {x: x*x for x in range(6)}
print(squares)

# Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}





#delete or remove elements from a dictionary
# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

# remove a particular item
print(squares.pop(4))  
print(squares)

# remove all items
print(squares.clear())
print(squares)

# delete the dictionary itself
print(del squares)
print(squares)

#output
16
{}