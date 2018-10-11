# Tuple
tup1 = ('physics', 'chemistry', 1000, 2000);
tup2 = (1, 2, 3, 4, 5, 6, 7 );
print "tup1[0]: ", tup1[0];
print "tup2[1:5]: ", tup2[1:5];

#output
tup1[0]:  physics
tup2[1:5]:  [2, 3, 4, 5]

#Adding tuples
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print tup3;

#output
(12, 34.56, 'abc', 'xyz')

#Delete Tuple Elements
tup = ('physics', 'chemistry', 1000, 2000);
print tup;
del tup;

#output
('physics', 'chemistry', 1000, 2000)