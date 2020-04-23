import pprint 
a=int(input("enter the value for row"))
b=int(input("enter the number of variables to be present in each list/column1"))
c=int(input("enter the value for column2"))
array=[[['*' for col in range(b)] for col in range(c)] for row in range(a)]
pprint.pprint(array)