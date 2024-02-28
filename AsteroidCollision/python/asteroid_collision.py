from typing import List

def asteroidCollision(asteroids: List[int]) -> List[int]:
    results = []
    for a in asteroids:
        # while not empty and on collision course
        while len(results) and a < 0 and results[-1] > 0:
            # if incoming is too small
            if abs(results[-1]) > abs(a): 
                break

            # if pop cancels out
            if results.pop() + a == 0:
                break
        # survived collision conditions
        else:
            results.append(a)
    return results