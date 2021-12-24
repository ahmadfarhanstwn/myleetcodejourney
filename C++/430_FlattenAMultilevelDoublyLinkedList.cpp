/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        stack<Node*> s;
        if(head) s.push(head);
        while(!s.empty())
        {
            Node* node = s.top();
            s.pop();
            if (node->child)
            {
                if(node->next)
                {
                    node->next->prev = NULL;
                    s.push(node->next);
                }
                node->next = node->child;
                node->child->prev = node;
                node->child = NULL;
                s.push(node->next);
            }
            else if (!node->next)
            {
                if (!s.empty())
                {
                    Node* next = s.top();
                    node->next = next;
                    next->prev = node;
                }
            }
            else
            {
                s.push(node->next);
            }
        }
        return head;
    }
};