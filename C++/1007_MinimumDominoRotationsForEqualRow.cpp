class Solution {
public:
    int minDominoRotations(vector<int>& tops, vector<int>& bottoms) {
        int topTop = 1, bottomBottom = 1, topBottom = 0, bottomTop = 0, topSame = 0, bottomSame = 0, top = tops[0], bottom = bottoms[0];
        for(int i = 1; i < tops.size(); i++){
            if (tops[i] == top && bottoms[i] == top){
                topTop += 1;
                topBottom += 1;
                topSame += 1;
            } else if (tops[i] == top){
                topTop += 1;
            } else if (bottoms[i] == top){
                topBottom += 1;
            }
            if (tops[i] == bottom && bottoms[i] == bottom){
                bottomTop += 1;
                bottomBottom += 1;
                bottomSame += 1;
            } else if (tops[i] == bottom){
                bottomTop += 1;
            } else if (bottoms[i] == bottom){
                bottomBottom += 1;
            }
        }
        if (topTop + topBottom - topSame == bottoms.size() && bottomTop + bottomBottom - bottomSame == bottoms.size()){
            return min({topTop - topSame, topBottom-topSame, bottomTop - bottomSame, bottomBottom - bottomSame});
        }
        else if (topTop + topBottom - topSame == bottoms.size()){
            return min(topTop - topSame, topBottom-topSame);
        } else if (bottomTop + bottomBottom - bottomSame == bottoms.size()){
            return min(bottomTop - bottomSame, bottomBottom - bottomSame);
        } else{
            return -1;
        }
    }
};