# 645. Set Mismatch

**Difficulty:** Easy  
**Topics:** Array, Sorting, Searching  
**LeetCode:** [View problem](https://leetcode.com/problems/set-mismatch/)

## Problem Summary

An array of length `n` should contain each integer from `1` through `n` exactly once. Instead, one value appears twice and another is missing. Find both values and return them in this order: `[duplicate, missing]`.

## Examples

**Example 1**

```text
Input:  nums = [1, 2, 2, 4]
Output: [2, 3]
```

**Example 2**

```text
Input:  nums = [1, 1]
Output: [1, 2]
```

## Approach: Sorting and Linear Search

This solution combines sorting, adjacent-element comparison, and membership checks to find the duplicated and missing numbers.

1. Initialize `miss` and `duplicated` to `0`.
2. Sort `nums` in ascending order so repeated numbers appear next to each other.
3. For each expected value `i` from `1` to `n`:
   - If `i` is a valid array index and `nums[i] == nums[i - 1]`, record that repeated number as `duplicated`.
   - If the expected value `i` is not present in `nums`, record it as `miss`.
4. Return `[duplicated, miss]`.

### Walkthrough

For `nums = [1, 2, 2, 4]`:

- After sorting, the array remains `[1, 2, 2, 4]`.
- At `i = 2`, `nums[2]` and `nums[1]` are both `2`; therefore, `duplicated = 2`.
- At `i = 3`, the value `3` is not found in `nums`; therefore, `miss = 3`.
- The final result is `[2, 3]`.

## Complexity Analysis

Let `n` be the length of `nums`.

- **Time: `O(n²)` worst case** — Sorting takes `O(n log n)`. The loop runs `n` times, and each `i not in nums` membership check can scan up to `n` elements (`O(n)`), giving `O(n²)` overall.
- **Auxiliary space: `O(n)` worst case in CPython** — The algorithm stores only a few integer variables, but Python's built-in list sort (Timsort) may use temporary memory proportional to `n`. This excludes the input and the constant-size returned list.

> **Important:** `nums.sort()` modifies the input list in place. Also, the repeated `i not in nums` checks make this implementation quadratic; using a frequency map or a set could reduce the overall time to `O(n)` with `O(n)` extra space, but the implementation below intentionally preserves the submitted approach.

## Python Solution

[View the Python implementation](solution.py)

## Key Takeaway

Sorting brings duplicate values next to each other, making them easy to identify. However, searching a Python list inside a loop can become expensive: nested linear work leads to quadratic time complexity, even without an explicitly nested `for` loop.
