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
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) return head;
        int size = 0;
        ListNode* headKw, *tail;
        headKw = tail = head;
        while(head)
        {
            size++;
            if (!head->next && k % size != 0) 
            {
                head->next = headKw;
                break;
            }
            head = head->next;
        }
        int tailIndex = size - (k % size);
        if (tailIndex == size) return headKw;
        for (int i = 1; i <= tailIndex; i++)
        {
            if (i == tailIndex)
            {
                headKw = tail->next;
                tail->next = nullptr;
                break;
            }
            tail = tail->next;
        }
        return headKw;
    }
};