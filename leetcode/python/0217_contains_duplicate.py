"""
Platform = LeetCode
Problem = 217. Contains Duplicate
Link = https://leetcode.com/problems/contains-duplicate/
Difficulty = Easy
Language = Python
Pattern =  Hash sets
Date = 2026-11-23
Minutes = 25 mins
Solved alone = N
Re-solved =
"""

from typing import List

# 1. Understand: Giving a list of integers, if a number appears more than once, return true. If each number appears just once, return false.
#    Example 1: [1,2,1,1,5,6] - True
#    Example 2: [5,6,7,9,2,0] - False
#    Edge cases (empty, one item, duplicates, negatives): For a list with just one item, expected return is false. Empty list returns False. Duplicates return true. negatives, if appearing once, false, else true.

# 2. Match: which pattern, and why? Hash set: sets hold unique items and checks in in O(1) on avg. uses hashing instead of scanning item by item

# 3. Plan: the steps, written before any code. Target time and space.
#    1. create an empty set and loop through all the items in the list.
#    2. Base case is false, assuming each number appears once.
#    3. for each item in the list, if it is in set already, return true. if not, add the item to the set.
#    4. if the loop finishes, return False.
# Target: O(n) time, O(n) space.


# 4. Implement: turn each plan step into code.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True

            else:
                seen.add(num)
        return False


# 5. Review: trace example 1 by hand, line by line, before running. : seen = {1,2} True

# 6. Evaluate: time O(): O(n), space O(): O(n) .


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 1, 1, 5, 6]) == True  # example 1: 1 repeats
    assert s.containsDuplicate([5, 6, 7, 9, 2, 0]) == False  # example 2: all unique
    assert s.containsDuplicate([]) == False  # edge: empty list
    assert s.containsDuplicate([7]) == False  # edge: one item
    assert s.containsDuplicate([-1, 2, -1]) == True  # edge: negatives repeat
    print("all examples pass")
