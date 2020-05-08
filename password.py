username=input("enter your username to register-->")
password=input("enter your password to register-->")
u,l,n,s=0,0,0,0
while True:
	password=input("enter your password to register-->")
	if(len(password)>=8 and len(password)<16):
		for char in password:
			if (char.islower()):
				l+=1
			elif (char.isupper()):
				u+=1
			elif (char.isdigit()):
				n+=1
			elif(char=='$' or char=='#' or char=="@"):
				s+=1

	if(1>=1 and u>=1 and n>=1 and s>=1):
		if(l+u+n+s==len(password)):
			print("it is a valid password!")
	else:
		print("invalid password")
	