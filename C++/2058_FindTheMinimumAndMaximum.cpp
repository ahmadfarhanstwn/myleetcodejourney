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
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        int firstLocal = 0, lastLocal = 0, indexNode = 2, lastValue = head->val;
        head = head->next;
        vector<int> output =  {-1,-1};
        while(head){
            if (head->val < lastValue && head->next && head->val < head->next->val || head->val > lastValue && head->next && head->val > head->next->val){
                if (firstLocal == 0){
                    firstLocal = indexNode;
                } else{
                    output[0] = output[0] != -1 ? min(output[0],indexNode - lastLocal) : indexNode - lastLocal;
                    output[1] = indexNode - firstLocal;
                }
                lastLocal = indexNode;
            }
            indexNode++;
            lastValue = head->val;
            head = head->next;
        }
        return output;
    }
};