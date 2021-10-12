class Solution {
public:
    int monotoneIncreasingDigits(int n) {
        string a = to_string(n);
        int sign = a.size();
        for(int i = a.size()-1; i > 0; i--){
            if (a[i] < a[i-1]){
                sign = i;
                a[i-1] = a[i-1] -1; 
            }
        }
        for(int i = sign; i<a.size(); i++) a[i] = '9';
        return stoi(a);
    }
};