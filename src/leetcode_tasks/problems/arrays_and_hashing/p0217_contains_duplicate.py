"""Contains Duplicate - LeetCode 217

Given an integer array, return true if any value appears at least twice.
"""

phase = 1
difficulty = "easy"
leetcode_id = 217
title = "Contains Duplicate"

# ── Attempts ──────────────────────────────────────────────

# Attempt 1 — check-as-you-go with early exit
class Attempt1:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False


# Attempt 2 — one-liner set comparison
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


# ── Tests ─────────────────────────────────────────────────

tests = {
    "method": "containsDuplicate",
    "cases": [
        {"args": [[1, 2, 3, 1]], "expected": True},
        {"args": [[1, 2, 3, 4]], "expected": False},
        {"args": [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]], "expected": True},
    ],
}


# ── Notes ─────────────────────────────────────────────────

'''
Same lesson reinforced: check as you go beats processing everything first.

But there's a new layer here — you wrote both approaches, so the takeaway is: know when a shortcut exists,
but understand why the longer version matters.

The one-liner (set(nums) != len(nums)) is clever, but it always scans the full list. The loop version
can bail out on the first duplicate. In an interview or with huge data, that early exit matters.

So the meta learning: "shorter code" and "better solution" aren't always the same thing.
'''
