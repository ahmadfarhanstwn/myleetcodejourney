class Solution {
public:
    int minimumLength(string s) {
        int left = 0, right = s.size()-1, output = s.size();
        while (left<right){
            int deletedElements = 0;
            if (s[left] != s[right]){
                return output;
            }
            deletedElements += 2;
            int lefty = left + 1, righty = right - 1;
            while (lefty < right){
                if (s[lefty] != s[left]){
                    break;
                } else{
                    deletedElements += 1;
                    lefty += 1;
                }
            }
            while (righty > lefty){
                if (s[righty] != s[right]){
                    break;
                } else{
                    deletedElements += 1;
                    righty -= 1;
                }
            }
            output -= deletedElements;
            right = righty;
            left = lefty;
        }
        return output;
    }
};