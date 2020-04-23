mydict = {"hello" : "world", "speckbit" : "self-learning", "life" : "meaning"}
mysample=input("enter the string you would want the key value for")
for key, value in mydict.items():
	if value==mysample:
		print(key)