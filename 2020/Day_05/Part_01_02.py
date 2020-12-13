#initialize
import os
try:
    os.chdir('./2020/Day_05')
except:
    pass

#import seating_assignments
with open("binary_space_partitions.txt", "r") as f:
    s = f.read().splitlines()

import math as m

def seatIdGenerator(binary_space_partitions):
    #airplane parameters
    row_f = 0
    row_b = 127
    col_l = 0
    col_r = 7
    seat_assignments = {}
    i = 0
    while i < len(binary_space_partitions):
        bits = list(binary_space_partitions[i])
        curr_row_f = row_f
        curr_row_b = row_b
        curr_col_l = col_l
        curr_col_r = col_r
        b = 0
        final_row = None
        final_col = None
        while b < len(bits):
            if b == 6:
                if bits[b] == "F":
                    final_row = curr_row_f
                else:
                    final_row = curr_row_b
            elif b == len(bits) - 1:
                if bits[b] == "R":
                    final_col = curr_col_r
                else:
                    final_col = curr_col_l
            elif bits[b] == "F":
                curr_row_b = m.floor((curr_row_b + curr_row_f)/2)
            elif bits[b] == "B":
                curr_row_f = m.ceil((curr_row_b + curr_row_f)/2)
            elif bits[b] == "R":
                curr_col_l = m.ceil((curr_col_l + curr_col_r)/2)
            else:
                curr_col_r = m.floor((curr_col_l + curr_col_r)/2)
            b+=1
        #print(binary_space_partitions[i], final_row, final_col)
        seat_assignments[(final_row * 8) + final_col] = [final_row, final_col]
        i+=1
    return seat_assignments

seatIDs = seatIdGenerator(binary_space_partitions = s)

#Part 01:
print(max(k for k, v in seatIDs.items()))
#Ans. 858

#Part 02:
##Using a loop to find empty seat in ordered seat assignments
#sort dictionary by seatID, place into list
ordered_seatIDs_list = sorted(seatIDs.items())
#convert list to dictionary
ordered_seatIDs = {v[0]:v[1] for v in ordered_seatIDs_list}

#find starting and ending row/col of seat assignments
min_seatID = min(k for k, v in seatIDs.items())
max_seatID = max(k for k, v in seatIDs.items())
row_i = seatIDs[min_seatID][0]
col_i = seatIDs[min_seatID][1]
row_n = seatIDs[max_seatID][0]
col_n = seatIDs[max_seatID][1]

#find the empty seat using ordered property of seat assignment dict
empty_row = None
empty_col = None
for key, value in ordered_seatIDs.items():
    if value[0] != row_i or value[1] != col_i:
        empty_row = row_i
        empty_col = col_i
        break
    if col_i == 7:
        col_i = 0
        row_i+=1
    else:
        col_i+=1

empty_seat = {}
empty_seat[(empty_row * 8) + empty_col] = [empty_row, empty_col]
print(empty_seat)
#Ans. 557 [69, 5]

#Graphical Display
import matplotlib.pyplot as plt
import numpy as np

x_ticks = np.arange(0, max(v[0] for k, v in seatIDs.items()), 5).tolist()
#add empty seat to seat assignment dict
seatIDs.update(empty_seat)
for key, value in seatIDs.items():
   x = value[0]
   y = value[1]
   plt.scatter(x, y, color = ("r" if value[0] == empty_row and value[1] == empty_col else "b" ))
   plt.title("Find the Empty Seat")
   plt.xlabel("Seat Rows")
   plt.ylabel("Seal Columns")
   plt.xticks(x_ticks)

plt.legend(seatIDs.keys())
plt.show()