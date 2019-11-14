import sys

input=sys.stdin.readline().strip('\n').split(' ')
width=input[0]
split_count=[1]

splits=[0]
toAdd=sys.stdin.readline().strip('\n').split(' ')

for i in toAdd:
	splits.append(int(i))

splits.append(int(width))

def split(list, answers):

	if len(list)==0:
		s=sorted(answers)	
		print(*s, sep=' ')	
		return None		

	reference=list[0]
	list.remove(reference)
	for i in list:
		answers.add(i - reference)
	split(list, answers)

split( splits, set() )





