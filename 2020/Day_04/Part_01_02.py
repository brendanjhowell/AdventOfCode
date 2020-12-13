#initialize
import os
try:
    os.chdir('./2020/Day_04')
except:
    pass

#import passports
with open("passports.txt", "r") as f:
    p = f.read().splitlines()

#data parsing to get passports in correct format
##fields displayed across lines in chunks with no blank lines between them make up one passport. passports are split by blank line boundaries.
passports = []
i = 1
hold = p[0]
while i < len(p):
    if p[i] != "":
        hold = hold + " " + p[i]
    else: # (We've encountered a blank line. everything contained within "hold" up to this point comprises one passport, and we want to save this passport off in "passports" and begin to populate "hold" with contents from the line following our current blank line.)
        passports.append(hold)
        hold = p[i+1]
        i+=1
    i+=1
    if i == len(p):
        passports.append(hold)

def validPassportCounter(passports, data_validation_flag):
    #check for whether data validation is required (Part 2) or not (Part 1)
    if not data_validation_flag:
        #initialize valid passport counter
        valid_counter = 0
        i = 0
        while i < len(passports):
            by_item = passports[i].split(" ")
            if len(by_item) == 8:
                valid_flag = True
            elif len(by_item) < 7:
                valid_flag = False
            else:            
                opt_find = False
                j = 0
                while j < len(by_item):
                    if by_item[j][0:3] == "cid":
                        opt_find = True
                    j+=1
                if opt_find == True:
                    valid_flag = False
                else:
                    valid_flag = True                
            if valid_flag:
                valid_counter+=1
            i+=1
    
    else:
        #define passport structure
        passport_struct = {}
        passport_struct["byr"] = None #(Birth Year)
        passport_struct["iyr"] = None #(Issue Year)
        passport_struct["eyr"] = None #(Expiration Year)
        passport_struct["hgt"] = None #(Height)
        passport_struct["hcl"] = None #(Hair Color)
        passport_struct["ecl"] = None #(Eye Color)
        passport_struct["pid"] = None #(Passport ID)
        passport_struct["cid"] = None #(Country ID)

        #initialize valid passport counter
        valid_counter = 0
        i = 0
        while i < len(passports):
            by_item = passports[i].split(" ")
            j = 0
            while j < len(by_item):
                passport_struct[by_item[j][0:3]] = by_item[j][4:]
                j+=1

            #make checks against dictionary corresponding to each passport we have
            valid_passport = True
            for key, val in passport_struct.items():
                ##missing field checks
                if key != "cid" and val is None:
                    valid_passport = False
                else:
                    ##data validation checks
                    #birth year
                    if key == "byr":
                        if int(val) < 1920 or int(val) > 2002:
                            valid_passport = False

                    #issue year
                    if key == "iyr":
                        if int(val) < 2010 or int(val) > 2020:
                            valid_passport = False

                    #expiration year
                    if key == "eyr":
                        if int(val) < 2020 or int(val) > 2030:
                            valid_passport = False

                    #height
                    if key == "hgt":
                        if val[-2:] not in ["in", "cm"]:
                            valid_passport = False 
                        else:
                            if val[-2:] == "in":
                                if int(val[:len(val) - 2]) < 59 or int(val[:len(val) - 2]) > 76:
                                    valid_passport = False       
                            else:
                                if int(val[:len(val) - 2]) < 150 or int(val[:len(val) - 2]) > 193:
                                    valid_passport = False
                                    
                    #hair color
                    if key == "hcl":
                        hair_code = list(val)
                        if len(hair_code) != 7:
                            valid_passport = False                            
                        else:
                            h = 0
                            while h < len(hair_code):
                                if h == 0:
                                    if hair_code[h] != "#":
                                        valid_passport = False                                    
                                elif hair_code[h] not in ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]:
                                    valid_passport = False
                                h+=1                

                    #eye color
                    if key == "ecl":
                        if val not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                            valid_passport = False

                    #passport id
                    if key == "pid":
                        if len(val) != 9:
                            valid_passport = False
                            
                    #country id
                    if key == "cid":
                        continue # (Whether "cid" is included on a passport or not does not determine its validity.)
            
            #check for validity, tabulate with counter
            if valid_passport:
                valid_counter += 1
            passport_struct = {key: None for key in passport_struct}
            i+=1       
    
    return valid_counter

#Part 01:
print(validPassportCounter(passports=passports, data_validation_flag = False))
#Ans. 226

#Part 01:
print(validPassportCounter(passports=passports, data_validation_flag = True))
#Ans. 160