# Exercise 3
# Write a program that, given an array v of n numbers and another number k,
# determines whether or not there exist two elements in v whose sum is exactly k.
# For example, given v = [10, 5, 2, 7] and k = 17, the output expected is true
# because (10 + 7 = 17).

v = [10, 5, 2, 7]
k = 12



def testearray(v, k):
    for i in range(len(v) - 1):  # N
        for j in range(i + 1, len(v)):  # N
            soma = v[i] + v[j]
            if soma == k:
                return True
    return False

print(testearray(v,k))

