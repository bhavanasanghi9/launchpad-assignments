num=[1, 1, 2, 3, 4, 64, 35, 93, 35, 87, 4, 3]
new_list=[]
for i in num:
	if i not in new_list:
		new_list.append(i)
	print(new_list)
