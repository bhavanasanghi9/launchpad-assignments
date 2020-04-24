record={}
n_st=int(input("enter the number of students you want to include in the record"))
for n in range(n_st):
	students,*marks=input("enter the student name and all their marks").split()
	marks=list(map(int,marks))
	record[students]=marks
	

user_input = ''

while user_input !='exit':
	try:
		user_input=input("enter the name of student and the name of the subject to get his score")
	
	


	
		name,subject=user_input.split()
		for students,marks in record.items():
			if students==name:
				if subject=='math':
					print(f"student {name} scored {record[students][0]} in math")
				
				elif subject=='physics':
					print(f"student {name} scored {record[students][1]} in physics")
				
				elif subject=='chemistry':
					print(f"student {name} scored {record[students][2]} in chemistry")
				
				elif subject=='biology':
					print(f"student {name} Scored {record[students][3]} in biology")
				
				elif subject=='social-science':
					print(f"student {name} Scored {record[students][4]} in social-science")
				break
	except:
		print('disable')