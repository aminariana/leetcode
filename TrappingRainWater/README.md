# Trapping Rain Water

![Hard](https://img.shields.io/badge/Difficulty-Hard-red)

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it is able to trap after raining.

**Example 1:**

![trap](rainwatertrap.png)

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue) are being trapped between blocks (black).
```
**Example 2:**
```
Input: height = [4,2,0,3,2,5]
Output: 9
```

## Solution Hint
1. O(n) time O(1) space
2. Try an accumulator
3. Two opposing indexes