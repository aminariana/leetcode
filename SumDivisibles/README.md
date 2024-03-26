# Sum Divisibles

![Medium](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Part 1
Write a function that returns the sum from 0 to integer `n`.
```java
// interface
int SumNaturalNumbers(int n);

// test
Assert.assertEquals(55, SumNaturalNumbers(10));
Assert.assertEquals(4753, SumNaturalNumbers(97));
```

## Part 2
Change the solution to support summing the same range only where elements divide a divider.
```java
// interface
int SumNaturalNumbers(int n, int divider);

// test
Assert.assertEquals(30, SumNaturalNumbers(12, 3));
```

## Part 3
Change the solution to support summing the same range where elements divide any dividers in a given set.
```java
// interface
int SumNaturalNumbers(int n, List<Integer> dividers);

// test
Assert.assertEquals(277038, SumNaturalNumbers(1000, ImmutableList.of(3, 5, 7, 44)));
```

## Solution Explanation
In Part 1 you may offer a trade-off between a for loop and a math hack.

In Part 2 you demonstrate your ability to re-use code instead of rewriting from scratch.

In Part 3 you illustrate through observing the potential to double-count candidates, if you re-use code, that you're flexible enough to rewrite the design from scratch if necessary.