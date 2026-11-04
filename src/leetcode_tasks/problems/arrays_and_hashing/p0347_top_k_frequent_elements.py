"""Top K Frequent Elements - LeetCode 347

Given an integer array and an integer k, return the k most frequent elements.
"""

from collections import Counter

phase = 1
difficulty = "medium"
leetcode_id = 347
title = "Top K Frequent Elements"

# ── Attempts ──────────────────────────────────────────────

# Attempt 1 — variable shadowing bug
class Attempt1:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [k[0] for k in Counter(nums).most_common(k)]


# Attempt 2 — clean unpacking
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [num for num, _ in Counter(nums).most_common(k)]


# ── Tests ─────────────────────────────────────────────────

tests = {
    "method": "topKFrequent",
    "cases": [
        {"args": [[1, 1, 1, 2, 2, 3], 2], "expected": [1, 2]},
        {"args": [[1], 1], "expected": [1]},
        {"args": [[4, 4, 4, 1, 1, 2, 2, 2, 3], 2], "expected": [4, 2]},
    ],
}


def compare(result, expected):
    return sorted(result) == sorted(expected)


# ── Notes ─────────────────────────────────────────────────

"""
The Core Idea

Count how often each number appears, then grab the top k. Python's Counter class does both of these things out of the box.

My Journey
Attempt 1 — Variable Shadowing Bug

I wrote a one-liner using Counter.most_common(k), which was the right call.
But I reused k as my loop variable in the list comprehension, shadowing the function parameter k.
It worked by accident because most_common(k) evaluates before the loop runs, but it's a bug waiting to happen.
I also used index access k[0] instead of unpacking the tuple, making it harder to read.

Attempt 2 — Clean Version

Fixed the shadowing by using num as the loop variable.
Unpacked the tuple properly with num, _ so it's immediately clear I'm taking the number and discarding the count. Same logic, no hidden bugs.

Meta Learnings
Watch variable shadowing. If a loop variable has the same name as a parameter, you've created a silent bug. Always pick distinct names.
It might work today and break tomorrow.
Unpack tuples instead of indexing. num, count = item is always clearer than item[0]. It gives names to your data and shows your intent.
Use _ for values you don't need.
Know your standard library. Counter.most_common(k) solved this in one line. Without it, I'd be writing a dictionary, sorting by values,
slicing — doing by hand what the library already does. When working with frequencies, Counter is almost always the answer.
Think about time complexity after you have a working solution. The follow-up asked for better than O(n log n). most_common uses a heap internally,
 so it runs in O(n log k), which meets that requirement. Know why your solution is fast, not just that it passes.
Short code isn't always simple code. My one-liner was compact but had a naming bug hiding in it. A slightly longer version with clear variable
names is better every time. Readability beats cleverness.
"""
