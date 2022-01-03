class Solution {
public:
    int mod = 1e9 + 7;
    
    long long count(long long a, long long b)
    {
        long long res = 1;
        
        a = a % mod;
        if (a == 0) return 0;
        
        while (b > 0)
        {
            if (b & 1) res = (res*a) % mod;
            
            b = b >> 1;
            a = (a*a) % mod;
        }
        return res;
    }
    
    int countGoodNumbers(long long n) {
        long long five = (n+1)/2;
        long long four = n - five;
        long long res = ((count(5LL,five) % mod * count(4LL,four) % mod) % mod);
        return (int)res;
    }
};