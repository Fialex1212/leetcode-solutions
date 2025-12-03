# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Category: Array, Two Pointers
# Submitted: Dec 03, 2025 10:47


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = sorted(set(nums))

        for i in range(len(k)):
            nums[i] = k[i]

        return len(k)
