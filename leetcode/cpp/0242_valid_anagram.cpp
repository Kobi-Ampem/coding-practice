/*
Platform = LeetCode
Problem = 242. Valid Anagram
Link = https://leetcode.com/problems/valid-anagram/
Difficulty = Easy
Language = C++
Pattern = Hashing
Date = 2026-11-25
Minutes =20
Solved alone = N
Re-solved =

Build: g++ -std=c++17 -Wall -Wextra -O2 0242_valid_anagram.cpp && ./a.out
*/

#include <bits/stdc++.h>
using namespace std;

// 1. Understand: An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using every original letter once
//    Two strings are anagrams if they contain the exact same characters
//    with the exact same frequencies (order does not matter).
//    Example 1: MAC -> CAM
//    Example 2: Lemon -> Melon
//    Edge cases (empty, one item, duplicates, negatives):
//      - Different lengths -> false immediately.
//      - Empty strings ("", "") -> true (not in LeetCode constraints since len >= 1, but logically true).
//      - Single matching letter ("a", "a") -> true in LeetCode.
//      - Identical words ("rat", "rat") -> true in LeetCode (counts match, even though English definition differs).
//      - Case/charset -> LeetCode guarantees lowercase English letters 'a'-'z' only.

// 2. Match: Frequency Counter (Fixed-Size Array of size 26).
//    Why? Because the character set is strictly bounded ('a' to 'z'), an array of 26 integers
//    acts as an O(1)-space hash map without hashing overhead.

// 3. Plan: Target time O(n), target space O(1).
//    1. If s.length() != t.length(), return false.
//    2. Create an integer array count[26] initialized to 0. Loop through both strings simultaneously:
//       increment count for s[i] and decrement count for t[i].
//    3. Loop through count[26]; if any entry is not 0, return false. Otherwise, return true.

// 4. Implement: turn each plan step into code.
class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.length() != t.length())
        {
            return false;
        }

        int count[26] = {0};

        for (int i = 0; i < s.length(); i++)
        {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }

        for (int c : count)
        {
            if (c != 0)
            {
                return false;
            }
        }

        return true;
    }
};

// 5. Review: Trace s = "anagram", t = "nagaram"
//    - Lengths: both 7 -> continue.
//    - i = 0: s[0]='a' (count[0] = 1),  t[0]='n' (count[13] = -1)
//    - i = 1: s[1]='n' (count[13] = 0), t[1]='a' (count[0] = 0)
//    - i = 2: s[2]='a' (count[0] = 1),  t[2]='g' (count[6] = -1)
//    - i = 3: s[3]='g' (count[6] = 0),  t[3]='a' (count[0] = 0)
//    - i = 4: s[4]='r' (count[17] = 1), t[4]='r' (count[17] = 0)
//    - i = 5: s[5]='a' (count[0] = 1),  t[5]='a' (count[0] = 0)
//    - i = 6: s[6]='m' (count[12] = 1), t[6]='m' (count[12] = 0)
//    - Final check: all 26 elements in count are 0 -> returns true.

// 6. Evaluate: Time O(n) where n is string length (single pass + 26-step check),
//              Space O(1) (fixed array of 26 integers).

int main()
{
    Solution sol;
    assert(sol.isAnagram("anagram", "nagaram") == true);
    assert(sol.isAnagram("rat", "car") == false);
    assert(sol.isAnagram("a", "a") == true);
    assert(sol.isAnagram("a", "b") == false);
    assert(sol.isAnagram("ab", "a") == false);
    assert(sol.isAnagram("", "") == true);
    cout << "all examples pass" << endl;
    return 0;
}
