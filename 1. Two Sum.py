# The problem:
# Given an array of integers nums and an integer
# target, return indices of the two numbers such that they add up to target.

#Pseudocode:
#Reuqirment: to have the index and the value of each element in the list, have the target to comapre
#steps: looping over the list for the first time to have the index and the value of the first position
#looping for the second time from the second position to have the index and the value too
# then compare, if the value of both of them ar eequal to the target
# Then print the indexs of them

# Solution
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]