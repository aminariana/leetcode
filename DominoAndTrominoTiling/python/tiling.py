def numTilings(n: int) -> int:
    # each tuple (x, y) represents x = full tilings, y = broken tilings
    tiling = (1, 0) # for 1-length board 1 full tiling (vertical tile) and none broken
    prev = (1, 0) # for 0-length board 1 full tiling (empty board), and none broken
    for i in range(1, n):
        # the new full tilings for k-length are by:
        # - adding a vetical tile to k-1 full tilings
        # - adding two horizontal tiles to k-2 full tilings
        # - completing k-1 broken tilings by a tromino
        # the new broken tilings for k-length are by:
        # - extending broken k-1 broken tilings by a horizontal tile
        # - extending full k-2 tilings by 2x tromino choices
        prev, tiling = tiling, (tiling[0] + prev[0] + tiling[1], tiling[1] + 2 * prev[0])
        # print(f"{i}: {tiling}")
    return tiling[0] % (pow(10, 9) + 7)
