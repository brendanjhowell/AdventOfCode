
fuel_modules = open("C:/Users/brend/Downloads/Advent of Code/2019/Day_01/fuel_modules.txt", "r")
p = fuel_modules.read().splitlines()

i = 0
t = 0
while i < len(p):
    t+=(int(p[i])//3)-2
    i+=1
print(t)
