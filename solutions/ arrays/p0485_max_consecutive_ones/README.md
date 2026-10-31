# 485. Max Consecutive Ones

**Difficulty:** Easy  
**Topics:** Array  
**LeetCode:** [View problem](https://leetcode.com/problems/max-consecutive-ones/)

## Problem Summary

Given an array containing only `0`s and `1`s, find the length of its longest uninterrupted sequence of `1`s.

## Examples

**Example 1**

```text
Input:  nums = [1, 1, 0, 1, 1, 1]
Output: 3
```

**Example 2**

```text
Input:  nums = [1, 0, 1, 1, 0, 1]
Output: 2
```

## Approach: Single Pass with a Running Counter

The solution scans the array once, keeping track of the current consecutive run of `1`s and the longest run found so far.

1. Initialize `s = 0` to count the current run and `max = 0` to store the longest run.
2. Iterate over the array from left to right:
   - If the current element is `1`, increment `s`.
   - If the current element is `0`, update `max` when the completed run is at least as long as the previous maximum, then reset `s` to `0`.
3. After the loop, check whether the array ends in `1`. If so, compare the final run with `max` because it was not followed by a `0`.
4. Return `max`.

### Walkthrough

For `nums = [1, 1, 0, 1, 1, 1]`:

| Index | Value | Current run `s` after iteration | Longest run `max` after iteration |
| --: | --: | --: | --: |
| 0 | 1 | 1 | 0 |
| 1 | 1 | 2 | 0 |
| 2 | 0 | 0 | 2 |
| 3 | 1 | 1 | 2 |
| 4 | 1 | 2 | 2 |
| 5 | 1 | 3 | 2 |

The array ends in `1`, so the final check updates `max` to `3`.

```text
Result: 3
```

## Complexity Analysis

Let `n` be the number of elements in `nums`.

- **Time:** `O(n)` — The algorithm processes each element once, with constant-time work per iteration.
- **Auxiliary space:** `O(1)` — Only a fixed number of integer variables are used, regardless of the input size.

## Python Solution

[View the Python implementation](solution.py)

## Key Takeaway

A running counter is enough to identify the longest streak of consecutive values in a single pass. When the last streak reaches the end of the array, it must also be considered before returning the answer.

> **Python style note:** The submitted solution uses `max` as a variable name, which shadows Python's built-in `max()` function. A name such as `max_count` would be clearer in future solutions; the original variable name is kept here to reflect the submitted approach.
