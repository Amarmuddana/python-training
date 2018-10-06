Index and Slice Strings in Python
#Example 1
>>> a = "String"
>>> a[0]
output: 'S'
>>> a[1]
output:'t'
>>> a[2]
output:'r'
>>> a[3]
output:'i'
>>> a[4]
output:'n'
>>> a[5]
output:'g'
#Example2
>>> a = "String"
>>> a[-1]
output:'g'
>>> a[-2]
output:'n'
>>> a[-3]
output:'i'
>>> a[-4]
output:'r'
>>> a[-5]
output:'t'
>>> a[-6]
output:'S'

#Example3
Python program that slices list
values = [100, 200, 300, 400, 500]
# Get elements from second index to third index.
slice = values[1:3]
print(slice)

Output
[200, 300]

#Example4
Python program that slices, negative second index
values = [100, 200, 300, 400, 500]
# Slice from third index to index one from last.
slice = values[2:-1]
print(slice)

Output
[300, 400]

#Example5
Python program that slices, starts and ends
values = [100, 200, 300, 400, 500]
# Slice from start to second index.
slice = values[:2]
print(slice)
# Slice from second index to end.
slice = values[2:]
print(slice)

Output
[100, 200]
[300, 400, 500]

