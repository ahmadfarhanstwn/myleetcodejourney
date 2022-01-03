class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> s;
        int index = 0;
        for (int i : pushed)
        {
            s.push(i);
            while(!s.empty() && s.top() == popped[index])
            {
                s.pop();
                index++;
            }
        }
        return s.empty();
    }
};