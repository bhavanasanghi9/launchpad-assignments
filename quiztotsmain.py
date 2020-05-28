from puruquiz1 import Teacher , Student

while True:
	

	print('-'*30)
	print("welcome to Quizapp")
	ch=int(input("1.add_questions\n2.take quiz\n3.check class result \n-->"))
	
	if ch==1:
		"""takes teacher's name, the questions added , the options to be displayed and correct option and appends to list quizapp[]"""
		"""these are lists inside lists , looks like a matrix"""
		options = []
		corr_ans = []
		question = []
		name = input("Enter your name \n-->")
		n=int(input("enter the number of questions you want to add \n-->"))
		for i in range(n):
			question.append(input(f"enter question {i+1} \n-->"))
			options.append(input("enter 4 options for the questions seperated by commas \n-->").split(","))
			corr_ans.append(input("enter the correct option for the question \noptions being a,b,c,d. Enter any one.\n-->"))
		Teacher.quizapp.append(Teacher(name,question,options,corr_ans))



	elif ch==2:
		if not Teacher.quizapp:
			print("No quizes added yet, please check later") 
		else:		
			score = []
			print("-"*30)
			print("welcome to Quizapp!")
			"""name of student = name"""
			name=input("enter your name before you take the quiz \n-->")
			print("The following teachers have uploaded their quiz. which quiz would you like to take: ")
			"""displays the names of teachers who have created a quiz"""
			for i in Teacher.quizapp:
				print(i.teacher_name)
			teach = input().strip()
			"""iterates the list quizapp[] to see if student has entered correct name of teacher"""
			for obj in Teacher.quizapp:
				if obj.teacher_name == teach:
					for i in range(len(obj.question)):
						
						Teacher.question_answer(obj,i)
						
						ans = input("Enter your option: ").strip().lower()
						"""for every correct ans , 1 is appended to list score[]"""
						score.append(Teacher.correct_ans(ans,i,obj))											
			Student.quizer.append(Student(name,sum(score)))
			print(f"You scored: {sum(score)}")



	elif ch==3:
		Student.tot_marks()
		
	
	else:
		break
