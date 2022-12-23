#initialize
import os
try:
    os.chdir('./2022/Day_02')
except:
    pass

#import sea floor depth measurement values
with open("rock_paper_scissors.txt", "r") as f:
    rps_strategy_raw = f.read().split('\n')
    rps_strategy = []
    for i in rps_strategy_raw:
        rps_strategy.append(i.split())

# ROCK = 1
# PAPER = 0
# SCISSORS = -1

# OPP	YOU
# Rock - Rock = 0 [YOU TIE]
# Rock - Paper = 1 [YOU WIN]
# Rock -  Scissors = 2 [YOU LOSE]

# Paper - Rock = -1 [YOU LOSE]
# Paper - Paper = 0 [YOU TIE]
# Paper - Scissors = 1 [YOU WIN]

# Scissors - Rock = -2 [YOU WIN]
# Scissors - Paper = -1 [YOU LOSE]
# Scissors - Scissors = 0 [YOU TIE]

# - If 0, you tie.
# - If 1 or -2, you win.
# - If -1 or 2, you lose.

#create hash map for shape selection score
rps_shape_scores = {}
rps_shape_scores['A'] = 1 #rock win
rps_shape_scores['B'] = 2 #paper win
rps_shape_scores['C'] = 3 #scissors win

#create hash map for outcome scores
rps_outcome_scores = {}
#win
rps_outcome_scores['1'] = 6
rps_outcome_scores['-2'] = 6
#lose
rps_outcome_scores['-1'] = 0
rps_outcome_scores['2'] = 0
#draw
rps_outcome_scores['0'] = 3

#create hash map for outcome scoring determination
rps_outcome_score_map = {}
rps_outcome_score_map['A'] = 1 #Rock, 1
rps_outcome_score_map['B'] = 0 #Paper, 0
rps_outcome_score_map['C'] = -1 #Scissors, -1

#create hash map of rps characters
rps_alt_char_map = {}
rps_alt_char_map['X']='A'
rps_alt_char_map['Y']='B'
rps_alt_char_map['Z']='C'

#Part 01: What would your total score be if everything goes exactly according to your strategy guide?
#create function rpsStrategyScoreCalculator - takes inputs: rps_outcome_score_map [dict], rps_outcomes_scores [dict], rps_shape_scores [dict], rps_alt_char_map [dict], and rps_strategy [list]
def rpsStrategyScoreCalculator(rps_outcome_score_map, rps_outcome_scores, rps_shape_scores, rps_alt_char_map, rps_strategy):
    score = 0
    for match in rps_strategy:
        #compute outcome-based score
        score += rps_outcome_scores[str(rps_outcome_score_map[match[0]] - rps_outcome_score_map[rps_alt_char_map[match[1]]])]
        #compute shape-based score
        score += rps_shape_scores[rps_alt_char_map[match[1]]]
    return score

print("Part #01:", rpsStrategyScoreCalculator(rps_outcome_score_map, rps_outcome_scores, rps_shape_scores, rps_alt_char_map, rps_strategy))
#Ans. 15632


##Part 02: Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
#create hash map of rps forced outcomes
rps_forced_outcome_map = {}
rps_forced_outcome_map['X']='L'
rps_forced_outcome_map['Y']='D'
rps_forced_outcome_map['Z']='W'

#create hash map of rps forced outcome resulting scores
rps_forced_outcome_resulting_selection = {} #forced outcome, opponent's selection
rps_forced_outcome_resulting_selection['L_A'] = 'C'
rps_forced_outcome_resulting_selection['L_B'] = 'A'
rps_forced_outcome_resulting_selection['L_C'] = 'B'
rps_forced_outcome_resulting_selection['D_A'] = 'A'
rps_forced_outcome_resulting_selection['D_B'] = 'B'
rps_forced_outcome_resulting_selection['D_C'] = 'C'
rps_forced_outcome_resulting_selection['W_A'] = 'B'
rps_forced_outcome_resulting_selection['W_B'] = 'C'
rps_forced_outcome_resulting_selection['W_C'] = 'A'


#create function rpsStrategyScoreCalculator - takes inputs: rps_outcome_score_map [dict], rps_outcomes_scores [dict], rps_shape_scores [dict], rps_forced_outcome_map [dict], rps_forced_outcome_resulting_selection [dict], and rps_strategy [list]
def rpsStrategyScoreCalculator_forcedOutcome(rps_outcome_score_map, rps_outcome_scores, rps_shape_scores, rps_forced_outcome_map, rps_forced_outcome_resulting_selection, rps_strategy):
    score = 0
    for match in rps_strategy:
        #compute outcome-based score
        score += rps_outcome_scores[str(rps_outcome_score_map[match[0]] - rps_outcome_score_map[rps_forced_outcome_resulting_selection[str(rps_forced_outcome_map[match[1]])+'_'+match[0]]])]
        #compute shape-based score
        score += rps_shape_scores[rps_forced_outcome_resulting_selection[str(rps_forced_outcome_map[match[1]])+'_'+match[0]]]
    return score

print("Part #02:", rpsStrategyScoreCalculator_forcedOutcome(rps_outcome_score_map, rps_outcome_scores, rps_shape_scores, rps_forced_outcome_map, rps_forced_outcome_resulting_selection, rps_strategy))
#Ans. 14416
