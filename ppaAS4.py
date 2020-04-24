n=int(input("type how many names you want to enter"))

for i in range(n):
	input_string=input("enter your name")
	first,last=input_string.split(' ')
	newfirst=""
	for char in first:
		if char.isalpha():
			newfirst += char

	newlast=""
	for char in last:
		if char.isalpha():
			newlast += char 	
	print(newfirst+" "+newlast)