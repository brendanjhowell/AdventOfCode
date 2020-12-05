#Initialize
import os
try:
    os.chdir('./2020/Day_02')
except:
    pass

#import expense report values
with open("passwords.txt", "r") as f:
    p = f.read().splitlines()

def passwordValidityCounter(company, passwords):
    #Part 01: Find count of valid passwords. (Sled Rental Company - Shopkeeper's Last Employer)
    if company == "sled":
        valid_count = 0
        i = 0
        while i < len(passwords):
            s = passwords[i].split(" ")
            #count of letter
            min_amt = int(s[0].split("-")[0])
            max_amt = int(s[0].split("-")[1])

            #letter of scope
            letter = list(s[1])[0]

            #check count of letter of scope in password for validity
            split_pass = list(s[2])
            if split_pass.count(letter) >= min_amt and split_pass.count(letter) <= max_amt:
                valid_count+=1

            i+=1

    #Part 02: Find count of valid passwords. (Official Toboggan Corporate Authentication System)
    elif company == "toboggan":
        valid_count = 0
        i = 0
        while i < len(passwords):
            s = passwords[i].split(" ")
            #positions A and B of letter (we subtract one to properly index at zero)
            pos_A = int(s[0].split("-")[0]) - 1
            pos_B = int(s[0].split("-")[1]) - 1

            #letter of scope
            letter = list(s[1])[0]

            #check positions of letter of scope in password for validity
            pos_match_count = 0 #used to count presence of letter in positions A and B - if equal to 1, OR(pos_A, pos_B) applies [not "AND"], giving us valid password.
            split_pass = list(s[2])
            if split_pass[pos_A] == letter:
                pos_match_count += 1
            if split_pass[pos_B] == letter:
                pos_match_count += 1
            if pos_match_count == 1:
                valid_count+=1
            i+=1
    return valid_count

#Part 01:
print(passwordValidityCounter(company = "sled", passwords = p))
#Ans. 515

#Part 02:
print(passwordValidityCounter(company = "toboggan", passwords = p))
#Ans. 711