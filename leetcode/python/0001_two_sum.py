"""
Platform = LeetCode
Problem = 1. Two Sum
Link = https://leetcode.com/problems/two-sum/
Difficulty = Easy
Language = Python
Pattern = Hash Map (Complement Lookup)
Date = 2026-11-27
Minutes = 18
Solved alone = Y
Re-solved =
"""

# 1. Understand: Find the indices of two distinct elements in nums that add up to target
#    Example 1: nums =, target = 9 -> [0, 1] (2 + 7 = 9)
#    Example 2: nums =, target = 6 -> [1, 2] (2 + 4 = 6)
#    Edge cases (empty, one item, duplicates, negatives):
#    - Empty/one item: Guaranteed at least 2 elements by constraints.
#    - Duplicates: e.g., [3, 3], target = 6 ->. Checking before inserting avoids reusing the same index.
#    - Negatives/Zeros: e.g., [-3, 4, 3, 90], target = 0 ->. Standard subtraction handles negatives naturally.

# 2. Match: which pattern, and why?
#    Hash Map (Dictionary). Instead of a nested loop checking every pair in O(n^2), trade O(n) space to store visited values and check target - current_num in O(1) time.

# 3. Plan: the steps, written before any code. Target time and space.
#    Target: Time O(n), Space O(n)
#    1. Initialize an empty dictionary seen to map number and index
#    2. Loop through nums using enumerate to get both index i and value num
#    3. Calculate complement = target - num
#    4. If complement is already in seen, return [seen[complement], i].
#    5. Otherwise, store seen[num] = i and continue.

# 4. Implement: turn each plan step into code.
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


# 5. Review: trace example 1 by hand, line by line, before running.
#    nums =, target = 9
#    - seen = {}
#    - i = 0, num = 2: complement = 9 - 2 = 7. Is 7 in seen? No. seen = {2: 0}.
#    - i = 1, num = 7: complement = 9 - 7 = 2. Is 2 in seen? Yes (index 0).
#    - Return [seen[2], 1] ->. Matches expected output.

# 6. Evaluate: time O(n), space O(n).
#    - Time: O(n) because we traverse the list once, and dictionary lookups take O(1) average time.
#    - Space: O(n) because in the worst case, we store up to n - 1 elements in the dictionary.


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([-3, 4, 3, 90], 0) == [0, 2]
    print("all examples pass")
