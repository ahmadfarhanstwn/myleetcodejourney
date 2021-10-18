class Solution {
public:
    int minimumDeletions(string s) {
        int output = 0, countB = 0;
        for (char i : s){
            if (i == 'a'){
                output = min(output + 1, countB);
            } else{
                countB++;
            }
        }
        return output;
    }
};