class Solution {
public:
    int nthUglyNumber(int n) {
        int two = 0, three = 0, five = 0;
        int nextTwo = 2, nextThree = 3, nextFive = 5;
        int minny = 0;
        vector<int> ugly = {1};
        while(ugly.size() < n)
        {
            minny = min({nextTwo,nextThree,nextFive});
            ugly.push_back(minny);
            if (nextTwo == ugly[ugly.size()-1])
            {
                two++;
                nextTwo = ugly[two] * 2;
            }
            if (nextThree == ugly[ugly.size()-1])
            {
                three++;
                nextThree = ugly[three] * 3;
            }
            if (nextFive == ugly[ugly.size()-1])
            {
                five++;
                nextFive = ugly[five] * 5;
            }
        }
        return ugly[ugly.size()-1];
    }
};