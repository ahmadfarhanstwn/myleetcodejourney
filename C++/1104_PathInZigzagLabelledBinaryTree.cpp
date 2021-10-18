class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        int n = 0;
        vector<int> output;
        while (label >= pow(2, n)) n += 1;
        n -= 1;
        while (n >= 0){
            output.push_back(label);
            if (label % 2 == 1) label -= 1;
            label = (pow(2, n)-1) - ((label-(pow(2, n)))/2);
            n -= 1;
        }
        std::reverse(output.begin(),output.end());
        return output;
    }
};