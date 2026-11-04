"""Two Sum - LeetCode 1

Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.
"""

phase = 1
difficulty = "easy"
leetcode_id = 1
title = "Two Sum"

# ── Attempts ──────────────────────────────────────────────

# Attempt 1 — overcomplicated two-pass approach
class Attempt1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr = {}
        for i, n in enumerate(nums):
            t = (i, target - n)
            k = n
            if k in arr:
                arr[k].append(t)
            else:
                arr[k] = [t]
        for k in arr.keys():
            l = arr[k]
            for i in l:
                ind, val = i
                if val in arr:
                    r = arr[val]
                    ind2, val2 = r[0]
                    if ind2 == ind:
                        continue
                    return [ind, ind2]
        return -1


# Attempt 2 — one-pass hash map (clean)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr = {}
        for i, n in enumerate(nums):
            r = target - n
            if r in arr:
                index = arr[r]
                return [index, i]
            arr[n] = i


# ── Tests ─────────────────────────────────────────────────

tests = {
    "method": "twoSum",
    "cases": [
        {"args": [[2, 7, 11, 15], 9], "expected": [0, 1]},
        {"args": [[3, 2, 4], 6], "expected": [1, 2]},
        {"args": [[3, 3], 6], "expected": [0, 1]},
    ],
}


# ── Notes ─────────────────────────────────────────────────

'''
Meta Learning:
The big lesson is: don't collect everything first and search later — check as you go.

In Attempt 1, you built a whole map of all the data, then went back and searched through it. In Attempt 2, you checked each number while you were storing them. The moment you found a match, you stopped.

That's the pattern: build and search at the same time. It's simpler code, fewer bugs, and often faster. You'll see this idea come up again and again in other problems.

Notes:
Attempt 1 — Overengineered but on the right track

Your first attempt shows you understood the core idea: use a hash map to avoid O(n²) brute force. But the execution got tangled:

You're building a full map of every number to a list of (index, complement) tuples, then doing a second pass to look up complements. This is essentially two passes over the data plus nested loops over the stored tuples — more complex than it needs to be.
The if ind2 == ind: continue guard shows you were thinking about the "can't use the same element twice" constraint, which is good.
But the whole structure — lists of tuples, a second loop over arr.keys(), unpacking r[0] — introduces a lot of surface area for bugs and makes the logic hard to follow. You're storing information you never really need (every pair's complement) and then searching through your own stored data.

The fundamental issue: you're doing the "store" and "lookup" in two separate phases when they can happen in one pass.

Attempt 2 — Clean and nearly correct

This is a big improvement. One pass, simple complement check, early return. The logic is tight:

For each number, compute the complement.
Check if the complement is already in the map.
If yes, return. If no, store the current number.

Time I took to solve: 1 hour
'''
