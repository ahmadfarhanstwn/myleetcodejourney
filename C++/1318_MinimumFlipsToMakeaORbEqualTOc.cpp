class Solution {
public:
    int minFlips(int a, int b, int c) {
        int res = 0;
        int bitA, bitB, bitC;
        while(a || b || c)
        {
            bitA = a & 1;
            bitB = b & 1;
            bitC = c & 1;
            if ((bitA | bitB) != bitC)
            {
                if (bitA && bitB)
                    res += 2;
                else
                    res++;
            }
            a = a >> 1;
            b = b >> 1;
            c = c >> 1;
        }
        return res;
    }
};