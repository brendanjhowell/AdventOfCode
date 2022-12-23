
fuel_modules = open("fuel_modules.txt", "r")
p = fuel_modules.read().splitlines()

def FuelModuleSum(p):
    t = 0
    i = 0
    while i < len(p):
        v0 = int(p[i])
        v = (v0//3)-2
        while v > 0:
            t+=v
            v=(v//3)-2
        i+=1
    print(t)

FuelModuleSum(p)
