package Dota2Senate.java;

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public String predictPartyVictory(String senate) {
        Queue<Character> q = new ArrayDeque<Character>();
        int votes[] = new int[256];
        int bans[] = new int[256];
        for (int i = 0; i < senate.length(); i++) {
            q.add(senate.charAt(i));
            votes[senate.charAt(i)]++;
        }
        // Make a logical decision queue loop
        Character decider = ' ';
        while (q.size() > 0) {
            decider = q.remove();
            char opposer = (decider == 'R') ? 'D' : 'R';
            if (bans[decider] > 0) {
                // no right to vote, don't go back in line
                bans[decider]--;
                continue;
            } else if (votes[opposer] == 0) {
                // declare victory
                break;
            } else {
                // ban opposition
                votes[opposer]--;
                bans[opposer]++;
            }
            // Go back in line
            q.add(decider);
        }
        // Last person standing
        return (decider == 'R') ? "Radiant" : "Dire";
    }
}
