class Solution {
public:
    int countBattleships(vector<vector<char>>& board) {
        int res = 0;
        for(int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[i].size(); j++)
            {
                if (board[i][j] == '.') continue;
                else
                {
                    if(j - 1 >= 0 && board[i][j-1] == '.' && i-1 >= 0 && board[i-1][j] == '.' || i-1 < 0 && j-1 < 0 || i-1 < 0 && board[i][j-1] == '.' || j-1 < 0 && board[i-1][j] == '.')
                    {
                        res++;
                    }
                }
            }
        }
        return res;
    }
};