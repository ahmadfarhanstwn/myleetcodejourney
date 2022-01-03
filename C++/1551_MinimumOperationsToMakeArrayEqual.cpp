class Solution {
public:
    int minOperations(int n) {
        int res = 0;
        n -= 1;
        while(n > 0)
        {
            res += n;
            n -= 2;
        }
        return res;
    }
};