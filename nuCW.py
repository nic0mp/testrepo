# Complete the solution so that it returns true if the first argument(string) 
# passed in ends with the 2nd argument (also a string).
def solution(string, ending):
    return string.endswith(ending)

# Given an array of integers, find the one that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#  The sum of these multiples is 23.Finish the solution so that it returns the sum of all the multiples 
#  of 3 or 5 below the number passed in. Additionally, if the number 
# is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    list_c = []
    for i in range(number):
        if (number % 3 == 0) or (number % 5 ==0):
            list_c.append(i)
        print(list_c)