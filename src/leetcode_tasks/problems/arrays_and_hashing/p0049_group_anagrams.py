"""Group Anagrams - LeetCode 49

Given an array of strings, group the anagrams together.
"""

from collections import Counter

phase = 1
difficulty = "medium"
leetcode_id = 49
title = "Group Anagrams"

# ── Attempts ──────────────────────────────────────────────

# Attempt 1 — Counter-based key with helper function
class Attempt1:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def get_key(counter: Counter) -> str:
            sorted_items = sorted((item, count) for item, count in counter.items() if count > 0)
            return "|".join(f"{item}:{count}" for item, count in sorted_items)

        counters = [(get_key(Counter(st)), st) for st in strs]
        groups = {}
        for el in counters:
            key, val = el
            if key in groups:
                groups[key].append(val)
            else:
                groups[key] = [val]
        return [value for value in groups.values()]


# Attempt 2 — sorted string as key
class Attempt2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        keys = [(''.join(sorted(st)), st) for st in strs]
        d = {}
        for k in keys:
            key, val = k
            if key in d:
                d[key].append(val)
            else:
                d[key] = [val]
        return [s for s in d.values()]


# Attempt 3 — clean and simple
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for st in strs:
            key = ''.join(sorted(st))
            d.setdefault(key, []).append(st)
        return list(d.values())


# ── Tests ─────────────────────────────────────────────────

tests = {
    "method": "groupAnagrams",
    "cases": [
        {
            "args": [["eat", "tea", "tan", "ate", "nat", "bat"]],
            "expected": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        },
        {"args": [[""]], "expected": [[""]]},
        {"args": [["a"]], "expected": [["a"]]},
    ],
}


def compare(result, expected):
    return sorted(sorted(g) for g in result) == sorted(sorted(g) for g in expected)


# ── Notes ─────────────────────────────────────────────────

"""
Attempt 1 — Overcomplicated

I used Counter to count every letter, then built a custom string key like "a:1|e:1|t:1".
This worked but I wrote a whole helper function (get_key) just to turn a Counter into a string.
I also made an intermediate list of tuples, used an if/else block for grouping, and wrote a pointless list comprehension for the return.

It passed, but it was way more code than needed.

Attempt 2 — Dropped the Counter

I realized that sorting the string itself ("eat" -> "aet") gives me the same unique key as the
Counter approach, without any of the extra machinery. Big simplification. But I still had the unnecessary tuple list,
the if/else grouping, and the redundant list comprehension on return.

Attempt 3 — Clean and Simple

Looped directly over strs instead of building a tuple list first. Replaced the 4-line if/else with setdefault,
which does the same thing in one line. Changed the list comprehension to just list(d.values()). Final solution is
5 lines of actual logic with no imports needed.

Meta Learnings
Before writing a helper function, ask: is there a simpler way to get the same result? Sorting the string directly was
always the answer. I just didn't see it because I jumped to Counter first.

Don't build intermediate data structures you don't need. If you're creating a list just to loop over it right after,
 skip the list and loop directly.

Learn your dictionary tools. setdefault and defaultdict exist so you don't have to write if/else for "add to list or
create new list" every time. This pattern comes up constantly.

A list comprehension that does nothing ([x for x in something]) is just a slow copy. Use list(something) or don't copy at all.

Start simple. My first instinct was to reach for Counter, a helper function, and tuple lists. The best solution was the
 most obvious one: sort the string, use it as a key. Simple beats clever almost every time.

 Refactoring in steps works. I didn't jump from attempt 1 to attempt 3. Each round I removed one layer of unnecessary complexity.
That's a good way to learn — improve one thing at a time so you understand why each change matters.
"""
