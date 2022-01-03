class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1, right = *max_element(piles.begin(), piles.end());
        while (left < right)
        {
            int mid = (left+right) / 2;
            int total = 0;
            for (auto & i : piles) 
                total += (i + mid - 1) / mid;
            if (total > h) left = mid+1;
            else right = mid;
        }
        return left;
    }
};