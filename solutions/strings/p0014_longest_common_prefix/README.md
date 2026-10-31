# 14. Longest Common Prefix

**Difficulty:** Easy  
**Topics:** String, Prefix Matching  
**LeetCode:** [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

## Problem Summary

Given a non-empty list of strings, find the longest prefix shared by every string. Return an empty string if there is no common prefix.

## Examples

**Example 1**

```text
Input:  strs = ["flower", "flow", "flight"]
Output: "fl"
```

**Example 2**

```text
Input:  strs = ["dog", "racecar", "car"]
Output: ""
```

## Approach: Shortest String + Incremental Prefix Comparison

The solution first finds the **shortest input string**. Since the longest common prefix cannot be longer than the shortest string, this limits the candidate prefixes that need to be checked.

1. Initialize the minimum length with the length of the first string.
2. Scan the strings and keep the index of a shortest string. If two strings tie, the later one is selected.
3. Store that string as the reference, then remove it from `strs` using `pop`.
4. Generate candidate prefixes of the reference string from length `1` to its full length.
5. Compare each candidate against the corresponding prefix of every remaining string. Stop checking a candidate as soon as one comparison fails.
6. Save the longest candidate that matches all remaining strings. For a single input string, return that string.

### Walkthrough

For `strs = ["flower", "flow", "flight"]`, the shortest string is `"flow"`.

| Candidate | Matches `"flower"`? | Matches `"flight"`? | Longest prefix so far |
| :-- | :--: | :--: | :-- |
| `"f"` | Yes | Yes | `"f"` |
| `"fl"` | Yes | Yes | `"fl"` |
| `"flo"` | Yes | No | `"fl"` |
| `"flow"` | Yes | No | `"fl"` |

**Result:** `"fl"`

## Complexity Analysis

Let `m` be the number of strings and `L` be the length of the shortest string.

- **Time: `O(m × L²)` in the worst case when `L ≥ 1`.** Finding the shortest string takes `O(m)` time. For each prefix length `k` from `1` to `L`, up to `m - 1` strings are checked. Creating and comparing slices of length `k` takes `O(k)`, so the total cost is `O(m × (1 + 2 + ... + L)) = O(m × L²)`. When `L = 0`, the loop over prefixes is skipped and the total time is `O(m)`.
- **Auxiliary space: `O(L)`.** Temporary string slices and the saved prefix require up to `O(L)` additional memory. The input list itself is modified, not duplicated.

## Implementation Notes

- Initializing `minString = len(strs[0])` **correctly fixes the previous issue**, which started the minimum length at `0` and did not select the shortest non-empty string.
- `minString` initially holds a number (minimum length) and later a string. Separate names such as `min_length` and `reference_string` would improve readability.
- `strs.pop(index)` **mutates the input list**. Avoiding this side effect is worth considering in future revisions.
- The approach checks all subsequent prefix lengths even after a mismatch; stopping the outer loop at the first mismatch would reduce unnecessary work.
- The Python implementation retains the author's algorithm and variable names, with spacing formatted for readability.

## Python Solution

[View the Python implementation](solution.py)

## Key Takeaway

**The shortest string provides a natural upper bound on any common prefix.** Choosing it first simplifies the search, while careful attention to repeated slicing, early termination, and input mutation can improve the implementation further.
