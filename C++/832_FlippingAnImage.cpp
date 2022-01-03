class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        int left, right;
        for (int i = 0; i < image.size();i++)
        {
            left = 0; 
            right = image.size()-1;
            while(left <= right)
            {
                swap(image[i][left], image[i][right]);
                image[i][left] = image[i][left] ? 0 : 1;
                if (left != right) image[i][right] = image[i][right] ? 0 : 1;
                left++;
                right--;
            }
        }
        return image;
    }
};