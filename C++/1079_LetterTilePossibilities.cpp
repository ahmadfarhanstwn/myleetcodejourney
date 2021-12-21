class Solution {
public:
    int numTilePossibilities(string tiles) {
        set<string> per;
        this->permute(per,tiles,"",vector<int>{});
        return per.size();
    }
    
    int permute(set<string>& res, string& tiles, string perm, vector<int> index)
    {
        if (perm.size() > tiles.size())
        {
            return 0;
        }
        else
        {
            for(int i = 0; i < tiles.size(); i++)
            {
                if (std::find(index.begin(), index.end(), i) != index.end())
                {
                    continue;
                }
                else
                {
                    perm += tiles[i];
                    res.insert(perm);
                    index.push_back(i);
                    permute(res, tiles, perm, index);
                    perm.pop_back();
                    index.pop_back();
                }
            }
        }
        return 0;
    }
};