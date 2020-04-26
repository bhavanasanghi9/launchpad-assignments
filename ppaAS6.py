record={}
n_st=int(input("enter the number of students you want to include in the record"))
for n in range(n_st):
	students,*marks=input("enter the student name and all their marks").split()
	marks=list(map(int,marks))
	record[students]=marks

	
math=[]
physics=[]
chemistry=[]
biology=[]
socialscience=[]

subjectname=input("enter the subject name to see the marks of all the students")
for students,marks in record.items():
	if subjectname=='math':
		math.append((record[students][0],students))
		math=sorted(math,reverse=True)
	
	elif subjectname=='physics':
		physics.append((record[students][1],students))
		physics=sorted(physics,reverse=True)
	elif subjectname=='chemistry':
		chemistry.append((record[students][2],students))
		chemistry=sorted(chemistry,reverse=True)
	elif subjectname=='biology':
		biology.append((record[students][3],students))
		biology=sorted(biology,reverse=True)
	elif subjectname=='social-science':
		socialscience.append((record[students][4],students))
		socialscience=sorted(socialscience,reverse=True)


for i,j in math:
	print(j, " got ",i)
for a,b in physics:
	print(b, " got ",a)
for x,y in chemistry:
	print(y,' got ',x)
for c,d in biology:
	print(d,' got ',c)
for n,m in socialscience:
	print(m,' got ',n)