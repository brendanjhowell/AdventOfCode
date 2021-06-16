#initialize
import os
try:
    os.chdir('./2020/Day_08')
except:
    pass

#import seating_assignments
with open("handheld_game_console_boot_code_example.txt", "r") as f:
    b = f.read().splitlines()

print(b)