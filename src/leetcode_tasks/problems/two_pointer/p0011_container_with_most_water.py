"""Container With Most Water - LeetCode 11

Given n vertical lines at positions 0..n-1 with heights height[i],
find two lines that form a container holding the most water.
Area = min(height[left], height[right]) * (right - left).
"""

phase = 1
difficulty = "medium"
leetcode_id = 11
title = "Container With Most Water"

# ── Attempts ──────────────────────────────────────────────

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        current_best = 0
        while left < right:
            h1, h2 = height[left], height[right]
            a = min(h1, h2) * (right - left)
            if a > current_best:
                current_best = a
            if h1 <= h2:
                left += 1
            else:
                right -= 1
        return current_best


# ── Tests ─────────────────────────────────────────────────

tests = {
    "method": "maxArea",
    "cases": [
        {"args": [[1, 8, 6, 2, 5, 4, 8, 3, 7]], "expected": 49},
        {"args": [[1, 1]], "expected": 1},
        {"args": [[4, 3, 2, 1, 4]], "expected": 16},
        {"args": [[1, 2, 1]], "expected": 2},
    ],
}


# ── Notes ─────────────────────────────────────────────────

"""
key learnings:

why two pointers work on UNSORTED input:
  - in 3Sum, sorting enabled two pointers. here the array can't be sorted
    because position matters (width = right - left).
  - instead, starting at the widest container (left=0, right=n-1) is the key.
    width can only shrink from here, so the only way to find a bigger area
    is to find a taller minimum height.

the "move the shorter wall" rule:
  - area = min(h1, h2) * width. the shorter wall caps the height.
  - keeping the short wall and moving the tall one can NEVER help:
    width shrinks by 1, and min height stays the same or gets worse.
  - moving the short wall MIGHT help: you could find a taller wall that
    compensates for the lost width.
  - when h1 == h2, moving either (or both) is fine — neither side can
    improve while the other stays.

the wording trap:
  - "container with most water" sounds like you need walls on all sides
    and water can't leak over shorter intermediate walls. it's NOT that.
  - it's just: pick two lines, area = min(heights) * distance. ignore
    everything in between. (Trapping Rain Water is the harder version
    where intermediate walls matter.)

complexity: O(n) time, O(1) space — each pointer moves at most n times total.

original bug: three separate if statements for h1>h2, h2>h1, h1==h2 caused
  an infinite loop risk. simplified to if h1 <= h2: move left, else: move right.
"""
