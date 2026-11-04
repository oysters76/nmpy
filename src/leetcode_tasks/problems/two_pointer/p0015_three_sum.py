"""3Sum - LeetCode 15

Given an integer array, return all unique triplets that sum to zero.
"""

phase = 1
difficulty = "medium"
leetcode_id = 15
title = "3Sum"

# ── Attempts ──────────────────────────────────────────────

# Attempt 1 — DFS brute force with Node class
class Node:
    def __init__(self, index, parent, val, depth=0):
        self.index = index
        self.parent = parent
        self.sum = val
        self.depth = depth


class Attempt1:
    def to_result(self, nums, node):
        r = []
        while node is not None:
            r.append(nums[node.index])
            node = node.parent
        return r

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        stack = [Node(i, None, nums[i], 1) for i in range(len(nums))]
        result = set()
        while len(stack) > 0:
            node = stack.pop()
            if node.depth == 3:
                if node.sum == 0:
                    result.add(tuple(sorted(self.to_result(nums, node))))
                continue
            for i in range(node.index + 1, len(nums)):
                stack.append(Node(i, node, node.sum + nums[i], node.depth + 1))
        return [list(t) for t in result]


# Attempt 2 — sort + two pointer (tutored, verbose)
class Attempt2:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        arr = sorted(nums)
        solutions = []
        for i in range(len(arr)):
            fixed = arr[i]

            if i > 0 and arr[i] == arr[i - 1]:
                continue

            complement = fixed * -1

            l = i + 1
            r = len(arr) - 1

            if l >= len(arr):
                continue

            while l <= len(arr) - 1 and l < r:
                n1, n2 = arr[l], arr[r]
                s = n1 + n2
                if s == complement:
                    sol = [fixed, n1, n2]
                    solutions.append(sol)
                    while (l + 1) < len(arr) and arr[l] == arr[l + 1]:
                        l += 1
                    while r >= 0 and arr[r] == arr[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                    continue
                else:
                    if s > complement:
                        r -= 1
                    elif s < complement:
                        l += 1

        return solutions


# Attempt 3 — sort + two pointer (cleaned up)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return result


# ── Tests ─────────────────────────────────────────────────

tests = {
    "method": "threeSum",
    "cases": [
        {"args": [[-1, 0, 1, 2, -1, -4]], "expected": [[-1, -1, 2], [-1, 0, 1]]},
        {"args": [[0, 1, 1]], "expected": []},
        {"args": [[0, 0, 0]], "expected": [[0, 0, 0]]},
    ],
}


def compare(result, expected):
    return sorted(sorted(t) for t in result) == sorted(sorted(t) for t in expected)


# ── Notes ─────────────────────────────────────────────────

"""
key learnings:

the "reduce to a solved problem" pattern:
  - fix one number (nums[i]), then the remaining problem is "find two numbers
    that sum to -nums[i]" — which is Two Sum II (sorted array, two pointers).
  - this is a general technique: kSum reduces to (k-1)Sum by fixing one element.

why sort first:
  - enables two-pointer technique (too big → move right inward, too small → move left outward)
  - enables duplicate skipping without a set (identical values are adjacent after sorting)
  - sorting is O(n log n), dominated by the O(n²) two-pointer scan, so it's "free"

duplicate skipping — two places, both critical:
  1. fixed pointer: if nums[i] == nums[i-1], skip — you'd repeat the exact same search
  2. after finding a triplet: advance left past duplicates, retreat right past duplicates,
     THEN move both one more step. forgetting the final l+=1, r-=1 causes infinite loops.

attempt 1 → attempt 2 journey:
  - attempt 1 (DFS brute force) was O(n³) with a set for dedup. correct but TLE.
  - the insight was: sorting lets you skip duplicates inline, and two pointers
    let you search in O(n) instead of O(n²) for the remaining pair.
  - attempt 2 was the tutored version — verbose but correct. attempt 3 cleaned it up.

O(n²) is optimal for 3Sum — there's a well-known conjecture that you can't do better.

complement = -nums[i] is cleaner than complement = nums[i] * -1
"""
