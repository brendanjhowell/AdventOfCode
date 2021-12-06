#initialize
import os
from re import I
try:
    os.chdir('./2021/Day_03')
except:
    pass

#import scipy for matrix calculations
from scipy import stats

#import sea floor depth measurement values
with open("diagnostic_report.txt", "r") as f:
    p = f.read().splitlines()
diagnostic_report_array = [[int(a) for a in str(x)] for x in p]

#Part 01: Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together.
#What is the power consumption of the submarine?

#create function binaryToDecimalConverter
def binaryToDecimalConverter(binary_num): #list input
    decimal_num = 0
    n = len(binary_num)
    i = 0
    while i < len(binary_num):
        decimal_num+=int(binary_num[i])*(2**(n-1))
        n-=1
        i+=1
    return decimal_num

#create function gammaRateCalculator
def gammaRateCalculator(diagnostic_report_array): #array input
    array = diagnostic_report_array
    #find 'mode' of diagnostic_report_array as list of bits, then flatten list of bits from scipy stats output ~> this becomes the gamma rate represented as a list of binary digits
    return [item for sublist in stats.mode(array).mode for item in sublist] #list output

#create function epsilonRateCalculator
def epsilonRateCalculator(gamma_rate): #list input of binary digits
    epsilon_rate = []
    i = 0
    while i < len(gamma_rate):
        if gamma_rate[i] == 1:
            epsilon_rate.append(0)
        else:
            epsilon_rate.append(1)
        i+=1
    return epsilon_rate #list output of binary digits

#create function powerConsumptionCalculator
def powerConsumptionCalculator(gamma_rate, epsilon_rate): #list input of binary digits for both parameters
    gamma_rate_decimal = binaryToDecimalConverter(gamma_rate)
    epsilon_rate_decimal = binaryToDecimalConverter(epsilon_rate)
    return gamma_rate_decimal * epsilon_rate_decimal #decimal output

#set parameters for gamma_rate and epsilon_rate
gamma_rate = gammaRateCalculator(diagnostic_report_array)
epsilon_rate = epsilonRateCalculator(gammaRateCalculator(diagnostic_report_array))
print("Part #01:", powerConsumptionCalculator(gamma_rate, epsilon_rate))
# Ans. 738234


##Part 02: Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together.
#What is the life support rating of the submarine?

#create function oxygenGeneratorRatingCalculator
def oxygenGeneratorRatingCalculator(bit_num, diagnostic_report_array):
    i = bit_num
    array = diagnostic_report_array
    #mode array gives us list of most common bits at each index across all binary numbers
    mode_array = [item for sublist in stats.mode(array).mode for item in sublist]
    #count array gives us list of counts of most common bit at each index across all binary numbers
    count_array = [item for sublist in stats.mode(array).count for item in sublist]
    n = len(array)
    focus_bit = mode_array[i] #this is the bit we need to focus on for a given pass-through of binary numbers noted by iterator i
    if count_array[i] == n // 2: #i.e., count of 1s and 0s is the same out of remaining binary numbers in array
        focus_bit = 1 #we know that if this edge case applies, the focus bit would've been 0 without any changes. we need to choose the higher bit here instead for the oxygen generator rating, which doesn't align with scipy's "mode" output [by default, it would provide the lower bit].
    filtered_array = []
    j = 0
    while j < len(array):
        if array[j][i] == focus_bit:
            filtered_array.append(array[j])
        j+=1
    i+=1
    #base case ~> we only have one binary number left in our array after filtering
    if len(filtered_array) == 1:
        return filtered_array[0]
    #recurvise case ~> we haven't yet filtered to one binary number and must continue traversing our mode array
    else:
        return oxygenGeneratorRatingCalculator(i, filtered_array)

#create function co2ScrubberRating
def co2ScrubberRatingCalculator(bit_num, diagnostic_report_array):
    i = bit_num
    array = diagnostic_report_array
    #mode array gives us list of most common bits at each index across all binary numbers
    mode_array = [item for sublist in stats.mode(array).mode for item in sublist]
    #count array gives us list of counts of most common bit at each index across all binary numbers
    count_array = [item for sublist in stats.mode(array).count for item in sublist]
    #flipping the mode array gives us list of the least common bits at each index across all binary numbers
    flipped_mode_array = [1 if f == 0 else 0 for f in mode_array]
    n = len(array)
    focus_bit = flipped_mode_array[i] #this is the bit we need to focus on for a given pass-through of binary numbers noted by iterator i
    if count_array[i] == n // 2: #i.e., count of 1s and 0s is the same out of remaining binary numbers in array
        focus_bit = 0 #if this edge case applies, we're looking at the result of a flipped array where a "mode" of 0 became 1 at a given index of mode_array. for c02 rating, we need to revert to the "mode" of 0, as we opt to choose the lower bit value instead.
    filtered_array = []
    j = 0
    while j < len(array):
        if array[j][i] == focus_bit:
            filtered_array.append(array[j])
        j+=1
    i+=1
    #base case - we only have one binary number left in our array after filtering
    if len(filtered_array) == 1:
        return filtered_array[0]
    #recurvise case ~> we haven't yet filtered to one binary number and must continue traversing our mode array
    else:
        return co2ScrubberRatingCalculator(i, filtered_array)

#create function lifeSupportRatingCalculator
def lifeSupportRatingCalculator(oxygen_generator_rating, co2_scrubber_rating): #list input of binary digits for both parameters
    oxygen_generator_rating_decimal = binaryToDecimalConverter(oxygen_generator_rating)
    co2_scrubber_rating_decimal = binaryToDecimalConverter(co2_scrubber_rating)
    return oxygen_generator_rating_decimal * co2_scrubber_rating_decimal #decimal output

#set parameters for oxygen_generator_rating and co2_scrubber_rating
oxygen_generator_rating = oxygenGeneratorRatingCalculator(0, diagnostic_report_array)
co2_scrubber_rating = co2ScrubberRatingCalculator(0, diagnostic_report_array)
print("Part #02:", lifeSupportRatingCalculator(oxygen_generator_rating, co2_scrubber_rating))
# Ans. 3969126