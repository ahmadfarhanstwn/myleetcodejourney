class Solution {
public:
    vector<int> constructArray(int n, int k) {
        int result = 1;
        int distinc = k;
        vector<int> output;
        output.push_back(result);
        while (distinc != 0){
            result += distinc;
            output.push_back(result);
            distinc = distinc > 0 ? (distinc - 1) * -1 : (distinc + 1) * -1; 
        }
        if (output.size() == n) return output;
        for (int i = k + 2; i < n+1; i++){
            output.push_back(i);
        }
        return output;
    }
};