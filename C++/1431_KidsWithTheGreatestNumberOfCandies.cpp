class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maks = *max_element(candies.begin(), candies.end());
        vector<bool> res;
        for (int & i : candies)
        {
            if (i + extraCandies >= maks) res.push_back(true);
            else res.push_back(false);
        }
        return res;
    }
};