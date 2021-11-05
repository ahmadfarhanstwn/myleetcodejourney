class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        unordered_map<int,int> dick;
        int output = 0;
        int product = 0;
        int sum = 0;
        for (int i = 0; i < nums.size();i++){
            for(int j = i+1; j < nums.size();j++){
                product = nums[i] * nums[j];
                if (dick.find(product) == dick.end()){
                    dick[product] = 1;
                } else{
                    dick[product] += 1;
                }
            }
        }
        for (auto key: dick){
            if (key.second > 1){
                sum = key.second - 1;
                while(sum > 0){
                    output += 8 * sum;
                    sum--;
                }
            }
        }
        return output;
    }
};