gravity_assist_program = open("C:/Users/brend/Downloads/Advent of Code/2019/Day_02/gravity_assist_program.txt", "r")

p_str = gravity_assist_program.read().split(",")
p = [int(x) for x in p_str]

#Replacements
p[1] = 12
p[2] = 2

chunk = 0 #iterates by 4
while chunk < len(p):
    if p[chunk] == 1:
        v = p[p[chunk+1]]+p[p[chunk+2]]
        p[p[chunk+3]] = v
    elif p[chunk] == 2:
        v = p[p[chunk+1]]*p[p[chunk+2]]
        p[p[chunk+3]] = v
    elif p[chunk] == 99:
        break
    else:
        break
    chunk+=4
print(p[0])
