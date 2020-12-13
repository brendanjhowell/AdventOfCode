#initialize
import os
try:
    os.chdir('./2020/Day_06')
except:
    pass

#import seating_assignments
with open("customs_declaration_forms.txt", "r") as f:
    question_responses = [l.split() for l in f.read().split('\n\n')]

#Part 01:
response_count = 0
i = 0
while i < len(question_responses):
    response_count+=len(set(''.join(map(str,question_responses[i]))))
    i+=1
print(response_count)
#Ans. 6587

#Part 02:
response_count = 0
def intersection(lst1, lst2): 
    return list(set(lst1) & set(lst2))

i = 0
while i < len(question_responses):
    j = 1
    result = question_responses[i][0]
    while j < len(question_responses[i]):
        result = intersection(result, question_responses[i][j])
        j+=1
    response_count+=len(set(result))
    i+=1
print(response_count)
#Ans. 3235