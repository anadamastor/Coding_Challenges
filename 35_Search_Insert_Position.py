#
# Given a sorted array of distinct integers and 
# a target value, return the index if the target 
# is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n)
#  runtime complexity.
#
def searchInsert(nums,target):
    if target in nums:
        return nums.index(target)
    for i in range(len(nums)):
        if nums[i] > target:
            return i
    return len(nums)

nums = [3,3,5,6]
target = 0

print(searchInsert(nums,target))