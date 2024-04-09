from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    unbeaten = []
    for today, temp in enumerate(temperatures):
        while len(unbeaten) and temp > temperatures[unbeaten[-1]]:
            other_day = unbeaten.pop()
            answer[other_day] = today - other_day
        unbeaten.append(today)
    return answer
