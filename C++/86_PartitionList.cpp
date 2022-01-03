/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* left = new ListNode(0),*  right = new ListNode(0),
        *l = left, *r = right, *curr = head;
        
        while(curr)
        {
            if (curr->val < x)
            {
                l->next = curr;
                l = l->next;
            }
            else
            {
                r->next = curr;
                r = r->next;
            }
            curr = curr->next;
        }
        l->next = right->next, r->next = nullptr;
        return left->next;
    }
};