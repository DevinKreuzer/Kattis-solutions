import sys


input=sys.stdin.readline().strip('\n').split(' ')
num_coms=int(input[0])
price=int(input[1])

student_list=[] 
for i in sys.stdin.readline().strip('\n').split(' '):
	student_list.append(int(i))

max_list=[]

for i in range(len(student_list)):
	if len(max_list)==0:
		max_list.append( student_list[0] - price)
	else:
		max_list.append( max( student_list[i]-price, student_list[i]-price + max_list[i-1] ))
print(max(max_list)) 
