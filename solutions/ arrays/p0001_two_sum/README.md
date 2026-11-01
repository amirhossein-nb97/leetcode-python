# 1. Two Sum

**Difficulty:** Easy  
**Topics:** Array, Brute Force  
**LeetCode:** [Two Sum](https://leetcode.com/problems/two-sum/)

## Problem Summary

Given an integer array `nums` and a target sum, return the indices of two **different** elements whose values add up to the target. Exactly one valid pair exists, and the indices may be returned in any order.

## Examples

**Example 1**

```text
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
```

**Example 2**

```text
Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]
```

**Example 3**

```text
Input:  nums = [3, 3], target = 6
Output: [0, 1]
```

## Approach: Brute Force (Nested Loops)

This implementation checks pairs of numbers until it finds two values that add up to the target.

1. Create an empty list called `result` to hold the answer's indices.
2. Use the outer loop to select a first index `i`.
3. Use the inner loop to examine each subsequent index `j`, starting at `i + 1`. This avoids pairing an element with itself and avoids checking the same unordered pair twice.
4. When `nums[i] + nums[j] == target`, append both indices to `result` and break out of the inner loop.
5. Return `result` after the outer loop finishes.

### Walkthrough

For `nums = [2, 7, 11, 15]` and `target = 9`:

| First index (`i`) | Second index (`j`) | Sum | Matches target? |
| :--: | :--: | --: | :--: |
| 0 | 1 | 2 + 7 = 9 | Yes |

The matching indices are `[0, 1]`.

## Complexity Analysis

Let `n` be the number of elements in `nums`.

- **Time: `O(n²)` in the worst case.** The nested loops can inspect up to `n(n - 1) / 2` index pairs. Breaking the inner loop after finding the matching pair does not change the worst-case upper bound.
- **Auxiliary space: `O(1)`.** The algorithm uses a fixed number of variables and stores exactly two indices in its result. No additional data structure grows with `n`.

## Implementation Notes

- The use of `range(i + 1, len(nums))` ensures that the same array element is never selected twice.
- The `break` statement exits **only the inner loop**. The outer loop continues, but since the problem guarantees exactly one valid pair, no additional matching indices are appended.
- This solution intentionally retains the author's brute-force approach. A future optimization using a hash map could reduce the time complexity to `O(n)` at the cost of `O(n)` extra space.

## Python Solution

[View the Python implementation](solution.py)

## Key Takeaway

**A nested-loop solution is a clear starting point for pair-search problems.** It is useful for establishing correctness before considering data structures that reduce repeated comparisons.
