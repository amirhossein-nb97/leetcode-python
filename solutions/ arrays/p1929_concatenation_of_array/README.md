# 1929. Concatenation of Array

**Difficulty:** Easy  
**Topics:** Array, Simulation  
**LeetCode:** [View problem](https://leetcode.com/problems/concatenation-of-array/)

## Problem Summary

Given an integer array `nums` of length `n`, create a new array `ans` of length `2n`. The first `n` positions should contain the original elements, and the next `n` positions should repeat those elements in the same order.

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 1]
Output: [1, 2, 1, 1, 2, 1]
```

**Example 2**

```text
Input:  nums = [1, 3, 2, 1]
Output: [1, 3, 2, 1, 1, 3, 2, 1]
```

## Approach: Preallocated Array and Index Mapping

Instead of using Python's list concatenation operator, this solution constructs the output array explicitly. We allocate an array with twice the input length, then fill **both halves in a single loop**.

1. Set `n` to the length of `nums`.
2. Allocate `ans` with `2 * n` positions.
3. For each index `i` from `0` to `n - 1`:
   - Set `ans[i] = nums[i]` to fill the first half.
   - Set `ans[i + n] = nums[i]` to fill the second half.
4. Return `ans`.

### Walkthrough

For `nums = [1, 2, 1]`, `n = 3` and the new array has six positions:

| `i` | `nums[i]` | First-half position | Second-half position |
| --: | --: | :-- | :-- |
| 0 | 1 | `ans[0] = 1` | `ans[3] = 1` |
| 1 | 2 | `ans[1] = 2` | `ans[4] = 2` |
| 2 | 1 | `ans[2] = 1` | `ans[5] = 1` |

```text
Result: [1, 2, 1, 1, 2, 1]
```

## Complexity Analysis

Let `n` be the length of `nums`.

- **Time:** `O(n)` — Initializing the output array takes `O(n)` time, and the single loop performs two constant-time assignments for each of the `n` elements.
- **Space:** `O(n)` — The new array contains `2n` elements. Excluding the required output array, the algorithm uses `O(1)` auxiliary space.

## Python Solution

[View the Python implementation](solution.py)

## Key Takeaway

Index mapping makes it possible to fill multiple regions of a preallocated array in one pass. The assignment `ans[i + n] = nums[i]` places each value exactly `n` positions after its original location.
