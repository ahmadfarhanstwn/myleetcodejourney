/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public int[] NodesBetweenCriticalPoints(ListNode head) {
        int firstLocal = 0, lastLocal = 0, indexNode = 2, lastValue = head.val;
        head = head.next;
        int[] output = {-1,-1};
        while(head != null){
            if (head.val < lastValue && head.next != null && head.val < head.next.val || head.val > lastValue && head.next != null && head.val > head.next.val){
                if (firstLocal == 0){
                    firstLocal = indexNode;
                } else{
                    output[0] = output[0] != -1? Math.Min(output[0],indexNode - lastLocal) : indexNode - lastLocal;
                    output[1] = indexNode - firstLocal;
                }
                lastLocal = indexNode;
            }
            lastValue = head.val;
            indexNode++;
            head = head.next;
        }
        return output;
    }
}