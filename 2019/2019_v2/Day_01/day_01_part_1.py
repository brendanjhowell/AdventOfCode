
fuel_modules = open("fuel_modules.txt", "r")
p = fuel_modules.read().splitlines()

i = 0
t = 0
while i < len(p):
    t+=(int(p[i])//3)-2
    i+=1
print(t)