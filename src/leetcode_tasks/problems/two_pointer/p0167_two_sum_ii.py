"""Two Sum II - LeetCode 167

Given a 1-indexed sorted array, find two numbers that add up to the target.
Return their indices (1-indexed).
"""

phase = 1
difficulty = "medium"
leetcode_id = 167
title = "Two Sum II"

# ── Attempts ──────────────────────────────────────────────

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            n1, n2 = numbers[l], numbers[r]
            result = n1 + n2
            if result == target:
                return [l + 1, r + 1]
            if result > target:
                r -= 1
            elif result < target:
                l += 1
        return -1


# ── Tests ─────────────────────────────────────────────────

tests = {
    "method": "twoSum",
    "cases": [
        {"args": [[2, 7, 11, 15], 9], "expected": [1, 2]},
        {"args": [[2, 3, 4], 6], "expected": [1, 3]},
        {"args": [[-1, 0], -1], "expected": [1, 2]},
    ],
}


# ── Notes ─────────────────────────────────────────────────

"""
Two Sum II — LeetCode 167

The array is already sorted and you need to find
two numbers that add up to the target. The constraint says constant extra space so you can't use a hashmap.

Two pointers is the natural fit here. Start one pointer at
the beginning and one at the end. Add the two numbers. If the sum is too big, move the r
ight pointer left to make it smaller. If the sum is too small, move the left pointer right to make it
bigger. If it matches, return the indices plus one since the problem uses 1-indexed arrays.

This works because the array is sorted. Moving right inward always decreases the sum. Moving left outward
always increases it. So you're guaranteed to converge on the answer if one exists, and the problem says it always does.

Time is O(n), space is O(1). This is exactly what the problem is asking for. Solution is clean, nothing to trim.

You picked the right tool immediately this time. Sorted array plus constant space constraint — two pointers
was the obvious choice and you went straight for it. That's pattern recognition building up.

Compare this to your palindrome solution where you started with zip and reversed and all before simplifying. Here
you didn't overcomplicate it. You wrote the direct solution first. That's progress.

The bigger takeaway is learning to read constraints as hints. "Sorted" screams binary search or two pointers. "Constant space" rules
out hashmaps. "Exactly one solution" means you don't need to handle duplicates or no-answer cases. Every constraint in a problem is a
clue pointing you toward the intended approach. Get in the habit of reading them before you start thinking about solutions.
"""
