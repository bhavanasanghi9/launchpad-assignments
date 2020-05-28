from tabulate import tabulate 
class Teacher:
	quizapp = []
	score = []

	def __init__(self,teacher_name,question,options,correct_answer):
		
		self.teacher_name=teacher_name
		self.question=question
		self.options=options
		self.correct_answer=correct_answer

	def question_answer(obj,i):
		"""displays the questions along with its options from quizapp list"""
		
		print(obj.question[i])
		print(f"a.{obj.options[i][0]} \nb.{obj.options[i][1]} \nc.{obj.options[i][2]} \nd.{obj.options[i][3]}")

	def correct_ans(ans,i,obj):
		"""checks if the student's answer(ans) is the same as the correct answer as entered by teacher"""
		if ans == obj.correct_answer[i]:
			
			print("That was the correct answer!!")
			return 1
		else:
			
			print(f"That's the wrong answer.The correct answer is: {obj.correct_answer[i]}")
			return 0
		

class Student:
	quizer = []
	table=[]

	def __init__(self,name,total_score):
		self.total_score= total_score
		self.name=name
	
	def tot_marks():
		"""displays the marks of all the students that have taken the quiz"""
		if not Student.quizer:
			print("No results added yet. Please check in later.")
		else:
			for obj in Student.quizer:
						print(f"{obj.name}:{obj.total_score}")
				
				






