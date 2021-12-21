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
    ListNode* sortList(ListNode* head) {
        if (head == NULL || head->next == NULL) return head;
        
        ListNode* slow = head;
        ListNode* fast = head->next;
        
        while(fast != NULL && fast->next != NULL)
        {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        fast = slow->next;
        slow->next = NULL;
        
        return this->mergeSort(sortList(head),sortList(fast));
    }
    
    ListNode* mergeSort(ListNode* list1, ListNode* list2)
    {
        ListNode dummy(0);
        ListNode* current = &dummy;
        
        while(list1 != NULL && list2 != NULL)
        {
            if (list1->val <= list2->val)
            {
                current->next = list1;
                list1 = list1->next;
            }
            else
            {
                current->next = list2;
                list2 = list2->next;
            }
            
            current = current->next;
        }
        
        if (list1 != NULL)
        {
            current->next = list1;
        }
        else
        {
            current->next = list2;
        }
        
        return dummy.next;
    }
};