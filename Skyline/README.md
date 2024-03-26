# The Skyline Problem

![Hard](https://img.shields.io/badge/Difficulty-Hard-red)

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

Figure A|Figure B
-|-
![Figure A](skyline1.jpg) | ![Figure B](skyline2.jpg)

#### Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers `[Li, Ri, Hi]`, where `Li` and `Ri` are the x coordinates of the left and right edge of the ith building, respectively, and `Hi` is its height. It is guaranteed that `0 ≤ Li`, `Ri ≤ INT_MAX`, `0 < Hi ≤ INT_MAX`, and `Ri - Li > 0`. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: `[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ]`.

The output is a list of "key points" (red dots in Figure B) in the format of `[ [x1,y1], [x2, y2], [x3, y3], ... ]` that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as: `[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]`.

**Notes:**

- The number of buildings in any input list is guaranteed to be in the range `[0, 10000]`.
- The input list is already sorted in ascending order by the left x position `Li`.
- The output list must be sorted by the x position.
- There must be no consecutive horizontal lines of equal height in the output skyline. For instance, `[...[2 3], [4 5], [7 5], [11 5], [12 7]...]` is not acceptable; the three lines of height 5 should be merged into one in the final output as such: `[...[2 3], [4 5], [12 7], ...]`

## Solution Explanation

First, treat buildings as line-bars along the x-axis (sorting by x implied), where the left of the building is denoted by positive height bars and the right of the building is denoted by negative height. This action simply enables us to visit verticals in order without special backtracking.

Importantly, sort such that heights at the same x value become descending; thus along the sorted bars where they collide on x, we visit the highest bar first. Now along x, pick the highest (first) positive bar as a "climb" dot in skyline; don't override it with lower values.**

Each time a positive bar is encountered, toss its height into the "roofs" max-heap. This heap will be useful when we're jumping down from rooftop to rooftop.

When a negative bar (building right-side ending) is encountered, remove it from the max-heap first. Then look for the max value (i.e. the next rooftop still in play). Pick that height for the drop. If nothing in the heap, that means we drop all the way to zero.

Importantly, if many buildings end on the same x-axis spot, the subsequent drops should happen in-place, so instead of adding to the skyline they should minimize the same drop point.

I have taken certain liberties to reduce the lines of code because I find the less lines of code, the easier it becomes to read and understand.

Code: 20 lines short read.
Complexity: Time O(n log n) Space O(n).

** For those of you familiar with advanced abstractions, using this mapping of data, superimposed height values are now a descreasing monotinic series, which makes them easier to merge using the skyline as the stack.
