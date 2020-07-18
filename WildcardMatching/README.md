# Wildcard Matching

[![Hard](https://img.shields.io/badge/Difficulty-Hard-Red.svg)](https://github.com/aminariana/leetcode)

Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'`.

```
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
```

The matching should cover the **entire** input string (not partial).

**Note:**
* `s` could be empty and contains only lowercase letters `a-z`.
* `p` could be empty and contains only lowercase letters `a-z`, and characters like `?` or `*`.

**Example 1:**
```
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

**Example 2:**
```
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
```

**Example 3:**
```
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
```

**Example 4:**
```
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
```

**Example 5:**
```
Input:
s = "acdcb"
p = "a*c?b"
Output: false
```

## Solution Explanation
Imagine a DP table with the string characters along the X axis and pattern characters along the Y axis. Importantly, you need extra header row and columns to avoid a whole bunch of if conditions in case you're on the first row or column. For patterns starting with asterisk this is especially useful, because it eliminates the need for reverse tracking. The exact character matches and question mark are simple to evaluate because they depend on previous string and pattern sizes `dp[i-1][j-1]`. For asterisk which is the hard part, we evaluate the current state based on whether the shorter string matched the same tail asterisk pattern, if not we look at whether without the asterisk there's a match (zero char match).

(I spent 3 hours on this problem before introducing the extra header row / col. That was an if-statement hell. Once the extra row + col were introduced, the code became half its size.)