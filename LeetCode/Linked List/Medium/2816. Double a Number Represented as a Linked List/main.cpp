#include <iostream>

using namespace std;

 //Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* doubleIt(ListNode* head) {
        ListNode* curr = head;
        if(curr->val >4){
            head = new ListNode(1,curr);
        }

        while(curr->next != nullptr){
            int carry = 0;
            if (curr-> next -> val >4){
                carry = 1;
            }
            curr-> val = (curr->val*2 %10) + carry;
            curr = curr->next;
        }
        curr->val = (curr->val*2 %10);
        return head;
    }

};

int main(){
    // head = [9,9,9]
    // head = [1,8,9]
   ListNode* head  =  new ListNode(1, new ListNode(8, new ListNode(9)));
   Solution* obj = new Solution();
   ListNode* res = obj->doubleIt(head);
  while (res != nullptr){
      std::cout <<  res->val;
      res = res->next;
  }
  std::cout<<endl;
  ListNode* head1  =  new ListNode(9, new ListNode(9, new ListNode(9)));
  res = obj->doubleIt(head1);
  while (res != nullptr){
      std::cout <<  res->val;
      res = res->next;
      
  }
  
}