1470. Shuffle the Array
Difficulty: Easy
Topics: Array, Simulation
LeetCode: View problem
Problem Summary
The input array nums has 2n elements, with the first n elements forming one group and the remaining n elements forming another. Build a new array by alternating elements from the two groups, preserving the order within each group.
Examples
Example 1
Input:  nums = [2, 5, 1, 3, 4, 7], n = 3
Output: [2, 3, 5, 4, 1, 7]
Example 2
Input:  nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4
Output: [1, 4, 2, 3, 3, 2, 4, 1]
Example 3
Input:  nums = [1, 1, 2, 2], n = 2
Output: [1, 2, 1, 2]
Approach: Array Slicing and Interleaving
This solution divides the input into two equal halves and then combines them by taking one element from each half in turn.
1. Create nums1 from the first n elements: nums[0:n].
2. Create nums2 from the last n elements: nums[n:2*n].
3. Initialize an empty result list, res.
4. Loop over indices 0 through n - 1. In each iteration:
   - Append nums1[i].
   - Append nums2[i].
5. Return res.
Walkthrough
Given nums = [2, 5, 1, 3, 4, 7] and n = 3:
nums1 = [2, 5, 1]
nums2 = [3, 4, 7]
i	nums1[i]	nums2[i]	res after iteration
0	2	3	[2, 3]
1	5	4	[2, 3, 5, 4]
2	1	7	[2, 3, 5, 4, 1, 7]


Complexity Analysis
Let n be half the length of the input array.
- Time: O(n) — Creating both slices copies 2n elements in total. The loop runs n times and appends two elements per iteration, for an overall linear runtime.
- Space: O(n) — The slices contain 2n elements in total, and the result contains 2n elements. The extra memory therefore grows linearly with n (including or excluding the output list).
Python Solution
[View the Python implementation](solution.py)
Key Takeaway
Slicing separates the two halves cleanly, and alternating append operations preserves their relative order while producing the required interleaving.
