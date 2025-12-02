# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/
# Category: Hash Table, Math, String
# Submitted: Dec 03, 2025 00:40
# Time: O(n)
# Space: O(n)


class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = romans[s[0]]
        for i in range(1, len(s)):
            current = romans[s[i]]
            prev = romans[s[i - 1]]
            if current < prev:
                total -= current
            else:
                total += current
        return total
