# https://leetcode.com/problems/two-sum/

# 1. Two Sum
# Easy

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

# Brute Force Solution:
# A brute force solution would involve checking every pair of numbers in the array to see if their sum equals the target. This solution has a time complexity of O(n^2), where n is the length of the array. It involves two nested loops to compare each pair of numbers. Here's an implementation in Python:

class Solution:
    def twoSum(nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
            

# Hash Map Solution:
# A more efficient solution involves using a hash map (also known as a dictionary or an associative array) to store the values and their indices as we iterate through the array. In this solution, we check if the complement of the current number (target minus the current number) exists in the hash map. If it does, we have found the pair that adds up to the target. This solution has a time complexity of O(n), where n is the length of the array. Here's an implementation in Python:

# Two-Pass Hash Map Solution:

# - In this solution, we'll make two passes over the input array nums. In the first pass, we'll create a hash map where the keys are the elements of nums and the values are their corresponding indices.
# - After creating the hash map, we'll perform a second pass over nums. For each element num in nums, we'll calculate the complement complement = target - num.
# - If the complement exists in the hash map and its corresponding index is not the same as the current index, we have found a valid pair. We'll return the indices of the current element and its complement.
# - If no valid pair is found, we'll return an empty array.

# The time complexity of this solution is O(n) since we make two passes over the input array nums. Here's the implementation in Python:

class Solution:
    def twoSum(nums, target):
        num_map = {}
        # First pass: create hash map
        for i, num in enumerate(nums):
            num_map[num] = i
        
        # Second pass: check for valid pairs
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map and num_map[complement] != i:
                return [i, num_map[complement]]
        
        return []  # No valid pair found

# One-Pass Hash Map Solution:

# - In this solution, we'll make a single pass over the input array nums. As we iterate through nums, we'll check if the complement of the current element exists in the hash map.
# - If the complement exists, we have found a valid pair. We'll return the indices of the current element and its complement.
# - If the complement doesn't exist, we'll add the current element to the hash map for future lookups.
# - If no valid pair is found, we'll return an empty array.

# The time complexity of this solution is O(n) since we make a single pass over the input array nums. Here's the implementation in Python:
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

# Both solutions have a similar time complexity, but the one-pass hash map solution is more efficient since it requires only a single pass over the input array.


# The two-pointer approach is generally used for solving problems where you need to find a pair of elements in a sorted array that satisfies a certain condition. Since the problem doesn't mention anything about the array being sorted, the two-pointer approach is not directly applicable in this case.

# However, you can modify the approach slightly to solve the twoSum problem efficiently. Here's how you can do it:

# - Sort the input array nums in non-decreasing order. This step can be done in O(n log n) time complexity using a sorting algorithm like quicksort or mergesort.
# - Initialize two pointers, left and right, pointing to the start and end of the sorted array, respectively.
# - While the left pointer is less than the right pointer:
#     -- Calculate the sum of the elements at the left and right pointers, i.e., sum = nums[left] + nums[right].
#     -- If sum is equal to the target, return the indices [left, right].
#     -- If sum is less than the target, increment the left pointer by one (move it to the right).
#     -- If sum is greater than the target, decrement the right pointer by one (move it to the left).
# - If no valid pair is found, return an empty list.

# The time complexity of this approach is O(n log n) due to the sorting step. Here's an implementation in Python:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sort the input array in non-decreasing order
        nums.sort()
        
        # Initialize two pointers
        left = 0
        right = len(nums) - 1
        
        # Iterate until the two pointers meet
        while left < right:
            # Calculate the sum of the elements at the two pointers
            curr_sum = nums[left] + nums[right]
            
            # Check if the sum is equal to the target
            if curr_sum == target:
                return [left, right]
            elif curr_sum < target:
                # Increment the left pointer
                left += 1
            else:
                # Decrement the right pointer
                right -= 1
        
        # No valid pair found
        return []
