# Count of Smaller Numbers After Self

[![Hard](https://img.shields.io/badge/Difficulty-Hard-Red.svg)](https://github.com/aminariana/leetcode)

You are given an integer array nums and you have to return a new counts array. The counts array has the property where `counts[i]` is the number of smaller elements to the right of `nums[i]`.

**Example:**

```ruby
Input: [5,2,6,1]
Output: [2,1,1,0] 

# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
```

## Solution Explanation

Note that the last element of the expected result is always zero. Working backwards from the input end, each successive element has to divide seen elements into less than or greater than itself (binary search). Build up such a seen set (`sorted` array) and do binarySearch on it. The insert position of each successive item is in fact the count of how many smaller items than it have been seen, which working backwards, correspond to the smaller count on the right of the element.

A corner case is the binarySearch position of an element when duplicate values exist. In case of duplicates, pick the first one (`while` loop corrects for this) because the first of the duplicates has the correct index equaling the count of smaller elements prior to it on `sorted`.

**Example:**

Given: `[5,2,6,1]`
* First, 1 has 0 elements less than it to its right.
* Then, 6 does binary search on [1] and results in insert position 1, i.e. 1 elements less than it.
* Then, 2 does binary search on [1, 6] and results in 1.
* Then, 5 does binary search on [1, 2, 6] and results in insert index 2.
* Insert these indexes each at the head of the output.
Output: [2,1,1,0]