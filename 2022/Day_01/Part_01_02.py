#initialize
import os
try:
    os.chdir('./2022/Day_01')
except:
    pass

#import sea floor depth measurement values
with open("Calories.txt", "r") as f:
    p = f.read().split('\n')
calories = p

#split out calories listing by elf
elves_calories = {}
elf_counter = 1
calories_list=[]
for i in calories:
    if i == '':
        elves_calories[elf_counter] = calories_list
        elf_counter+=1
        calories_list = []
    else:
        calories_list.append(int(i))

#print(elves_calories)

#Part 01: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

#create function totalCaloriesCalculator - takes hash table of {key:elf_num, list:calories} as input
def totalCaloriesCalculator(elves_calories):
    elves_totalcalories = {}
    for key in elves_calories:
        elves_totalcalories[key] = sum(elves_calories[key])
    return elves_totalcalories

#create function maxCaloriesElf - takes hash table of {key:elf_num, int:totalcalories} as input
def maxCaloriesElf(elves_totalcalories):
    currmax_key = '0'
    currmax_elf_totalcalories = {}
    currmax_elf_totalcalories[currmax_key] = 0
    for key in elves_totalcalories:
        if elves_totalcalories[key] > currmax_elf_totalcalories[currmax_key]:
            del currmax_elf_totalcalories[currmax_key]
            currmax_elf_totalcalories[key] = elves_totalcalories[key]
            currmax_key = key
    return currmax_elf_totalcalories


print("Part #01:", maxCaloriesElf(totalCaloriesCalculator(elves_calories)))

#Ans. 67450


##Part 02: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

#create function maxCaloriesElves_N - takes hash table of {key:elf_num, int:totalcalories} & n (top N elves) as input
def maxCaloriesElves_N(elves_totalcalories, n, curr_max_dict):
    if n == 0:
        return curr_max_dict
    else:
        n-=1
        for key in maxCaloriesElf(elves_totalcalories):
            curr_max_dict[key] = maxCaloriesElf(elves_totalcalories)[key]
        reduced_elves_totalcalories = elves_totalcalories.copy()
        del reduced_elves_totalcalories[key]
        return maxCaloriesElves_N(reduced_elves_totalcalories, n, curr_max_dict)

#create function total_maxCaloriesElves_N - takes hash table of {key:elf_num, int:totalcalories} input
def total_maxCaloriesElves_N(elves_totalcalories):
    curr_total = 0
    for key in elves_totalcalories:
        curr_total+=elves_totalcalories[key]
    return curr_total


print("Part #02:",total_maxCaloriesElves_N(maxCaloriesElves_N(totalCaloriesCalculator(elves_calories),3,dict())))

