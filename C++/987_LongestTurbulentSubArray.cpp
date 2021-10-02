class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        if (arr.size() == 1){
            return 1;
        }
        bool moreThan = arr[0] > arr[1];
        int output = 0;
        int subArray = (arr[1] != arr[0]) ? 2 : 1;
        for (int i = 1; i < (arr.size()-1); i++){
            if (moreThan){
                if (arr[i] < arr[i+1]){
                    subArray++;
                    moreThan = false;
                } else if (arr[i] > arr[i+1]){
                    output = max(output, subArray);
                    subArray = 2;
                } else{
                    output = max(output, subArray);
                    subArray = 1;
                }
            } else{
                if (arr[i] > arr[i+1]){
                    subArray++;
                    moreThan = true;
                } else if (arr[i] < arr[i+1]){
                    output = max(output, subArray);
                    subArray = 2;
                } else{
                    output = max(output, subArray);
                    subArray = 1;
                }
            }
        }
        output = max(output,subArray);
        return output;
    }
};