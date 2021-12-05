#initialize
import os
try:
    os.chdir('./2021/Day_02')
except:
    pass

#import sea floor depth measurement values
with open("planned_course.txt", "r") as f:
    p = f.read().splitlines()
planned_course = p

#Part 01: Calculate the horizontal position and depth you would have after following the planned course.
#What do you get if you multiply your final horizontal position by your final depth?

#create function horizontalPositionFinder
def horizontalPositionFinder(planned_course):
    #initialize beginning position: {x,y,x} ~> {0,0,0}
    curr_position = {'forward': 0, 'up': 0, 'down': 0}
    i = 0
    while i < len(planned_course):
        course_instruction = planned_course[i].split()
        curr_position[course_instruction[0]]+=int(course_instruction[1])
        i+=1
    #without "aim" we can calculate "depth" at the very end of the course instructions list
    depth = curr_position['down'] - curr_position['up']
    return curr_position['forward'] * depth

print("Part #01:", horizontalPositionFinder(planned_course))
#Ans. 2272262


##Part 02: Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course.
#What do you get if you multiply your final horizontal position by your final depth?

def horizontalPositionFinder_Aim(planned_course):
    #initialize beginning position: {x,y,x} ~> {0,0,0}
    curr_position = {'forward': ['forward',0], 'up': ['aim',0], 'down': ['aim',0], 'aim': ['aim',0]}
    #given that "aim" is being considered here, we must calculate depth after completing each course instruction
    depth = 0
    i = 0
    while i < len(planned_course):
        course_instruction = planned_course[i].split()
        if course_instruction[0] =='up':
            curr_position[curr_position[course_instruction[0]][0]][1]-=int(course_instruction[1])
        elif course_instruction[0] in ['down','forward']:
            curr_position[curr_position[course_instruction[0]][0]][1]+=int(course_instruction[1])
        #update depth calculation
        if course_instruction[0] == 'forward':
            depth+=(int(course_instruction[1]) * curr_position['aim'][1])
        i+=1
    
    return curr_position['forward'][1] * depth

print("Part #02:", horizontalPositionFinder_Aim(planned_course))
#Ans. 2134882034