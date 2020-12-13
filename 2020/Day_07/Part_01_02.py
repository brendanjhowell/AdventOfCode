#initialize
import os
try:
    os.chdir('./2020/Day_07')
except:
    pass

#import seating_assignments
with open("luggage_rules_example.txt", "r") as f:
    r = f.read().splitlines()

bags_dict = {}

i = 0
while i < len(r):
    bag_rule_id = ' '.join(r[i].split(" ")[:2])
    bag_rule_contains = ' '.join(r[i].split(" ")[4:])
    brc_cut = ''.join(' '.join(i for i in bag_rule_contains.split(" ") if i not in ["bag.", "bags.", "bag,", "bags,"]).split(", ")).split(" ")
    
    n = 3
    brc_list = [brc_cut[i * n:(i + 1) * n] for i in range((len(brc_cut) + n - 1) // n )]
    j = 0
    bag_contents = []
    while j < len(brc_list):
        if ' '.join(brc_list[j]) == "no other":
            bag_contents.append("None")
        else:
            bag_contents.append([brc_list[j][0], ' '.join(brc_list[j][1:])])
        j+=1
    
    bags_dict[bag_rule_id] = bag_contents

    i+=1

print(bags_dict)

#Part 01:
##How many bag colors can eventually contain at least one bag of desired color?
def containedBagTypeCounter(bag_rules, desired_bag_type, all_level_bags):
    for key, val in bag_rules.items():
        i = 0
        while i < len(val):
            if val[i][1] == desired_bag_type:
                if key not in all_level_bags:
                    all_level_bags.append(key)
                    containedBagTypeCounter(bag_rules = bag_rules, desired_bag_type = key, all_level_bags = all_level_bags)
            i+=1
    return len(all_level_bags)

bag_type = "shiny gold"
##print(containedBagTypeCounter(bag_rules = bags_dict, desired_bag_type = bag_type, all_level_bags = []))
#Ans. 302

#Part 02:
##How many individual bags are required inside your bag of desired color?
def totalBagsWithinDesiredBag(bag_rules, desired_bag_type, bag_count, next_bag_multiplier):
    for key, val in bag_rules.items():
        if key == desired_bag_type:
            print(val, "arriving", next_bag_multiplier)
            i = 0
            while i < len(val):
                if val[i] != "None":
                    print("before:", val[i][1], val[i][0], bag_count, next_bag_multiplier)
                    bag_count+=int(val[i][0])*next_bag_multiplier
                    next_bag_multiplier = int(val[i][0])
                    print("after:", val[i][1], val[i][0], bag_count, next_bag_multiplier)
                    totalBagsWithinDesiredBag(bag_rules = bag_rules, desired_bag_type = val[i][1], bag_count = bag_count, next_bag_multiplier = next_bag_multiplier)
                else:
                    next_bag_multiplier = 200
                    print("empty bag")
                i+=1
            print(val, "leaving", next_bag_multiplier)
    return bag_count

bag_type = "shiny gold"
print(totalBagsWithinDesiredBag(bag_rules = bags_dict, desired_bag_type = bag_type, bag_count = 0, next_bag_multiplier = 1))
#Ans.