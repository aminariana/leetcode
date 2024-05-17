# Majority Element

![Easy](https://img.shields.io/badge/Difficulty-Easy-green)

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

 

**Example 1:**
```
Input: nums = [3,2,3]
Output: 3
```
**Example 2:**
```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-10**9 <= nums[i] <= 10**9`


**Follow-up:**

![Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

Could you solve the problem in **linear time and in O(1) space**?

**Hint:**

- What if you ignore collapsed popularity?
- Boyer–Moore majority vote algorithm
