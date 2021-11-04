class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        vector<int> a;
        for(int i = 0; i < grid.size();i++){
            for(int j = 0; j < grid[i].size(); j++){
                a.push_back(grid[i][j]);
            }
        }
        sort(a.begin(), a.end());
        int median = a[a.size()/2];
        int output = 0;
        for (int b : a){
            if (abs(b-median)%x == 0){
                output += abs(b-median)/x;
            } else{
                return -1;
            }
        }
        return output;
    }
};