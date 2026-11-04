"""Longest Consecutive Sequence - LeetCode 128

Given an unsorted array of integers, find the length of the longest
consecutive elements sequence.
"""

phase = 1
difficulty = "medium"
leetcode_id = 128
title = "Longest Consecutive Sequence"

# ── Attempts ──────────────────────────────────────────────

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set(nums)
        max_v = 0
        for n in s:
            if (n - 1) in s:
                continue
            count = 1
            while (n + count) in s:
                count += 1
            max_v = max(count, max_v)
        return max_v


# ── Tests ─────────────────────────────────────────────────

tests = {
    "method": "longestConsecutive",
    "cases": [
        {"args": [[100, 4, 200, 1, 3, 2]], "expected": 4},
        {"args": [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], "expected": 9},
        {"args": [[]], "expected": 0},
        {"args": [[1]], "expected": 1},
    ],
}


# ── Notes ─────────────────────────────────────────────────

"""
## Your Notes — Longest Consecutive Sequence

### The Problem
Given an unsorted array, find the longest chain of consecutive numbers.
Order in the array doesn't matter — only which numbers exist.

### The Idea
Dump everything into a **set** for O(1) lookups. Then only start counting from **chain starters** — numbers where
`x - 1` doesn't exist in the set. Walk forward (x, x+1, x+2...) and count how far the chain goes. Track the max.

### Why It's O(n)
Every number gets visited at most twice — once in the loop, once as part of someone's chain. No number belongs to two chains.
The two nested loops look scary but the total work is linear.

### The Bug You Hit
Iterating over the **array** instead of the **set**. Duplicates in the array mean you recount the same chain over and over.
 Always iterate over the set.

### The Pattern Worth Remembering
When you need to check "does this value exist?" many times, a **set** is your friend. The trick of skipping non-starters (`if x-1 exists, skip`)
 turns a potentially quadratic approach into a linear one. This "only process from the root/start" pattern shows up everywhere — connected components,
 union-find, interval merging.

### Meta Learning

- **Before coding, ask: am I doing repeated work?** Your brute force instinct (start a chain from every number) was right in spirit. The only
refinement was skipping numbers that aren't chain starters.

- **Small details cause TLE.** Your logic was 100% correct. The only issue was `for n in nums` vs `for n in s` — one word difference, but it
 changes worst-case complexity entirely. When you get TLE with correct logic, look for redundant iterations first.

- **Unused variables are a smell.** That `positions = []` hinted that your thinking shifted mid-solve but the code didn't fully clean up. When you
finish solving, do a quick pass — delete anything you're not using.

- **Know your alternatives.** Sorting gives O(n log n) with less memory. HashSet gives O(n) with more memory. For competitive programming, pick based
 on constraints. For interviews, mention both and explain the tradeoff — interviewers love that.

- **Don't confuse this with LIS.** Longest Consecutive Sequence ignores array order and cares about value proximity. Longest Increasing Subsequence
respects array order and cares about relative magnitude. Different problems, different techniques.
"""
