#include <iostream>
#include <vector>
class Solution {
public:
    ListNode* solve(ListNode* head, int k, int len){
				/*  Base Condition */
        if(k > len || head == NULL){
            return head;
        }
		
			/*       reverse K nodes            */
        ListNode* prev = NULL;
        ListNode* curr = head;
        ListNode* nxt;
        int c=0;
        while(curr && c<k){
            nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
            c++;
        }
        head->next = solve(curr, k, len-k);
        return prev;
    }
    
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* temp = head;
        int len=0;
        while(temp){
            len++;
            temp = temp->next;
        }
        return solve(head, k, len);
    }
};
