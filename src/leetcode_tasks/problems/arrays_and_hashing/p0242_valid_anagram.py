"""Valid Anagram - LeetCode 242

Given two strings s and t, return true if t is an anagram of s.
"""

from collections import Counter

phase = 1
difficulty = "easy"
leetcode_id = 242
title = "Valid Anagram"

# ── Attempts ──────────────────────────────────────────────

# Attempt 1 — manual Counter comparison
class Attempt1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 = Counter(s)
        c2 = Counter(t)
        for i in c1.keys():
            if i not in c2.keys():
                return False
            v1 = c1[i]
            v2 = c2[i]
            if v1 != v2:
                return False
        return True


# Attempt 2 — Counter equality
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2


# ── Tests ─────────────────────────────────────────────────

tests = {
    "method": "isAnagram",
    "cases": [
        {"args": ["anagram", "nagaram"], "expected": True},
        {"args": ["rat", "car"], "expected": False},
        {"args": ["a", "a"], "expected": True},
        {"args": ["ab", "ba"], "expected": True},
    ],
}


# ── Notes ─────────────────────────────────────────────────

"""
Meta learning: before writing a loop, ask "does the data structure already do this for me?"

You saw this same idea with containsDuplicate — a set inherently removes duplicates, so you
didn't need to manually check for them. Here, Counter inherently supports equality comparison, so
 you don't need to manually compare key by key.

The pattern: learn what your tools can do natively, so you don't rebuild their features by hand. Less code, fewer bugs, same result.

First you understand the mechanics, then you trust the abstraction.

Attempt 1 wasn't wrong — it proved you understand what Counter equality means
 (same keys, same counts). Attempt 2 shows you now trust == to do that for you because you've
   already verified it manually.

This is the healthy pattern: build it by hand once so you understand it, then use the shortcut forever.
 If you'd jumped straight to c1 == c2 without ever writing the loop version, you wouldn't truly know what
   it's doing under the hood. Now you do, and that understanding will help when problems get harder and the built-in tools aren't enough.
"""
