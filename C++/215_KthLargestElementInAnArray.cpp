class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::priority_queue<int, std::vector<int>, greater<int>> pq;
        for (auto &i : nums)
        {
            pq.push(i);
            if (pq.size() > k) pq.pop();
        }
        return pq.top();
    }
};