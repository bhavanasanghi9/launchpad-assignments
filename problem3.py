num=[1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
ele=int(input("enter element from list"))
ind=[]
for i in range(len(num)):
	if num[i]==ele:
		ind.append(i)
	print(ind)
	