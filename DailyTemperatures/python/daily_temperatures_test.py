import random
from DailyTemperatures.python.daily_temperatures import dailyTemperatures

class TestDailyTemperatures:
    def test_basic(self):
        assert [1,1,4,2,1,1,0,0] == dailyTemperatures([73,74,75,71,69,72,76,73])

    def test_sorted_short(self):
        assert [1,1,1,0] == dailyTemperatures([30,40,50,60])

    def test_sorted_longer(self):
        assert [1,1,0] == dailyTemperatures([30,60,90])

    def test_up_down_repeat(self):
        assert [1,1,7,2,1,3,2,1,1,0,0] == dailyTemperatures([73,74,75,71,69,72,70,68,73,76,73])

    def test_spikey(self):
        assert [3,1,1,2,1,1,0,1,1,0] == dailyTemperatures([55,38,53,81,61,93,97,32,43,78])

    def test_record_high_start(self):
        assert [0,1,4,1,2,1,0,1,0,0] == dailyTemperatures([100,65,67,52,63,40,92,44,66,39])

    def test_epic(self):
        n = 100000
        input = [random.randint(30, 100) for _ in range(n)]
        output = dailyTemperatures(input)
        assert n == len(input)
        assert n == len(output)
        assert not all(map(lambda d: d == 0, output))
        for i in range(n):
            assert input[i + output[i]] >= input[i]
