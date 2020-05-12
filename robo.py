x=0
y=0
def robot(robo_tuple):
	global x
	global y
	
	if robo_tuple[0]=='UP':
		y+=int(robo_tuple[1])
	elif robo_tuple[0]=='DOWN':
		y-=int(robo_tuple[1])
	elif robo_tuple[0]=='RIGHT':
		x+=int(robo_tuple[1])
	elif robo_tuple[0]=='LEFT':
		x-=int(robo_tuple[1])




print('WELCOME TO ROBOT TRACKER!')
print('-'*30)
"""to enter the movements of the robot and store it in a variable"""


"""here we store the movements of the robot in a list and convert it into the tuple and then call the funtion 'robot'"""
robo_list1=input("enter the movements of the robot :").split()
robo_tuple1=tuple(robo_list1)
robot(robo_tuple1)
print(robo_tuple1)


robo_list2=input("enter the movements of the robot :").split()
robo_tuple2=tuple(robo_list2)
robot(robo_tuple2)
print(robo_tuple2)


robo_list3=input("enter the movements of the robot :").split()
robo_tuple3=tuple(robo_list3)
robot(robo_tuple3)
print(robo_tuple3)

robo_list4=input("enter the movements of the robot :").split()
robo_tuple4=tuple(robo_list4)
robot(robo_tuple4)
print(robo_tuple4)
print('-'*30)
print(f"the new position of the turtle is {x,y}")

print("let's track the distance of the robot from the initial point!")
dist=(((x-0)**2)+((y-0)**2))**0.5
print(f"the total distance travelled by the robot is {round(dist)}")



