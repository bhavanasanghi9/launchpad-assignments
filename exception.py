def divide(x,y):
	ans=x/y
	print(ans)

while True:
	try:
		a=int(input("enter the dividend"))
		b=int(input("enter the divisor"))
		divide(a,b)
	except ZeroDivisionError:
		print("divison by zero!")
	
