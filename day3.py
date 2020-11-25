#merge two dictionaries#

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d=d1.copy()
d.update(d2)
print(d)

#remove key from dictionaries#

myDict = {'a':1,'b':2,'c':3,'d':4}
if 'b' in myDict: 
    del myDict['b']
print(myDict)

#map two list in dictionary#

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))
print(color_dictionary)

#find length of set#

CSK={"dhoni","bravo","jadeja"}
print(len(CSK))

#remove intersection 2nd set from 1st set#

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:")
print(sn1-sn2)


