#PART B
import itertools
from collections import Counter

def undoom_dice(Die_A, Die_B):
    
    newDie_A = []
    newDie_B = []
    all_combinations = len(Die_A) * len(Die_B)
    sum_value_frequencies = []
    for pair in itertools.product(Die_A, Die_B):
         sum_value_frequencies+=[sum(pair)]
    sum_value_counter = Counter(sum_value_frequencies)
    max_sum_frequency = max(sum_freq for sum_freq in sum_value_counter.values())
    
    for dot in Die_A:
        if dot <= 4:
            newDie_A.append(dot)
        else:
            newDie_A.append(4)

    newDie_B = Die_B

    return newDie_A, newDie_B

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

newDie_A, newDie_B = undoom_dice(Die_A, Die_B)

print("After dooming dices, the new dices: ")
print("New Die A:", newDie_A)
print("New Die B:", newDie_B)


