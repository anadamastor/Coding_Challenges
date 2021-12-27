# https://leetcode.com/problems/maximum-average-subarray-i/
# 643. Maximum Average Subarray I
# You are given an integer array nums consisting 
# of n elements, and an integer k.

# Find a contiguous subarray whose length is equal
# to k that has the maximum average value and return 
# this value. Any answer with a calculation error less 
# than 10-5 will be accepted.

nums = [1,12,-5,-6,50,3]
# nums = [0,1,1,3,3]
k = 4

# Slicing approach ##################################
# def findMaxAverage(nums,k):
#   avg = []
#   for i in range(len(nums) - k + 1):
#     summ = 0
#     for j in range(i, i + k):
#       summ += nums[j]
#       avg.append(summ/k)
#   return max(avg)

# print(findMaxAverage(nums,k))

# Slicing approach ##################################
# Check this

# def findMaxAverage(nums,k):
#   avg = 0
#   output = 0
  
#   if len(nums) == 1:
#     return nums[0]

#   if len(nums) - k < 2:
#     len_range = 2
#   else:
#     len_range = len(nums) - k

#   for i in range(len_range):
#     print(i)
#     print(nums[i:i+k])
#     summ = sum(nums[i:i+k])
#     avg = summ/k

#     if avg > output:
#       output = avg    

#   return output

# print(findMaxAverage(nums,k))
# # findMaxAverage(nums,k)

# # Fedes approach ##################################

import sys


def findMaxAverage(nums, k):
  left = 0
  right = k

  maximum = - sys.maxsize - 1 # minimum integer in 

  while right <= len(nums):
    current_average = sum(nums[left:right]) / k
    maximum = max(current_average, maximum)

    left += 1
    right += 1
  
  return maximum

print(findMaxAverage(nums,k))

## Sliding window ##################################
def findMaxAverageSliding(nums, k):

  window_sum  = sum(nums[:k])
  max_avg = window_sum  / k

  for i in range(len(nums) - k):
    window_sum = window_sum  - nums[i] + nums[i+k]
    next_avg = window_sum / k
    max_avg = max(next_avg , max_avg)
    
  return max_avg
print(findMaxAverageSliding(nums,k))