class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<int> pq;
        int res = accumulate(begin(piles), end(piles), 0);
        for (int& i : piles)
        {
            pq.push(i);
        }
        while(k > 0)
        {
            auto temp = pq.top(); 
            pq.pop();
            res -= temp/2;
            pq.push((temp+1)/2);
            --k;
        }
        return res;
    }
};