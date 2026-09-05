# 🚀 USC CS Study - NeetCode 150 & Interview Prep

<div align="center">

![USC CS Study Banner](https://img.shields.io/badge/USC--CS--Study-NeetCode%20150-990000?style=for-the-badge&logo=github)
![Target](https://img.shields.io/badge/Goal-Finish%20NeetCode%20150-FFCC00?style=for-the-badge)
![Pace](https://img.shields.io/badge/Pace-3%20Problems%2FDay-brightgreen?style=for-the-badge)
![Timeline](https://img.shields.io/badge/Duration-Sep%205%20--%20Nov%2010%2C%202026-blue?style=for-the-badge)

**USC Computer Science Algorithm & Technical Interview Study Group**

[Study Page](https://changyulee.oopy.io/3d2d939a-b8c2-8067-a91b-c23334abdccb) • [NeetCode 150 Official](https://neetcode.io/practice) • [Organization](https://github.com/USC-CS-Study)

</div>

---

## 📌 Study Overview & Goals

- **Objective**: Finish all **150 NeetCode problems** systematically before midterms, build algorithmic intuition, and practice live problem-solving under real interview conditions.
- **Daily Pace**: **3 problems per day**, 6 days a week (18 problems/week). Wednesdays are dedicated to live challenge meetups!
- **Total Duration**: 50 study days (September 5, 2026 – November 10, 2026).
- **Difficulty Breakdown**: 28 Easy (19%) • 101 Medium (67%) • 21 Hard (14%) across 18 core categories.
- **After Midterms**: Transition into mock interviews covering **Technical, Behavioral, and System Design** prep together!

---

## 📅 Weekly Schedule & Logistics

### 1. 📖 Daily Practice (Mon, Tue, Thu, Fri, Sat, Sun)
- Solve the **3 designated problems** for the day.
- Push your solutions to your branch and open a PR into `main`.
- Review peers' solutions to compare time/space complexity and idiomatic patterns.

### 2. 🤝 Wednesday Live Meetups (Every Wednesday)
- **Time**: **7:30 PM – 9:30 PM**
- **Location**: **LVL** (USC campus, room TBD weekly)
- **Host**: **Chan** prepares the challenge problem each week.
- **Agenda**:
  - **7:30 – 8:15 PM**: Problem Retrospective — discuss hurdles, alternative approaches, and optimizations from the previous week's problems.
  - **8:15 – 9:00 PM**: **Live Timed Challenge** — solve 1 new, unfamiliar problem under timed interview conditions (problem statement revealed on the spot).
  - **9:00 – 9:30 PM**: Group solution review, complexity analysis, and feedback.

### 3. ☕ Midterm Break
- **Dates**: **October 8, 2026 – October 16, 2026 (inclusive)**.
- **Policy**: No daily problem assignments or Wednesday sessions during this window.
- **Resumption**: Study resumes on **Saturday, October 17, 2026** with **Day 29**.

---

## 🗂️ Repository Structure

```
neetcode-150/
├── problems/                       # 18 Category folders containing all 150 problems
│   ├── 01-arrays-hashing/
│   │   ├── 001-contains-duplicate/
│   │   │   ├── README.md           # Problem details, notes & links
│   │   │   └── <username>.py       # Member submissions
│   │   └── ...
│   ├── 02-two-pointers/
│   └── ... (all 18 categories)
├── wednesday-challenges/           # 8 Wednesday meetup challenge sessions
│   ├── week-01/                    # Week 1 challenge problem & solutions
│   │   ├── README.md
│   │   └── solutions/
│   └── ... (week-01 through week-08)
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md    # Standard PR template
│   └── workflows/
│       └── lint.yml                # CI automation
├── scripts/
│   └── verify_structure.py         # Repo validator
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 How to Submit Solutions

No separate branches are needed! Simply save your code as `<username>.py` inside the corresponding problem folder and push directly to `main`.

### 1. Save Your Solution
Save your solution file inside the corresponding problem folder using your GitHub username:
```
problems/01-arrays-hashing/001-contains-duplicate/<username>.py
problems/01-arrays-hashing/002-valid-anagram/<username>.py
problems/01-arrays-hashing/003-two-sum/<username>.py
```
*(Multi-language solutions are also welcome: `<username>.py`, `<username>.cpp`, `<username>.java`, etc.)*

### 2. Commit & Push
```bash
git add .
git commit -m "feat: solve Day 01 problems (<username>)"
git push origin main
```

---

## 🤝 Wednesday Challenge Sessions (8 Weeks)

| Session | Date | Agenda | Host | Location | Link |
|---|---|---|---|---|---|
| Week 01 | 2026-09-09 (Wed) | Live Challenge #1 + Retrospective | Chan | LVL (TBD) | [View Session](./wednesday-challenges/week-01/) |
| Week 02 | 2026-09-16 (Wed) | Live Challenge #2 + Retrospective | Chan | LVL (TBD) | [View Session](./wednesday-challenges/week-02/) |
| Week 03 | 2026-09-23 (Wed) | Live Challenge #3 + Retrospective | Chan | LVL (TBD) | [View Session](./wednesday-challenges/week-03/) |
| Week 04 | 2026-09-30 (Wed) | Live Challenge #4 + Retrospective | Chan | LVL (TBD) | [View Session](./wednesday-challenges/week-04/) |
| Week 05 | 2026-10-07 (Wed) | Live Challenge #5 + Pre-Midterm Review | Chan | LVL (TBD) | [View Session](./wednesday-challenges/week-05/) |
| *Break* | 2026-10-14 (Wed) | *Midterm Break (No Session)* | - | - | - |
| Week 06 | 2026-10-21 (Wed) | Live Challenge #6 + Post-Break Catchup | Chan | LVL (TBD) | [View Session](./wednesday-challenges/week-06/) |
| Week 07 | 2026-10-28 (Wed) | Live Challenge #7 + Retrospective | Chan | LVL (TBD) | [View Session](./wednesday-challenges/week-07/) |
| Week 08 | 2026-11-04 (Wed) | Live Challenge #8 + Final Prep | Chan | LVL (TBD) | [View Session](./wednesday-challenges/week-08/) |

---

## 📊 50-Day NeetCode 150 Curriculum & Checklist

| Day | Date | # | Problem | Difficulty | Category | NeetCode | Status |
|---|---|---|---|---|---|---|:---:|
| **Day 1** | `2026-09-05` | 001 | [Contains Duplicate](./problems/01-arrays-hashing/001-contains-duplicate) | 🟢 `Easy` | `Arrays & Hashing` | [NeetCode ↗](https://neetcode.io/problems/duplicate-integer/question?list=neetcode150) | [ ] |
|  |  | 002 | [Valid Anagram](./problems/01-arrays-hashing/002-valid-anagram) | 🟢 `Easy` | `Arrays & Hashing` | [NeetCode ↗](https://neetcode.io/problems/is-anagram/question?list=neetcode150) | [ ] |
|  |  | 003 | [Two Sum](./problems/01-arrays-hashing/003-two-sum) | 🟢 `Easy` | `Arrays & Hashing` | [NeetCode ↗](https://neetcode.io/problems/two-integer-sum/question?list=neetcode150) | [ ] |
| **Day 2** | `2026-09-06` | 004 | [Group Anagrams](./problems/01-arrays-hashing/004-group-anagrams) | 🟡 `Medium` | `Arrays & Hashing` | [NeetCode ↗](https://neetcode.io/problems/anagram-groups/question?list=neetcode150) | [ ] |
|  |  | 005 | [Top K Frequent Elements](./problems/01-arrays-hashing/005-top-k-frequent-elements) | 🟡 `Medium` | `Arrays & Hashing` | [NeetCode ↗](https://neetcode.io/problems/top-k-elements-in-list/question?list=neetcode150) | [ ] |
|  |  | 006 | [Encode and Decode Strings](./problems/01-arrays-hashing/006-encode-and-decode-strings) | 🟡 `Medium` | `Arrays & Hashing` | [NeetCode ↗](https://neetcode.io/problems/string-encode-and-decode/question?list=neetcode150) | [ ] |
| **Day 3** | `2026-09-07` | 007 | [Product of Array Except Self](./problems/01-arrays-hashing/007-product-of-array-except-self) | 🟡 `Medium` | `Arrays & Hashing` | [NeetCode ↗](https://neetcode.io/problems/products-of-array-discluding-self/question?list=neetcode150) | [ ] |
|  |  | 008 | [Valid Sudoku](./problems/01-arrays-hashing/008-valid-sudoku) | 🟡 `Medium` | `Arrays & Hashing` | [NeetCode ↗](https://neetcode.io/problems/valid-sudoku/question?list=neetcode150) | [ ] |
|  |  | 009 | [Longest Consecutive Sequence](./problems/01-arrays-hashing/009-longest-consecutive-sequence) | 🟡 `Medium` | `Arrays & Hashing` | [NeetCode ↗](https://neetcode.io/problems/longest-consecutive-sequence/question?list=neetcode150) | [ ] |
| **Day 4** | `2026-09-08` | 010 | [3Sum](./problems/02-two-pointers/010-3sum) | 🟡 `Medium` | `Two Pointers` | [NeetCode ↗](https://neetcode.io/problems/three-integer-sum/question?list=neetcode150) | [ ] |
|  |  | 011 | [Container With Most Water](./problems/02-two-pointers/011-container-with-most-water) | 🟡 `Medium` | `Two Pointers` | [NeetCode ↗](https://neetcode.io/problems/max-water-container/question?list=neetcode150) | [ ] |
|  |  | 012 | [Trapping Rain Water](./problems/02-two-pointers/012-trapping-rain-water) | 🔴 `Hard` | `Two Pointers` | [NeetCode ↗](https://neetcode.io/problems/trapping-rain-water/question?list=neetcode150) | [ ] |
| **Day 5** | `2026-09-10` | 013 | [Two Sum II Input Array Is Sorted](./problems/02-two-pointers/013-two-sum-ii-input-array-is-sorted) | 🟡 `Medium` | `Two Pointers` | [NeetCode ↗](https://neetcode.io/problems/two-integer-sum-ii/question?list=neetcode150) | [ ] |
|  |  | 014 | [Valid Palindrome](./problems/02-two-pointers/014-valid-palindrome) | 🟢 `Easy` | `Two Pointers` | [NeetCode ↗](https://neetcode.io/problems/is-palindrome/question?list=neetcode150) | [ ] |
|  |  | 015 | [Best Time to Buy And Sell Stock](./problems/03-sliding-window/015-best-time-to-buy-and-sell-stock) | 🟢 `Easy` | `Sliding Window` | [NeetCode ↗](https://neetcode.io/problems/buy-and-sell-crypto/question?list=neetcode150) | [ ] |
| **Day 6** | `2026-09-11` | 016 | [Longest Repeating Character Replacement](./problems/03-sliding-window/016-longest-repeating-character-replacement) | 🟡 `Medium` | `Sliding Window` | [NeetCode ↗](https://neetcode.io/problems/longest-repeating-substring-with-replacement/question?list=neetcode150) | [ ] |
|  |  | 017 | [Longest Substring Without Repeating Characters](./problems/03-sliding-window/017-longest-substring-without-repeating-characters) | 🟡 `Medium` | `Sliding Window` | [NeetCode ↗](https://neetcode.io/problems/longest-substring-without-duplicates/question?list=neetcode150) | [ ] |
|  |  | 018 | [Minimum Window Substring](./problems/03-sliding-window/018-minimum-window-substring) | 🔴 `Hard` | `Sliding Window` | [NeetCode ↗](https://neetcode.io/problems/minimum-window-with-characters/question?list=neetcode150) | [ ] |
| **Day 7** | `2026-09-12` | 019 | [Permutation In String](./problems/03-sliding-window/019-permutation-in-string) | 🟡 `Medium` | `Sliding Window` | [NeetCode ↗](https://neetcode.io/problems/permutation-string/question?list=neetcode150) | [ ] |
|  |  | 020 | [Sliding Window Maximum](./problems/03-sliding-window/020-sliding-window-maximum) | 🔴 `Hard` | `Sliding Window` | [NeetCode ↗](https://neetcode.io/problems/sliding-window-maximum/question?list=neetcode150) | [ ] |
|  |  | 021 | [Car Fleet](./problems/04-stack/021-car-fleet) | 🟡 `Medium` | `Stack` | [NeetCode ↗](https://neetcode.io/problems/car-fleet/question?list=neetcode150) | [ ] |
| **Day 8** | `2026-09-13` | 022 | [Daily Temperatures](./problems/04-stack/022-daily-temperatures) | 🟡 `Medium` | `Stack` | [NeetCode ↗](https://neetcode.io/problems/daily-temperatures/question?list=neetcode150) | [ ] |
|  |  | 023 | [Evaluate Reverse Polish Notation](./problems/04-stack/023-evaluate-reverse-polish-notation) | 🟡 `Medium` | `Stack` | [NeetCode ↗](https://neetcode.io/problems/evaluate-reverse-polish-notation/question?list=neetcode150) | [ ] |
|  |  | 024 | [Largest Rectangle In Histogram](./problems/04-stack/024-largest-rectangle-in-histogram) | 🔴 `Hard` | `Stack` | [NeetCode ↗](https://neetcode.io/problems/largest-rectangle-in-histogram/question?list=neetcode150) | [ ] |
| **Day 9** | `2026-09-14` | 025 | [Min Stack](./problems/04-stack/025-min-stack) | 🟡 `Medium` | `Stack` | [NeetCode ↗](https://neetcode.io/problems/minimum-stack/question?list=neetcode150) | [ ] |
|  |  | 026 | [Valid Parentheses](./problems/04-stack/026-valid-parentheses) | 🟢 `Easy` | `Stack` | [NeetCode ↗](https://neetcode.io/problems/validate-parentheses/question?list=neetcode150) | [ ] |
|  |  | 027 | [Binary Search](./problems/05-binary-search/027-binary-search) | 🟢 `Easy` | `Binary Search` | [NeetCode ↗](https://neetcode.io/problems/binary-search/question?list=neetcode150) | [ ] |
| **Day 10** | `2026-09-15` | 028 | [Find Minimum In Rotated Sorted Array](./problems/05-binary-search/028-find-minimum-in-rotated-sorted-array) | 🟡 `Medium` | `Binary Search` | [NeetCode ↗](https://neetcode.io/problems/find-minimum-in-rotated-sorted-array/question?list=neetcode150) | [ ] |
|  |  | 029 | [Koko Eating Bananas](./problems/05-binary-search/029-koko-eating-bananas) | 🟡 `Medium` | `Binary Search` | [NeetCode ↗](https://neetcode.io/problems/eating-bananas/question?list=neetcode150) | [ ] |
|  |  | 030 | [Median of Two Sorted Arrays](./problems/05-binary-search/030-median-of-two-sorted-arrays) | 🔴 `Hard` | `Binary Search` | [NeetCode ↗](https://neetcode.io/problems/median-of-two-sorted-arrays/question?list=neetcode150) | [ ] |
| **Day 11** | `2026-09-17` | 031 | [Search In Rotated Sorted Array](./problems/05-binary-search/031-search-in-rotated-sorted-array) | 🟡 `Medium` | `Binary Search` | [NeetCode ↗](https://neetcode.io/problems/find-target-in-rotated-sorted-array/question?list=neetcode150) | [ ] |
|  |  | 032 | [Search a 2D Matrix](./problems/05-binary-search/032-search-a-2d-matrix) | 🟡 `Medium` | `Binary Search` | [NeetCode ↗](https://neetcode.io/problems/search-2d-matrix/question?list=neetcode150) | [ ] |
|  |  | 033 | [Time Based Key Value Store](./problems/05-binary-search/033-time-based-key-value-store) | 🟡 `Medium` | `Binary Search` | [NeetCode ↗](https://neetcode.io/problems/time-based-key-value-store/question?list=neetcode150) | [ ] |
| **Day 12** | `2026-09-18` | 034 | [Add Two Numbers](./problems/06-linked-list/034-add-two-numbers) | 🟡 `Medium` | `Linked List` | [NeetCode ↗](https://neetcode.io/problems/add-two-numbers/question?list=neetcode150) | [ ] |
|  |  | 035 | [Copy List With Random Pointer](./problems/06-linked-list/035-copy-list-with-random-pointer) | 🟡 `Medium` | `Linked List` | [NeetCode ↗](https://neetcode.io/problems/copy-linked-list-with-random-pointer/question?list=neetcode150) | [ ] |
|  |  | 036 | [Find The Duplicate Number](./problems/06-linked-list/036-find-the-duplicate-number) | 🟡 `Medium` | `Linked List` | [NeetCode ↗](https://neetcode.io/problems/find-duplicate-integer/question?list=neetcode150) | [ ] |
| **Day 13** | `2026-09-19` | 037 | [LRU Cache](./problems/06-linked-list/037-lru-cache) | 🟡 `Medium` | `Linked List` | [NeetCode ↗](https://neetcode.io/problems/lru-cache/question?list=neetcode150) | [ ] |
|  |  | 038 | [Linked List Cycle](./problems/06-linked-list/038-linked-list-cycle) | 🟢 `Easy` | `Linked List` | [NeetCode ↗](https://neetcode.io/problems/linked-list-cycle-detection/question?list=neetcode150) | [ ] |
|  |  | 039 | [Merge K Sorted Lists](./problems/06-linked-list/039-merge-k-sorted-lists) | 🔴 `Hard` | `Linked List` | [NeetCode ↗](https://neetcode.io/problems/merge-k-sorted-linked-lists/question?list=neetcode150) | [ ] |
| **Day 14** | `2026-09-20` | 040 | [Merge Two Sorted Lists](./problems/06-linked-list/040-merge-two-sorted-lists) | 🟢 `Easy` | `Linked List` | [NeetCode ↗](https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=neetcode150) | [ ] |
|  |  | 041 | [Remove Nth Node From End of List](./problems/06-linked-list/041-remove-nth-node-from-end-of-list) | 🟡 `Medium` | `Linked List` | [NeetCode ↗](https://neetcode.io/problems/remove-node-from-end-of-linked-list/question?list=neetcode150) | [ ] |
|  |  | 042 | [Reorder List](./problems/06-linked-list/042-reorder-list) | 🟡 `Medium` | `Linked List` | [NeetCode ↗](https://neetcode.io/problems/reorder-linked-list/question?list=neetcode150) | [ ] |
| **Day 15** | `2026-09-21` | 043 | [Reverse Linked List](./problems/06-linked-list/043-reverse-linked-list) | 🟢 `Easy` | `Linked List` | [NeetCode ↗](https://neetcode.io/problems/reverse-a-linked-list/question?list=neetcode150) | [ ] |
|  |  | 044 | [Reverse Nodes In K Group](./problems/06-linked-list/044-reverse-nodes-in-k-group) | 🔴 `Hard` | `Linked List` | [NeetCode ↗](https://neetcode.io/problems/reverse-nodes-in-k-group/question?list=neetcode150) | [ ] |
|  |  | 045 | [Balanced Binary Tree](./problems/07-trees/045-balanced-binary-tree) | 🟢 `Easy` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/balanced-binary-tree/question?list=neetcode150) | [ ] |
| **Day 16** | `2026-09-22` | 046 | [Binary Tree Level Order Traversal](./problems/07-trees/046-binary-tree-level-order-traversal) | 🟡 `Medium` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/level-order-traversal-of-binary-tree/question?list=neetcode150) | [ ] |
|  |  | 047 | [Binary Tree Maximum Path Sum](./problems/07-trees/047-binary-tree-maximum-path-sum) | 🔴 `Hard` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/binary-tree-maximum-path-sum/question?list=neetcode150) | [ ] |
|  |  | 048 | [Binary Tree Right Side View](./problems/07-trees/048-binary-tree-right-side-view) | 🟡 `Medium` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/binary-tree-right-side-view/question?list=neetcode150) | [ ] |
| **Day 17** | `2026-09-24` | 049 | [Construct Binary Tree From Preorder And Inorder Traversal](./problems/07-trees/049-construct-binary-tree-from-preorder-and-inorder-traversal) | 🟡 `Medium` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/binary-tree-from-preorder-and-inorder-traversal/question?list=neetcode150) | [ ] |
|  |  | 050 | [Count Good Nodes In Binary Tree](./problems/07-trees/050-count-good-nodes-in-binary-tree) | 🟡 `Medium` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/count-good-nodes-in-binary-tree/question?list=neetcode150) | [ ] |
|  |  | 051 | [Diameter of Binary Tree](./problems/07-trees/051-diameter-of-binary-tree) | 🟢 `Easy` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/binary-tree-diameter/question?list=neetcode150) | [ ] |
| **Day 18** | `2026-09-25` | 052 | [Invert Binary Tree](./problems/07-trees/052-invert-binary-tree) | 🟢 `Easy` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/invert-a-binary-tree/question?list=neetcode150) | [ ] |
|  |  | 053 | [Kth Smallest Element In a Bst](./problems/07-trees/053-kth-smallest-element-in-a-bst) | 🟡 `Medium` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/kth-smallest-integer-in-bst/question?list=neetcode150) | [ ] |
|  |  | 054 | [Lowest Common Ancestor of a Binary Search Tree](./problems/07-trees/054-lowest-common-ancestor-of-a-binary-search-tree) | 🟡 `Medium` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree/question?list=neetcode150) | [ ] |
| **Day 19** | `2026-09-26` | 055 | [Maximum Depth of Binary Tree](./problems/07-trees/055-maximum-depth-of-binary-tree) | 🟢 `Easy` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/depth-of-binary-tree/question?list=neetcode150) | [ ] |
|  |  | 056 | [Same Tree](./problems/07-trees/056-same-tree) | 🟢 `Easy` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/same-binary-tree/question?list=neetcode150) | [ ] |
|  |  | 057 | [Serialize And Deserialize Binary Tree](./problems/07-trees/057-serialize-and-deserialize-binary-tree) | 🔴 `Hard` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/serialize-and-deserialize-binary-tree/question?list=neetcode150) | [ ] |
| **Day 20** | `2026-09-27` | 058 | [Subtree of Another Tree](./problems/07-trees/058-subtree-of-another-tree) | 🟢 `Easy` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/subtree-of-a-binary-tree/question?list=neetcode150) | [ ] |
|  |  | 059 | [Validate Binary Search Tree](./problems/07-trees/059-validate-binary-search-tree) | 🟡 `Medium` | `Trees` | [NeetCode ↗](https://neetcode.io/problems/valid-binary-search-tree/question?list=neetcode150) | [ ] |
|  |  | 060 | [Design Twitter](./problems/08-heap-priority-queue/060-design-twitter) | 🟡 `Medium` | `Heap / Priority Queue` | [NeetCode ↗](https://neetcode.io/problems/design-twitter-feed/question?list=neetcode150) | [ ] |
| **Day 21** | `2026-09-28` | 061 | [Find Median From Data Stream](./problems/08-heap-priority-queue/061-find-median-from-data-stream) | 🔴 `Hard` | `Heap / Priority Queue` | [NeetCode ↗](https://neetcode.io/problems/find-median-in-a-data-stream/question?list=neetcode150) | [ ] |
|  |  | 062 | [K Closest Points to Origin](./problems/08-heap-priority-queue/062-k-closest-points-to-origin) | 🟡 `Medium` | `Heap / Priority Queue` | [NeetCode ↗](https://neetcode.io/problems/k-closest-points-to-origin/question?list=neetcode150) | [ ] |
|  |  | 063 | [Kth Largest Element In An Array](./problems/08-heap-priority-queue/063-kth-largest-element-in-an-array) | 🟡 `Medium` | `Heap / Priority Queue` | [NeetCode ↗](https://neetcode.io/problems/kth-largest-element-in-an-array/question?list=neetcode150) | [ ] |
| **Day 22** | `2026-09-29` | 064 | [Kth Largest Element In a Stream](./problems/08-heap-priority-queue/064-kth-largest-element-in-a-stream) | 🟢 `Easy` | `Heap / Priority Queue` | [NeetCode ↗](https://neetcode.io/problems/kth-largest-integer-in-a-stream/question?list=neetcode150) | [ ] |
|  |  | 065 | [Last Stone Weight](./problems/08-heap-priority-queue/065-last-stone-weight) | 🟢 `Easy` | `Heap / Priority Queue` | [NeetCode ↗](https://neetcode.io/problems/last-stone-weight/question?list=neetcode150) | [ ] |
|  |  | 066 | [Task Scheduler](./problems/08-heap-priority-queue/066-task-scheduler) | 🟡 `Medium` | `Heap / Priority Queue` | [NeetCode ↗](https://neetcode.io/problems/task-scheduling/question?list=neetcode150) | [ ] |
| **Day 23** | `2026-10-01` | 067 | [Combination Sum](./problems/09-backtracking/067-combination-sum) | 🟡 `Medium` | `Backtracking` | [NeetCode ↗](https://neetcode.io/problems/combination-target-sum/question?list=neetcode150) | [ ] |
|  |  | 068 | [Combination Sum II](./problems/09-backtracking/068-combination-sum-ii) | 🟡 `Medium` | `Backtracking` | [NeetCode ↗](https://neetcode.io/problems/combination-target-sum-ii/question?list=neetcode150) | [ ] |
|  |  | 069 | [Generate Parentheses](./problems/09-backtracking/069-generate-parentheses) | 🟡 `Medium` | `Backtracking` | [NeetCode ↗](https://neetcode.io/problems/generate-parentheses/question?list=neetcode150) | [ ] |
| **Day 24** | `2026-10-02` | 070 | [Letter Combinations of a Phone Number](./problems/09-backtracking/070-letter-combinations-of-a-phone-number) | 🟡 `Medium` | `Backtracking` | [NeetCode ↗](https://neetcode.io/problems/combinations-of-a-phone-number/question?list=neetcode150) | [ ] |
|  |  | 071 | [N Queens](./problems/09-backtracking/071-n-queens) | 🔴 `Hard` | `Backtracking` | [NeetCode ↗](https://neetcode.io/problems/n-queens/question?list=neetcode150) | [ ] |
|  |  | 072 | [Palindrome Partitioning](./problems/09-backtracking/072-palindrome-partitioning) | 🟡 `Medium` | `Backtracking` | [NeetCode ↗](https://neetcode.io/problems/palindrome-partitioning/question?list=neetcode150) | [ ] |
| **Day 25** | `2026-10-03` | 073 | [Permutations](./problems/09-backtracking/073-permutations) | 🟡 `Medium` | `Backtracking` | [NeetCode ↗](https://neetcode.io/problems/permutations/question?list=neetcode150) | [ ] |
|  |  | 074 | [Subsets](./problems/09-backtracking/074-subsets) | 🟡 `Medium` | `Backtracking` | [NeetCode ↗](https://neetcode.io/problems/subsets/question?list=neetcode150) | [ ] |
|  |  | 075 | [Subsets II](./problems/09-backtracking/075-subsets-ii) | 🟡 `Medium` | `Backtracking` | [NeetCode ↗](https://neetcode.io/problems/subsets-ii/question?list=neetcode150) | [ ] |
| **Day 26** | `2026-10-04` | 076 | [Word Search](./problems/09-backtracking/076-word-search) | 🟡 `Medium` | `Backtracking` | [NeetCode ↗](https://neetcode.io/problems/search-for-word/question?list=neetcode150) | [ ] |
|  |  | 077 | [Implement Trie Prefix Tree](./problems/10-tries/077-implement-trie-prefix-tree) | 🟡 `Medium` | `Tries` | [NeetCode ↗](https://neetcode.io/problems/implement-prefix-tree/question?list=neetcode150) | [ ] |
|  |  | 078 | [Design Add And Search Words Data Structure](./problems/10-tries/078-design-add-and-search-words-data-structure) | 🟡 `Medium` | `Tries` | [NeetCode ↗](https://neetcode.io/problems/design-word-search-data-structure/question?list=neetcode150) | [ ] |
| **Day 27** | `2026-10-05` | 079 | [Word Search II](./problems/10-tries/079-word-search-ii) | 🔴 `Hard` | `Tries` | [NeetCode ↗](https://neetcode.io/problems/search-for-word-ii/question?list=neetcode150) | [ ] |
|  |  | 080 | [Number of Islands](./problems/11-graphs/080-number-of-islands) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/count-number-of-islands/question?list=neetcode150) | [ ] |
|  |  | 081 | [Max Area of Island](./problems/11-graphs/081-max-area-of-island) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/max-area-of-island/question?list=neetcode150) | [ ] |
| **Day 28** | `2026-10-06` | 082 | [Clone Graph](./problems/11-graphs/082-clone-graph) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/clone-graph/question?list=neetcode150) | [ ] |
|  |  | 083 | [Walls And Gates](./problems/11-graphs/083-walls-and-gates) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/islands-and-treasure/question?list=neetcode150) | [ ] |
|  |  | 084 | [Rotting Oranges](./problems/11-graphs/084-rotting-oranges) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/rotting-fruit/question?list=neetcode150) | [ ] |
| **Day 29** | `2026-10-17` | 085 | [Pacific Atlantic Water Flow](./problems/11-graphs/085-pacific-atlantic-water-flow) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/pacific-atlantic-water-flow/question?list=neetcode150) | [ ] |
|  |  | 086 | [Surrounded Regions](./problems/11-graphs/086-surrounded-regions) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/surrounded-regions/question?list=neetcode150) | [ ] |
|  |  | 087 | [Course Schedule](./problems/11-graphs/087-course-schedule) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/course-schedule/question?list=neetcode150) | [ ] |
| **Day 30** | `2026-10-18` | 088 | [Course Schedule II](./problems/11-graphs/088-course-schedule-ii) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/course-schedule-ii/question?list=neetcode150) | [ ] |
|  |  | 089 | [Graph Valid Tree](./problems/11-graphs/089-graph-valid-tree) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/valid-tree/question?list=neetcode150) | [ ] |
|  |  | 090 | [Number of Connected Components In An Undirected Graph](./problems/11-graphs/090-number-of-connected-components-in-an-undirected-graph) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/count-connected-components/question?list=neetcode150) | [ ] |
| **Day 31** | `2026-10-19` | 091 | [Redundant Connection](./problems/11-graphs/091-redundant-connection) | 🟡 `Medium` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/redundant-connection/question?list=neetcode150) | [ ] |
|  |  | 092 | [Word Ladder](./problems/11-graphs/092-word-ladder) | 🔴 `Hard` | `Graphs` | [NeetCode ↗](https://neetcode.io/problems/word-ladder/question?list=neetcode150) | [ ] |
|  |  | 093 | [Network Delay Time](./problems/12-advanced-graphs/093-network-delay-time) | 🟡 `Medium` | `Advanced Graphs` | [NeetCode ↗](https://neetcode.io/problems/network-delay-time/question?list=neetcode150) | [ ] |
| **Day 32** | `2026-10-20` | 094 | [Reconstruct Itinerary](./problems/12-advanced-graphs/094-reconstruct-itinerary) | 🔴 `Hard` | `Advanced Graphs` | [NeetCode ↗](https://neetcode.io/problems/reconstruct-flight-path/question?list=neetcode150) | [ ] |
|  |  | 095 | [Min Cost to Connect All Points](./problems/12-advanced-graphs/095-min-cost-to-connect-all-points) | 🟡 `Medium` | `Advanced Graphs` | [NeetCode ↗](https://neetcode.io/problems/min-cost-to-connect-points/question?list=neetcode150) | [ ] |
|  |  | 096 | [Swim In Rising Water](./problems/12-advanced-graphs/096-swim-in-rising-water) | 🔴 `Hard` | `Advanced Graphs` | [NeetCode ↗](https://neetcode.io/problems/swim-in-rising-water/question?list=neetcode150) | [ ] |
| **Day 33** | `2026-10-22` | 097 | [Alien Dictionary](./problems/12-advanced-graphs/097-alien-dictionary) | 🔴 `Hard` | `Advanced Graphs` | [NeetCode ↗](https://neetcode.io/problems/foreign-dictionary/question?list=neetcode150) | [ ] |
|  |  | 098 | [Cheapest Flights Within K Stops](./problems/12-advanced-graphs/098-cheapest-flights-within-k-stops) | 🟡 `Medium` | `Advanced Graphs` | [NeetCode ↗](https://neetcode.io/problems/cheapest-flight-path/question?list=neetcode150) | [ ] |
|  |  | 099 | [Climbing Stairs](./problems/13-1-d-dynamic-programming/099-climbing-stairs) | 🟢 `Easy` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/climbing-stairs/question?list=neetcode150) | [ ] |
| **Day 34** | `2026-10-23` | 100 | [Min Cost Climbing Stairs](./problems/13-1-d-dynamic-programming/100-min-cost-climbing-stairs) | 🟢 `Easy` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/min-cost-climbing-stairs/question?list=neetcode150) | [ ] |
|  |  | 101 | [House Robber](./problems/13-1-d-dynamic-programming/101-house-robber) | 🟡 `Medium` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/house-robber/question?list=neetcode150) | [ ] |
|  |  | 102 | [House Robber II](./problems/13-1-d-dynamic-programming/102-house-robber-ii) | 🟡 `Medium` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/house-robber-ii/question?list=neetcode150) | [ ] |
| **Day 35** | `2026-10-24` | 103 | [Longest Palindromic Substring](./problems/13-1-d-dynamic-programming/103-longest-palindromic-substring) | 🟡 `Medium` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/longest-palindromic-substring/question?list=neetcode150) | [ ] |
|  |  | 104 | [Palindromic Substrings](./problems/13-1-d-dynamic-programming/104-palindromic-substrings) | 🟡 `Medium` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/palindromic-substrings/question?list=neetcode150) | [ ] |
|  |  | 105 | [Decode Ways](./problems/13-1-d-dynamic-programming/105-decode-ways) | 🟡 `Medium` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/decode-ways/question?list=neetcode150) | [ ] |
| **Day 36** | `2026-10-25` | 106 | [Coin Change](./problems/13-1-d-dynamic-programming/106-coin-change) | 🟡 `Medium` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/coin-change/question?list=neetcode150) | [ ] |
|  |  | 107 | [Maximum Product Subarray](./problems/13-1-d-dynamic-programming/107-maximum-product-subarray) | 🟡 `Medium` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/maximum-product-subarray/question?list=neetcode150) | [ ] |
|  |  | 108 | [Word Break](./problems/13-1-d-dynamic-programming/108-word-break) | 🟡 `Medium` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/word-break/question?list=neetcode150) | [ ] |
| **Day 37** | `2026-10-26` | 109 | [Longest Increasing Subsequence](./problems/13-1-d-dynamic-programming/109-longest-increasing-subsequence) | 🟡 `Medium` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/longest-increasing-subsequence/question?list=neetcode150) | [ ] |
|  |  | 110 | [Partition Equal Subset Sum](./problems/13-1-d-dynamic-programming/110-partition-equal-subset-sum) | 🟡 `Medium` | `1-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/partition-equal-subset-sum/question?list=neetcode150) | [ ] |
|  |  | 111 | [Unique Paths](./problems/14-2-d-dynamic-programming/111-unique-paths) | 🟡 `Medium` | `2-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/count-paths/question?list=neetcode150) | [ ] |
| **Day 38** | `2026-10-27` | 112 | [Longest Common Subsequence](./problems/14-2-d-dynamic-programming/112-longest-common-subsequence) | 🟡 `Medium` | `2-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/longest-common-subsequence/question?list=neetcode150) | [ ] |
|  |  | 113 | [Best Time to Buy And Sell Stock With Cooldown](./problems/14-2-d-dynamic-programming/113-best-time-to-buy-and-sell-stock-with-cooldown) | 🟡 `Medium` | `2-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/buy-and-sell-crypto-with-cooldown/question?list=neetcode150) | [ ] |
|  |  | 114 | [Coin Change II](./problems/14-2-d-dynamic-programming/114-coin-change-ii) | 🟡 `Medium` | `2-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/coin-change-ii/question?list=neetcode150) | [ ] |
| **Day 39** | `2026-10-29` | 115 | [Target Sum](./problems/14-2-d-dynamic-programming/115-target-sum) | 🟡 `Medium` | `2-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/target-sum/question?list=neetcode150) | [ ] |
|  |  | 116 | [Interleaving String](./problems/14-2-d-dynamic-programming/116-interleaving-string) | 🟡 `Medium` | `2-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/interleaving-string/question?list=neetcode150) | [ ] |
|  |  | 117 | [Longest Increasing Path In a Matrix](./problems/14-2-d-dynamic-programming/117-longest-increasing-path-in-a-matrix) | 🔴 `Hard` | `2-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/longest-increasing-path-in-matrix/question?list=neetcode150) | [ ] |
| **Day 40** | `2026-10-30` | 118 | [Distinct Subsequences](./problems/14-2-d-dynamic-programming/118-distinct-subsequences) | 🔴 `Hard` | `2-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/count-subsequences/question?list=neetcode150) | [ ] |
|  |  | 119 | [Edit Distance](./problems/14-2-d-dynamic-programming/119-edit-distance) | 🟡 `Medium` | `2-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/edit-distance/question?list=neetcode150) | [ ] |
|  |  | 120 | [Burst Balloons](./problems/14-2-d-dynamic-programming/120-burst-balloons) | 🔴 `Hard` | `2-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/burst-balloons/question?list=neetcode150) | [ ] |
| **Day 41** | `2026-10-31` | 121 | [Regular Expression Matching](./problems/14-2-d-dynamic-programming/121-regular-expression-matching) | 🔴 `Hard` | `2-D Dynamic Programming` | [NeetCode ↗](https://neetcode.io/problems/regular-expression-matching/question?list=neetcode150) | [ ] |
|  |  | 122 | [Maximum Subarray](./problems/15-greedy/122-maximum-subarray) | 🟡 `Medium` | `Greedy` | [NeetCode ↗](https://neetcode.io/problems/maximum-subarray/question?list=neetcode150) | [ ] |
|  |  | 123 | [Jump Game](./problems/15-greedy/123-jump-game) | 🟡 `Medium` | `Greedy` | [NeetCode ↗](https://neetcode.io/problems/jump-game/question?list=neetcode150) | [ ] |
| **Day 42** | `2026-11-01` | 124 | [Jump Game II](./problems/15-greedy/124-jump-game-ii) | 🟡 `Medium` | `Greedy` | [NeetCode ↗](https://neetcode.io/problems/jump-game-ii/question?list=neetcode150) | [ ] |
|  |  | 125 | [Gas Station](./problems/15-greedy/125-gas-station) | 🟡 `Medium` | `Greedy` | [NeetCode ↗](https://neetcode.io/problems/gas-station/question?list=neetcode150) | [ ] |
|  |  | 126 | [Hand of Straights](./problems/15-greedy/126-hand-of-straights) | 🟡 `Medium` | `Greedy` | [NeetCode ↗](https://neetcode.io/problems/hand-of-straights/question?list=neetcode150) | [ ] |
| **Day 43** | `2026-11-02` | 127 | [Merge Triplets to Form Target Triplet](./problems/15-greedy/127-merge-triplets-to-form-target-triplet) | 🟡 `Medium` | `Greedy` | [NeetCode ↗](https://neetcode.io/problems/merge-triplets-to-form-target/question?list=neetcode150) | [ ] |
|  |  | 128 | [Partition Labels](./problems/15-greedy/128-partition-labels) | 🟡 `Medium` | `Greedy` | [NeetCode ↗](https://neetcode.io/problems/partition-labels/question?list=neetcode150) | [ ] |
|  |  | 129 | [Valid Parenthesis String](./problems/15-greedy/129-valid-parenthesis-string) | 🟡 `Medium` | `Greedy` | [NeetCode ↗](https://neetcode.io/problems/valid-parenthesis-string/question?list=neetcode150) | [ ] |
| **Day 44** | `2026-11-03` | 130 | [Insert Interval](./problems/16-intervals/130-insert-interval) | 🟡 `Medium` | `Intervals` | [NeetCode ↗](https://neetcode.io/problems/insert-new-interval/question?list=neetcode150) | [ ] |
|  |  | 131 | [Merge Intervals](./problems/16-intervals/131-merge-intervals) | 🟡 `Medium` | `Intervals` | [NeetCode ↗](https://neetcode.io/problems/merge-intervals/question?list=neetcode150) | [ ] |
|  |  | 132 | [Non Overlapping Intervals](./problems/16-intervals/132-non-overlapping-intervals) | 🟡 `Medium` | `Intervals` | [NeetCode ↗](https://neetcode.io/problems/non-overlapping-intervals/question?list=neetcode150) | [ ] |
| **Day 45** | `2026-11-05` | 133 | [Meeting Rooms](./problems/16-intervals/133-meeting-rooms) | 🟢 `Easy` | `Intervals` | [NeetCode ↗](https://neetcode.io/problems/meeting-schedule/question?list=neetcode150) | [ ] |
|  |  | 134 | [Meeting Rooms II](./problems/16-intervals/134-meeting-rooms-ii) | 🟡 `Medium` | `Intervals` | [NeetCode ↗](https://neetcode.io/problems/meeting-schedule-ii/question?list=neetcode150) | [ ] |
|  |  | 135 | [Minimum Interval to Include Each Query](./problems/16-intervals/135-minimum-interval-to-include-each-query) | 🔴 `Hard` | `Intervals` | [NeetCode ↗](https://neetcode.io/problems/minimum-interval-including-query/question?list=neetcode150) | [ ] |
| **Day 46** | `2026-11-06` | 136 | [Rotate Image](./problems/17-math-geometry/136-rotate-image) | 🟡 `Medium` | `Math & Geometry` | [NeetCode ↗](https://neetcode.io/problems/rotate-matrix/question?list=neetcode150) | [ ] |
|  |  | 137 | [Spiral Matrix](./problems/17-math-geometry/137-spiral-matrix) | 🟡 `Medium` | `Math & Geometry` | [NeetCode ↗](https://neetcode.io/problems/spiral-matrix/question?list=neetcode150) | [ ] |
|  |  | 138 | [Set Matrix Zeroes](./problems/17-math-geometry/138-set-matrix-zeroes) | 🟡 `Medium` | `Math & Geometry` | [NeetCode ↗](https://neetcode.io/problems/set-zeroes-in-matrix/question?list=neetcode150) | [ ] |
| **Day 47** | `2026-11-07` | 139 | [Happy Number](./problems/17-math-geometry/139-happy-number) | 🟢 `Easy` | `Math & Geometry` | [NeetCode ↗](https://neetcode.io/problems/non-cyclical-number/question?list=neetcode150) | [ ] |
|  |  | 140 | [Plus One](./problems/17-math-geometry/140-plus-one) | 🟢 `Easy` | `Math & Geometry` | [NeetCode ↗](https://neetcode.io/problems/plus-one/question?list=neetcode150) | [ ] |
|  |  | 141 | [Pow(x, n)](./problems/17-math-geometry/141-pow-x-n) | 🟡 `Medium` | `Math & Geometry` | [NeetCode ↗](https://neetcode.io/problems/pow-x-n/question?list=neetcode150) | [ ] |
| **Day 48** | `2026-11-08` | 142 | [Multiply Strings](./problems/17-math-geometry/142-multiply-strings) | 🟡 `Medium` | `Math & Geometry` | [NeetCode ↗](https://neetcode.io/problems/multiply-strings/question?list=neetcode150) | [ ] |
|  |  | 143 | [Detect Squares](./problems/17-math-geometry/143-detect-squares) | 🟡 `Medium` | `Math & Geometry` | [NeetCode ↗](https://neetcode.io/problems/count-squares/question?list=neetcode150) | [ ] |
|  |  | 144 | [Single Number](./problems/18-bit-manipulation/144-single-number) | 🟢 `Easy` | `Bit Manipulation` | [NeetCode ↗](https://neetcode.io/problems/single-number/question?list=neetcode150) | [ ] |
| **Day 49** | `2026-11-09` | 145 | [Number of 1 Bits](./problems/18-bit-manipulation/145-number-of-1-bits) | 🟢 `Easy` | `Bit Manipulation` | [NeetCode ↗](https://neetcode.io/problems/number-of-one-bits/question?list=neetcode150) | [ ] |
|  |  | 146 | [Counting Bits](./problems/18-bit-manipulation/146-counting-bits) | 🟢 `Easy` | `Bit Manipulation` | [NeetCode ↗](https://neetcode.io/problems/counting-bits/question?list=neetcode150) | [ ] |
|  |  | 147 | [Reverse Bits](./problems/18-bit-manipulation/147-reverse-bits) | 🟢 `Easy` | `Bit Manipulation` | [NeetCode ↗](https://neetcode.io/problems/reverse-bits/question?list=neetcode150) | [ ] |
| **Day 50** | `2026-11-10` | 148 | [Missing Number](./problems/18-bit-manipulation/148-missing-number) | 🟢 `Easy` | `Bit Manipulation` | [NeetCode ↗](https://neetcode.io/problems/missing-number/question?list=neetcode150) | [ ] |
|  |  | 149 | [Sum of Two Integers](./problems/18-bit-manipulation/149-sum-of-two-integers) | 🟡 `Medium` | `Bit Manipulation` | [NeetCode ↗](https://neetcode.io/problems/sum-of-two-integers/question?list=neetcode150) | [ ] |
|  |  | 150 | [Reverse Integer](./problems/18-bit-manipulation/150-reverse-integer) | 🟡 `Medium` | `Bit Manipulation` | [NeetCode ↗](https://neetcode.io/problems/reverse-integer/question?list=neetcode150) | [ ] |

---

## 🧭 Post-Midterm Interview Prep Roadmap

Once the 150 problems are completed, our study group will transition into intensive interview rounds:
1. **Technical Mock Interviews**: 45-minute timed peer coding sessions on LeetCode Medium/Hard problems under interview pressure.
2. **Behavioral Questions (STAR Method)**: Leadership, conflict resolution, technical challenges, and story bank refinement.
3. **System Design Fundamentals**: Scalability, caching, distributed systems, SQL vs NoSQL, and end-to-end architecture design.

---

## 📜 License & Acknowledgments

- Problem set curated by [NeetCode](https://neetcode.io/).
- Organized by the **USC CS Study Group**.
- Released under the [MIT License](./LICENSE).
