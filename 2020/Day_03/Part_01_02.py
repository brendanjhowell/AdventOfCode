#initialize
import os
try:
    os.chdir('./2020/Day_03')
except:
    pass

#import geology map
with open("geology_map.txt", "r") as f:
    m = f.read().splitlines()

#create iterable pine tree map
pine_tree_map = []
i = 0
while i < len(m):
    pine_tree_map.append(list(m[i]))
    i+=1

#create traversing rules dictionary
traverse_dict = {} # **[rightward travel, downward travel]**
traverse_dict["A"] = [1, 1]
traverse_dict["B"] = [3, 1] #Rule set for Part 01
traverse_dict["C"] = [5, 1]
traverse_dict["D"] = [7, 1]
traverse_dict["E"] = [1, 2]

def slopeTraversingTreeCounter(pine_tree_map, trav_rules_dict):
    #coordinates along pine tree map
    i = 1 #Global across rule sets
    j = {} #Unique j for each rule set
    tree_counter = {}
    for key in trav_rules_dict:
        j[key] = 0
        tree_counter[key] = 0

    while i + 1 <= len(pine_tree_map): # (We say i + 1 because we always want to look down one row from where we are to determine if we can keep traversing.)
        for key, val in trav_rules_dict.items():
            if i % val[1] == 0: # (Since we want to traverse every row [i], we may not need to check for trees if the rules tell us to nagivate down more than one row at a time.)
                j[key] = (j[key] + val[0]) % len(pine_tree_map[i])
                if pine_tree_map[i][j[key]] == "#":
                    tree_counter[key] += 1
        i+=1
    return tree_counter

tree_counts = slopeTraversingTreeCounter(pine_tree_map = pine_tree_map, trav_rules_dict = traverse_dict)

#Part 01:
print(tree_counts["B"]) # Rule set B aligns with the traversing path as noted above.
#Ans. 216

#Part 02:
tree_count_prod = 1
for key, val in tree_counts.items():
    tree_count_prod*=val
print(tree_count_prod)
#Ans. 6708199680