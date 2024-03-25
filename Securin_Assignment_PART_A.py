#PART A : 1
Die_A=[1,2,3,4,5,6]
Die_B=[1,2,3,4,5,6]
no_of_sides_A=len(Die_A)
no_of_sides_B=len(Die_B)
total_combinations = no_of_sides_A*no_of_sides_B
print("Total combinations possible:", total_combinations)
print()
print()

#PART A : 2
import itertools

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

matrix = [[0] * 6 for _ in range(6)]

for i, val_1 in enumerate(Die_A):
    for j, val_2 in enumerate(Die_B):
        matrix[i][j] = (val_1, val_2)

count=1
print("[",end=" ")
for row in matrix:
    print("[",end=" ")
    for value in row:
        count=count+1
        print(value,end=" ")
    if(count !=37):
        print("]")
    else:
        print("]",end=" ")
print("]")
print()
print()


#PART A : 3
import itertools

Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

combinations = list(itertools.product(Die_A, Die_B))

total_combinations = len(combinations)

sumValueCount = {}

for combo in combinations:
    sum_val = sum(combo)
    sumValueCount[sum_val] = sumValueCount.get(sum_val, 0) + 1

probabilities = {}
for sum_val, count in sumValueCount.items():
    probabilities[sum_val] = count / total_combinations

for sum_val, prob in probabilities.items():
    print(f"P(Sum={sum_val}) = {prob}")




        






import itertools
from collections import Counter








def undoom_dice(Die_A, Die_B):
    # Initialize new lists for reattached spots on each die
    New_Die_A = []
    New_Die_B = []

    # Calculate the total number of combinations for the original dice
    total_combinations = len(Die_A) * len(Die_B)

    # Determine the maximum frequency of each sum in the original combinations
    sum_frequencies = [sum(pair) for pair in itertools.product(Die_A, Die_B)]

# Count the frequencies of each sum
    sum_counter = Counter(sum_frequencies)

# Find the maximum frequency among the sums
    max_sum_frequency = max(sum_freq for sum_freq in sum_counter.values())
    print(max_sum_frequency)
    # Reattach spots to Die A
    for spot in Die_A:
        # If the spot count is already within the limit, append to New_Die_A as it is
        if spot <= 4:
            New_Die_A.append(spot)
        # If the spot count exceeds 4, adjust it to 4
        else:
            New_Die_A.append(4)

    # Reattach spots to Die B (can have any number of spots)
    New_Die_B = Die_B

    return New_Die_A, New_Die_B

# Example input
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

# Obtain the transformed dice
New_Die_A, New_Die_B = undoom_dice(Die_A, Die_B)

# Print the transformed dice
print("New Die A:", New_Die_A)
print("New Die B:", New_Die_B)


