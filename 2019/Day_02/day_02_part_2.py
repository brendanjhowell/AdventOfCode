gravity_assist_program = open("gravity_assist_program.txt", "r")

p_str = gravity_assist_program.read().split(",")
p = [int(x) for x in p_str]

#Goal
g = 19690720

#Replacements
#p[1] = 12
#p[2] = 2

def intcodeProgram(p):
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
    return p[0]

def outputFind(p, g):
    noun = 0
    verb = 0
    v = 0
    while v <= g:
        p_ref = [int(x) for x in p_str]
        p_ref[1] = noun
        p_ref[2] = verb
        #print(noun)
        v = intcodeProgram(p_ref)
        #print(v)
        noun+=1
    #Backtrack Adjustment
    noun-=2
    v = 0
    while v <= g:
        p_ref = [int(x) for x in p_str]
        p_ref[1] = noun
        p_ref[2] = verb
        v = intcodeProgram(p_ref)
        verb+=1

    #Backtrack Adjustment
    verb-=2

    return 100*noun + verb

print(outputFind(p, g))
