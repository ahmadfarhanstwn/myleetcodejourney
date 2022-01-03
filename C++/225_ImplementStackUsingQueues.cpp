class MyStack {
public:
    queue<int> q;
    int topV, temp;
    
    MyStack() {
        
    }
    
    void push(int x) {
        q.push(x);
        topV = x;
    }
    
    int pop() {
        for (int i = 0; i < q.size()-1; i++)
        {
            temp = q.front();
            topV = q.front();
            q.pop();
            q.push(temp);
        }
        temp = q.front();
        q.pop();
        return temp;
    }
    
    int top() {
        return topV;
    }
    
    bool empty() {
        return q.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */