# Exercise 1
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix  is shown below:
# [
#   [ 1, 2, 3 ],
#   [ 4, 5, 6 ],
#   [ 9, 8, 9 ]
# ]
# The left-to-right diagonal is 1 + 5 + 9 = 15.
# The right to left diagonal is 3 + 5 + 9 = 17.
# So their absolute difference is |15 - 17| = 2.

matrix = [
  [1, 2, 3, 4],
  [4, 5, 6, 5],
  [9, 8, 9, 6],
  [3, 4, 5, 7],
]

def diagonal_sum(matrix):
    left_sum = 0
    right_sum = 0
    for i in range(len(matrix)):
        left_sum += matrix[i][i]
        right_sum += matrix[i][(len(matrix) - 1) - i]
    absolute_difference = abs(left_sum - right_sum)
    return absolute_difference

print(diagonal_sum(matrix))



# Exercise 2
# Write a program that, given an array v of n numbers and another number k,
# determines whether or not there exist two elements in v whose sum is exactly k.
# For example, given v = [10, 5, 2, 7] and k = 17, the output expected is true
# because (10 + 7 = 17).
