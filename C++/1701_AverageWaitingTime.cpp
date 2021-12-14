class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        double summy = 0;
        int start = customers[0][0];
        for (vector<int> i : customers){
            start = max(start, i[0]);
            start += i[1];
            summy += start - i[0];
        }
        return summy / customers.size();
    }
};