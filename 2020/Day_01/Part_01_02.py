
#Initialize

#import expense report values
expense_report = open("C:/Users/brend/Documents/Github/AdventOfCode/2020/Day_01/expense_report.txt", "r")
p = expense_report.read().splitlines()
p_int = list(map(int, p))

#sort expense report values
expenses = sorted(p_int)

#Part 01: Find 2 numbers which add up to goal sum, calculate product of two numbers.
goal_sum = 2020

#create function expenseFinderDuo
def expenseFinderDuo(expenses, goal_sum):
    goal_seek = True
    i = 0
    while i < len(expenses) and goal_seek:
        j = i + 1
        rem = goal_sum - expenses[i]
        while j < len(expenses) and goal_seek:
            if expenses[j] == rem:
                goal_seek = True
                #print(expenses[i], expenses[j])
                return expenses[i] * expenses[j]
            elif rem < expenses[j]:
                break
            j+=1
        i+=1

print("Part #01:", expenseFinderDuo(expenses, goal_sum))
#Ans. 802011 (543, 1477)


##Part 02: Find 3 numbers which add up to goal sum, calculate product of 3 numbers.

def expenseFinderTriple(expenses, goal_sum):
    expenses_dict = {i: expenses[i] for i in range(0, len(expenses),1)}
    goal_seek = True
    i = 0
    while i < len(expenses) and goal_seek:
        j = i + 1
        rem = goal_sum - expenses[i]
        while j < len(expenses) and goal_seek:
            search_val = rem - expenses[j]
            if search_val < 1:
                break
            else:
                for key, val in expenses_dict.items():
                    if search_val == val and key not in (i, j):
                        #print(expenses[i], expenses[j], val)
                        goal_seek = False
                        return expenses[i] * expenses[j] * val
            j+=1
        i+=1

print("Part #02:", expenseFinderTriple(expenses, goal_sum))
#Ans. 248607374 (422, 577, 1021)
