enum States
{
    plusN,
    plusM,
    minN,
    minM
};

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        vector<std::string> visited;
        int typeState = matrix[0].size() > 1 ? 0 : 1;
        int mSize = matrix.size()-1, nSize = matrix[0].size()-1;
        int end = matrix.size() * matrix[0].size();
        int m = 0, n = 0;
        std::string pair, pairCompare;
        while(res.size() < end)
        {
            res.push_back(matrix[m][n]);
            pair = std::to_string(m) + "," + std::to_string(n);
            visited.push_back(pair);
            switch(typeState)
            {
                case States::plusN:
                    pairCompare = std::to_string(m) + "," + std::to_string(n+2);
                    if(n + 2 > nSize || std::find(visited.begin(), visited.end(), pairCompare) != visited.end())
                    {
                        typeState++;
                    }
                    n++;
                    break;
                case States::plusM:
                    pairCompare = std::to_string(m+2) + "," + std::to_string(n);
                    if(m + 2 > mSize || std::find(visited.begin(), visited.end(), pairCompare) != visited.end())
                    {
                        typeState++;
                    }
                    m++;
                    break;
                case States::minN:
                    pairCompare = std::to_string(m) + "," + std::to_string(n-2);
                    if(n - 2 < 0 || std::find(visited.begin(), visited.end(), pairCompare) != visited.end())
                    {
                        typeState++;
                    }
                    n--;
                    break;
                case States::minM:
                    pairCompare = std::to_string(m-2) + "," + std::to_string(n);
                    if(m - 2 < 0 || std::find(visited.begin(), visited.end(), pairCompare) != visited.end())
                    {
                        typeState = 0;
                    }
                    m--;
                    break;
                default:
                    break;
            }
        }
        return res;
    }
};