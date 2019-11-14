import sys

before=input()
after=input()

#remvove matching items at the BEGINNING of the strings
while(len(after)>0 and len(before)>0 and before[0] == after[0]):
    after=after[1:]
    before=before[1:]
 
#remove matching items atht the END of the strings
while(len(after)>0 and len(before)>0 and before[-1] == after[-1]):
    after=after[:-1]
    before=before[:-1]
    
print(len(after))