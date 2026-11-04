"""Valid Palindrome - LeetCode 125

Given a string, determine if it is a palindrome considering only
alphanumeric characters and ignoring cases.
"""

phase = 1
difficulty = "easy"
leetcode_id = 125
title = "Valid Palindrome"

# ── Attempts ──────────────────────────────────────────────

# Attempt 1 — zip with reversed
class Attempt1:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(c for c in s if c.isalnum()).lower()
        return all(x == y for x, y in zip(list(clean), list(reversed(clean)), strict=True))


# Attempt 2 — slice reversal
class Attempt2:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(c for c in s if c.isalnum()).lower()
        return clean == clean[::-1]


# Attempt 3 — two pointer, O(1) space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


# ── Tests ─────────────────────────────────────────────────

tests = {
    "method": "isPalindrome",
    "cases": [
        {"args": ["A man, a plan, a canal: Panama"], "expected": True},
        {"args": ["race a car"], "expected": False},
        {"args": [" "], "expected": True},
        {"args": ["aa"], "expected": True},
    ],
}


# ── Notes ─────────────────────────────────────────────────

"""
Valid Palindrome — LeetCode 125

The problem asks you to check if a string is a palindrome after you strip out everything that isn't a letter or number and make it all lowercase.

Attempt 1 was my first pass. I cleaned the string using isalnum to keep only letters and digits, lowered it,
then zipped it with its reverse and checked if every pair matched using all(). It works but it's overcomplicated.
I'm creating two full lists, using strict mode on zip for no reason since both sides are always the same length, and checking
every character twice because position 0 gets compared to the last and later the last gets compared to position 0.

Attempt 2 is the clean version of the same idea. Build the cleaned string, reverse it with slice notation, compare directly. One
line of logic. Does exactly what attempt 1 does without the extra machinery. This is the most Pythonic way to write it.

Attempt 3 is the two pointer approach. No new string gets created at all. One pointer starts from the left, one from the right.
Both skip over non-alphanumeric characters. Then you compare the characters at each pointer after lowering them. If they ever don't
 match, return false. If the pointers meet in the middle without a mismatch, it's a palindrome. This uses constant extra space unlike
 the first two which create a whole new string.

The takeaway is that attempt 2 is what you write when you want clean readable code. Attempt 3 is what you bring up in an interview to
show you understand space optimization. Attempt 1 works but there's no reason to reach for zip, reversed, list, all, and strict when a
 simple equality check does the job. Simpler is better.
"""
