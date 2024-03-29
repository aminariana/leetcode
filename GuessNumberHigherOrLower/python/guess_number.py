class Guess:
    def __init__(self, num: int):
        self.pick = num
    
    # The guess API is already defined for you.
    # @param num, your guess
    # @return -1 if num is higher than the picked number
    #          1 if num is lower than the picked number
    #          otherwise return 0
    def guess(self, num: int) -> int:
        return (self.pick > num) - (self.pick < num)

    def guessNumber(self, n: int) -> int:
        low, high = 1, n + 1
        while high > low:
            num = (low + high) // 2
            if self.guess(num) > 0:
                low = num + 1
            else:
                high = num
        return low
