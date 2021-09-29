class Solution {
public:
    int minFlips(string target) {
        char initial = '0';
        int output = 0;
        for (int i = 0; i < target.size(); i++){
            if (target[i] != initial){
                output++;
                initial = initial == '1' ? '0' : '1';
            }
        }
        return output;
    }
};