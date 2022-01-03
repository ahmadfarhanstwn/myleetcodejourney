class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        unordered_set<string> oMap;
        for (auto& i : obstacles)
            oMap.insert(to_string(i[0]) + "," + to_string(i[1]));
        int dir = 0, res = 0, x = 0, y = 0;
        vector<vector<int>> move = {{0,1},{1,0},{0,-1},{-1,0}};
        for(auto& j : commands)
        {
            if (j == -1)
            {
                dir++;
                if (dir > 3) dir = 0;   
            }
            else if (j == -2)
            {
                dir--;
                if (dir < 0) dir = 3;
            }
            else
            {
                while(j-- > 0)
                {
                    string key = to_string(x+move[dir][0]) + "," + to_string(y+move[dir][1]);
                    if(oMap.find(key)!=oMap.end()) break;
                    x += move[dir][0];
                    y += move[dir][1];
                }
            }
            res = max(res, (x*x) + (y*y));
        }
        return res;
    }
};