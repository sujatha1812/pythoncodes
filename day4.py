#list create,add,delete#

a=[1,2,'a',12.2]
a.append(10)
a.remove('a')
print(a)

#store a largest value to a  variable#

number = [3, 2, 8, 5, 10, 34]
largest_number = max(number);

print(largest_number)

#store a smallest value to a variable#

number = [3, 2, 8, 5, 10, 34]
smallest_number = min(number);

print(smallest_number)

#create tuple and rev it#

s=(1,2,3,'wild',23.4)
d=tuple(reversed(s))
print(d)

#create tuple and convert tuple into list#

s=(1,2,3,'wild',23.4)
d=list(s)
print(d)
