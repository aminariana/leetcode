package NumberOfRecentCalls.java;

import java.util.ArrayDeque;
import java.util.Queue;

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */
class RecentCounter {
    private Queue<Integer> q;

    public RecentCounter() {
        this.q = new ArrayDeque<Integer>();
    }
    
    public int ping(int t) {
        while(this.q.size() > 0 && this.q.peek() < t - 3000) {
            this.q.remove();
        }
        this.q.add(t);
        return this.q.size();
    }
}
