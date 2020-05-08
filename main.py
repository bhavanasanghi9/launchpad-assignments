to_do=[]
done=[]
class ToDoList:
	def __init__(self,list_name):
		self.list_name=list_name
		
		
		

	def add(self):
		self.task=input("enter the task you want to add to your list-->")
		
		to_do.append(self.task)
		print(to_do)
			


	def mark_done(self):
		self.taskdone=input("enter the task that has been completed-->")
		to_do.remove(self.taskdone)
		done.append(self.taskdone)
		print(f'you have completed--->{done} \nWAY TO GO')

	def see_tasks(self):
		print(f' \ntasks you have to finish--{to_do}')
		print(f' \ntasks you have finished--{done}')


print('WELCOME TO DO LIST MANAGER!')


while True:
	print('-'*30)
	ch=int(input("what would you like to do? \n1.create to do list \n2.add new tasks to it  \n3.mark task as done \n4.see all your tasks \n ---->"))
	if ch==1:
		list_name=input("enter the name of your to do list-->")
		
		lists=ToDoList(list_name)
		


	elif ch==2:
		
		lists.add()

	elif ch==3:
		
		lists.mark_done()

	elif ch==4:
		list_name=input("enter your list name to mark tasks as done-->")
		
		lists.see_tasks()
		
	else:
		exit