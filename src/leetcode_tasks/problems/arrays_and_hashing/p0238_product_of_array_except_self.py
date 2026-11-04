"""Product of Array Except Self - LeetCode 238

Given an integer array, return an array where each element is the product
of all elements except itself. No division allowed.
"""

phase = 1
difficulty = "medium"
leetcode_id = 238
title = "Product of Array Except Self"

# ── Attempts ──────────────────────────────────────────────

# Attempt 1 — separate prefix and suffix arrays
class Attempt1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])
        suffix = [0 for i in nums]
        suffix[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        result = []
        for i, _ in enumerate(nums):
            result.append(prefix[i] * suffix[i])
        return result


# Attempt 2 — cleaner prefix and suffix
class Attempt2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])
        suffix = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result


# Attempt 3 — O(1) space, reuse prefix array
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            prefix[i] = prefix[i] * right
            right *= nums[i]
        return prefix


# ── Tests ─────────────────────────────────────────────────

tests = {
    "method": "productExceptSelf",
    "cases": [
        {"args": [[1, 2, 3, 4]], "expected": [24, 12, 8, 6]},
        {"args": [[-1, 1, 0, -3, 3]], "expected": [0, 0, 9, 0, 0]},
        {"args": [[2, 3]], "expected": [3, 2]},
    ],
}


# ── Notes ─────────────────────────────────────────────────

"""
Problem: For each number, find the product of all the other numbers. O(n) time, no division.

Core insight: "Everything except me" = "everything to my left" × "everything to my right"

Prefix = product of all elements to the left, built left to right. Starts at 1 because nothing is to the left of the first element.

Suffix = product of all elements to the right, built right to left. Ends at 1 because nothing is to the right of the last element.

Multiply prefix[i] × suffix[i] at each index and you get the product of everything except that index.

O(1) space trick: Don't make a separate suffix array. Just use a single variable called right, go backwards
 through the prefix array, and multiply the suffix value in on the fly. The prefix array becomes the answer.

What I learned solving this:

I solved it three times, each time making it cleaner. First attempt worked but had messy parts — filling suffix with
0s for no reason, using enumerate when I only needed the index. Second attempt cleaned those up. Third attempt removed the
 suffix array entirely and replaced it with one variable.

Pattern to remember: When a problem says "no division," think about splitting the problem into left and right parts. Prefix
 and suffix arrays let you precompute both halves so you can combine them in O(n).

Meta takeaway: A working solution is always the first goal. Optimization comes after. Going from "it works" to "it's clean" to
 "it's optimal" is the right order. Don't try to write the perfect solution on the first try — build up to it.
"""
