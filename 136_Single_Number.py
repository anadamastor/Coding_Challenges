# Given a non-empty array of integers nums, 
# every element appears twice except for one. 
# Find that single one.
# LEETCODE 136

# You must implement a solution with a linear 
# runtime complexity and use only constant extra 
# pace.

def singleNumber(nums):
  freq_vec = {}
  for i in range(len(nums)):
    freq_vec.setdefault(nums[i], 0)
    freq_vec[nums[i]] += 1
  return min(freq_vec, key=freq_vec.get)