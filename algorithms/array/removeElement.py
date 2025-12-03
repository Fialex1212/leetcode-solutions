# 27. Remove Element
# https://leetcode.com/problems/remove-element/
# Category: Array, Two Pointers
# Submitted: Dec 03, 2025 11:15


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # 1 variant
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue
            else:
                i += 1

        # 2 variant
        new = []
        for i in nums:
            if i != val:
                new.append(i)
        nums[:] = new
        return len(new)
