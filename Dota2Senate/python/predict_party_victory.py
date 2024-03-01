from collections import deque
from collections import Counter

def predictPartyVictory(senate: str) -> str:
    q = deque([senator for senator in senate])
    votes = Counter(senate)
    bans = { 'R': 0, 'D': 0 }
    party = None
    while len(q):
        # Next turn
        party = q.popleft()
        opposition = 'D' if party == 'R' else 'R'
        # banned? moving on.
        if bans[party] > 0:
            bans[party] -= 1
            continue
        # victory? announce
        elif votes[opposition] == 0:
            break
        # decide to ban
        else:
            votes[opposition] -= 1
            bans[opposition] += 1
        # Back in line!
        q.append(party)
    return "Radiant" if party == 'R' else "Dire"
