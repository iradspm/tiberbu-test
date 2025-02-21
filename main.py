"""
Q1. "Write a function that counts how many times each character appears in a string and returns the result as a dictionary. Ignore spaces and make it case-insensitive (treat 'A' and 'a' as the same character).

Q2. Given an array of integers and a target sum, return the indices of two numbers in the array that add up to the target sum. You may assume there is exactly one solution, and you cannot use the same element twice. Return the indices in any order.
Q3. Given an array of integers and a target sum, find all triplets of consecutive numbers in the array that add up to the target sum. Return all starting indices where such triplets are found. The array may contain negative numbers and zeros. Multiple triplets may sum to the target.

Examples:
Input: nums = [1, 2, 3, 6, 5, 4], target = 6
Output: [0] // explanation: triplet [1,2,3] starts at index 0

Input: nums = [2, 3, 1, 2, 3, 1], target = 6
Output: [0, 3] // explanation: [2,3,1] appears twice, starting at indices 0 and 3

Input: nums = [-1, 0, 7, -2, 1, 4], target = 6
Output: [0] // explanation: [-1,0,7] starts at index 0

"""
from collections import Counter

def q_1(value:str):
    """number of times character appears in a string"""
    value = value.replace(" ", "").lower()
    return dict(Counter(value))

def q_3(nums:list, target:int):
    """
    Q3. Given an array of integers and a target sum, find all triplets of consecutive numbers in the array that add up to the target sum. Return all starting indices where such triplets are found. The array may contain negative numbers and zeros. Multiple triplets may sum to the target.
    """
    results = [] # O(1)
    for i in range(len(nums)-2): # O(n) - 3
        if nums[i] + nums[i+1] + nums[i+2] == target: #  O(1)
            results.append(i) # O(1)
    return results # O(1)

test_q1 = q_1("Tiberbu")
print(test_q1)
test_q3 = q_3([-1, 0, 7, -2, 1, 4], 6)
print(test_q3)