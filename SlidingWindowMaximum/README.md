# Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

##### Follow up:
Could you solve it in linear time?

##### Example:

```Ruby
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
```

##### Explanation:

```
Window position                Max
--------------------------    -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 ```
 
##### Constraints:

* `1 <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`
* `1 <= k <= nums.length`

## Solution Explanation
A descending monotonic queue is a window of numbers in which each element is less than the previous element. If it isn't, it "eats" the previous element and tracks the deletion count. Thus, in a sliding window, the head of the monotonic sequence is always the max, with a tracker for all the deletes it did to appear as the head.

**Example:** given `[1,2,4,3]`, its monotonic queue is `[[4,2],[3,0]]` meaning 4 ate two elements to become the head, and 3 ate nothing. Looking at the keys, `[4,3]` is monotonically descending.

This is useful, because during construction from the given input, at any given point you can look at the head to get the max. To get the sliding max, you pop the head intelligently; i.e. decrement its deletions if it has any, otherwise pop it.

The trigger to start reading from the head is once the first k elements of the input have been built up. Put the sliding maxes into the result set and voila!