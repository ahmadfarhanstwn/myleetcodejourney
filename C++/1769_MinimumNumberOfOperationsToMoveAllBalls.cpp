class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int> output = {0};
        int leftCount = 0, leftSum = 0, rightCount = 0, rightSum = 0;
        for (int i = 1; i < boxes.size();i++){
            if (boxes[i-1] == '1') leftCount+= 1;
            leftSum += leftCount;
            output.push_back(leftSum);
        }
        for (int i = boxes.size()-2; i > -1; i--){
            if (boxes[i+1] == '1') rightCount+= 1;
            rightSum += rightCount;
            output[i] += rightSum;
        }
        return output;
    }
};