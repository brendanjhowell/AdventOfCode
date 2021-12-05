#initialize
import os
try:
    os.chdir('./2021/Day_01')
except:
    pass

#import sea floor depth measurement values
with open("sonar_sweep_report.txt", "r") as f:
    p = f.read().split()
sea_floor_depth = list(map(int, p))

#print(sea_floor_depth)

#Part 01: Count the number of times a depth measurement increases from the previous measurement.

#create function measurementIncreaseTracker
def measurementIncreaseTracker(sea_floor_depth):
    i = 1
    prev = sea_floor_depth[0]
    measure_increase_count = 0
    while i < len(sea_floor_depth):
        if sea_floor_depth[i] > prev:
            measure_increase_count+=1
        prev = sea_floor_depth[i]
        i+=1
    return measure_increase_count

print("Part #01:", measurementIncreaseTracker(sea_floor_depth))
#Ans. 1581


##Part 02: Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

def measurementIncreaseTracker_SlidingSums(sea_floor_depth):
    i = 0
    prev = sum(sea_floor_depth[i:i+3])
    i+=1
    measure_increase_count = 0
    while i < len(sea_floor_depth):
        if sum(sea_floor_depth[i:i+3]) > prev:
            measure_increase_count+=1
        prev = sum(sea_floor_depth[i:i+3])
        i+=1
    return measure_increase_count

print("Part #02:", measurementIncreaseTracker_SlidingSums(sea_floor_depth))
#Ans. 1618
