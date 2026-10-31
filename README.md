# LeetCode Solutions in Python

![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)
![Focus](https://img.shields.io/badge/Focus-Data%20Structures%20%26%20Algorithms-334155)
![Status](https://img.shields.io/badge/Status-In%20Progress-2563EB)

A curated collection of my LeetCode solutions in **Python**, with clear explanations of the underlying algorithms, problem-solving strategies, and complexity analysis.

This repository documents how I approach coding challenges: **understand the problem, identify a useful pattern, implement a readable solution, and evaluate its efficiency**.

## Contents

- [Progress](#progress)
- [Solved Problems](#solved-problems)
- [Topics](#topics)
- [Repository Structure](#repository-structure)
- [How I Document Solutions](#how-i-document-solutions)
- [Profiles](#profiles)

## Progress

| Difficulty | Solved |
| :-- | --: |
| Easy | 1 |
| Medium | 0 |
| Hard | 0 |
| **Total** | **1** |

> This table is updated manually as solutions are published. The example in `examples/` is not included in these counts.

## Solved Problems

| # | Problem | Difficulty | Topics | Approach | Solution |
| --: | :-- | :-- | :-- | :-- | :-- |
| 1929 | [Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/) | Easy | Array, Simulation | Preallocated Array | [Explanation](solutions/arrays/p1929_concatenation_of_array/README.md) · [Python](solutions/arrays/p1929_concatenation_of_array/solution.py) |


## Topics

Solutions are organized by their **primary algorithmic pattern**, making it easier to revisit related problems.

| Topic | Directory |
| :-- | :-- |
| Arrays | `solutions/arrays/` |
| Strings | `solutions/strings/` |
| Hash Table | `solutions/hash_table/` |
| Two Pointers | `solutions/two_pointers/` |
| Sliding Window | `solutions/sliding_window/` |
| Stack & Queue | `solutions/stack_queue/` |
| Binary Search | `solutions/binary_search/` |
| Linked List | `solutions/linked_list/` |
| Trees | `solutions/trees/` |
| Graphs | `solutions/graphs/` |
| Backtracking | `solutions/backtracking/` |
| Dynamic Programming | `solutions/dynamic_programming/` |
| Greedy | `solutions/greedy/` |

## Repository Structure

```text
leetcode-python/
├── README.md                       # Portfolio overview and solution index
├── solutions/                      # Your published solutions
│   └── arrays/
│       └── p1929_concatenation_of_array/
│           ├── README.md           # Problem, approach, and complexity
│           └── solution.py         # Python implementation
├── templates/
│   ├── README.md                   # Reusable explanation template
│   └── solution.py                 # Reusable Python template
└── examples/
    └── p0001_two_sum/              # Illustrative example (not counted)
        ├── README.md
        └── solution.py
```

Topic folders under `solutions/` are created as needed.

## How I Document Solutions

Every published problem follows a consistent format:

1. **Problem overview:** A concise summary in my own words, plus the original LeetCode link.
2. **Examples:** Inputs and expected outputs when helpful.
3. **Approach:** The main insight and a step-by-step explanation.
4. **Complexity analysis:** Time and auxiliary space complexity, with reasoning.
5. **Python implementation:** Readable code in a separate `solution.py` file.

Problem directories use the naming convention `pXXXX_problem_name`, where `XXXX` is the zero-padded LeetCode problem number.

A worked example is available at [Two Sum](examples/p0001_two_sum/README.md), and a reusable starting point is available in [templates](templates/README.md).

## Profiles

- **GitHub:** [(https://www.linkedin.com/in/amir-hossein-nazm-bojnordi)]
- **LeetCode:** [(https://leetcode.com/u/amirhosseinnb/))]

---

*Focused on understanding patterns and writing thoughtful solutions—not just collecting accepted submissions.*
