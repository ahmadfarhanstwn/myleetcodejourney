class Solution {
public:
    int countVowelPermutation(int n) {
        const int mod = pow(10, 9)+7;
        long a = 1, e = 1, i = 1, o = 1, u = 1;
        for (int z = 1; z < n; z++){
            long aa = a;
            long ee = e;
            long ii = i;
            long oo = o;
            long uu = u;
            a = (ee + ii + uu) % mod;
            e = (aa + ii) % mod;
            i = (ee + oo) % mod;
            o = ii;
            u = (ii + oo) % mod;
        }
        return (a+e+i+o+u) % mod;
    }
};