class Solution {
public:
    int smallestChair(vector<vector<int>>& times, int targetFriend) {
        int target = times[targetFriend][0], smallestUnoccupied = 0;
        sort(times.begin(), times.end());
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        set<int> chairNum;
        for (auto & i : times)
        {
            int currentChair = -1;
            while (!pq.empty() && pq.top().first <= i[0])
            {
                chairNum.insert(pq.top().second);
                pq.pop();
            }
            if (chairNum.empty())
            {
                currentChair = smallestUnoccupied;
                smallestUnoccupied++;
            }
            else
            {
                currentChair = *(chairNum.begin());
                chairNum.erase(currentChair);
            }
            if (i[0] == target) return currentChair;
            pq.push({i[1], currentChair});
        }
        return 0;
    }
};