/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == NULL)
            return l2;
        if (l2 == NULL)
            return l1;
        ListNode* curr1 = l1;
        ListNode* curr2 = l2;
        ListNode* head = NULL;
        ListNode* tail = NULL;
        while(curr1 && curr2){
            if(curr1->val<curr2->val){
                if(!head){
                    head = curr1;
                    tail = curr1;
                }
                else{
                    tail->next = curr1;
                    tail = curr1;
                }
                curr1 = curr1->next;
            }
            else{
                if(!head){
                    head = curr2;
                    tail = curr2;
                }
                else{
                    tail->next = curr2;
                    tail = curr2;
                }
                curr2 = curr2->next;
            }
        }
        if(curr1)
            tail->next = curr1;
        if(curr2)
            tail->next = curr2;
        return head;
    }
};