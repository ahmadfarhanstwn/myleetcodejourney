class Solution {
public:
    bool isRobotBounded(string instructions) {
        int x = 0, y = 0, i = 0;
        vector<vector<int>> d = {{0,1},{1,0},{0,-1},{-1,0}};
        for (char ins : instructions){
            if (ins == 'G'){
                x += d[i][0];
                y += d[i][1];
            } else if (ins == 'L'){
                i = (i + 3) % 4;
            } else{
                i = (i + 1) % 4;
            }
        }
        return x == 0 && y == 0 || i != 0;
    }
};