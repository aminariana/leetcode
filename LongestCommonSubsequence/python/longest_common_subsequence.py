def longestCommonSubsequence(text1: str, text2: str) -> int:
    # dp[-1] is always 0, hence adding 1 to length
    # _dp is the row before current dp row. We don't need the full 2D DP
    _dp = [0] * (len(text1) + 1)
    dp = _dp.copy()
    # print(f"  - [{', '.join([c for c in text1])}]")
    for row, c2 in enumerate(text2):
        _dp, dp = dp, _dp
        for col, c1 in enumerate(text1):
            if c1 == c2:
                # character match means we can track back at len - 1 of both texts
                dp[col] = _dp[col - 1] + 1
            else:
                # no character match means we can fall back on the best of one of the texts slightly shorter
                dp[col] = max(_dp[col], dp[col-1])
        # print(f"{c2} - {dp}")
    return dp[-2]
