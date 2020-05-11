num_list=[]
"""let the number of elements of the list be n"""

n=int(input("enter the number of elements in the list"))
"""ele represents each element in the list that we are going to input"""
for i in range (0,n):
	ele=int(input("enter the elements of the list"))
	num_list.append(ele)
"""printing out the given list in descending order"""
num_list.sort()

"""this input function will accept the value of n for nth lowest number"""
nth_lowest=int(input("enter the value of n to find the nth lowest number"))
if nth_lowest>len(num_list):
	print("there is an error")
else:

	for j in num_list:
		print(f"the {nth_lowest}th lowest number is {num_list[nth_lowest-1]}")
		break
"""j being each element iterating in num_list"""
