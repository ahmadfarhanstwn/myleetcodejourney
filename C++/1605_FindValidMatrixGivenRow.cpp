class Solution {
public:
    vector<vector<int>> restoreMatrix(vector<int>& rowSum, vector<int>& colSum) {
        vector<vector<int>> output;
        vector<int> arrTemp;
        int minny;
        for (int i = 0; i < rowSum.size(); i++){
            arrTemp = {};
            for(int j = 0; j < colSum.size(); j++){
                minny = min(rowSum[i], colSum[j]);
                arrTemp.push_back(minny);
                rowSum[i] -= minny;
                colSum[j] -= minny;
            }
            output.push_back(arrTemp);
        }
        return output;
    }
};