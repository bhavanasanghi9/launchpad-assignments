str=input("enter any string of choice").split()
str.sort()
print(str)
str2=[]
for i in str:
	if i not in str2:
		str2.append(i)

for i in range(0,len(str2)):
	print(f'{str2[i]} : {str.count(str2[i])}')
