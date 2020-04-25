no_of_lines =int(input("enter the number of lines you want to enter")) 
ini_str= ""
for i in range(no_of_lines):
    ini_str+=input()+"\n"

res_str=""
print(ini_str)


res_pos=[i for i, e in enumerate(ini_str+'A') if e.isupper()]
print(res_pos)
res_list=[ini_str[res_pos[j]:res_pos[j+1]] for j in range(len(res_pos)-1)]
print(res_list)
for i in range(len(res_list)):
	res_str+=res_list[i]+' '

print(res_str)
