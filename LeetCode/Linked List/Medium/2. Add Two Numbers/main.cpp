/*
We create a linked list to store the addition of the 2 linked list . we loop if we have elements in l1 or l2 or if carry is not 0;
We add values to carry using if statmetns to avoid accessing .val of a null type node of liked list.
then we add remainder of the 10 modulus to ans liked list and send carry for the next loop
*/

#include <iostream>
using namespace std;

// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        int carry = 0;
        ListNode *sum = new ListNode(0);
        ListNode *ans = sum;
        while (l1 || l2 || carry)
        {
            if (l1)
            {
                carry = carry + l1->val;
                l1 = l1->next;
            }
            if (l2)
            {
                carry = carry + l2->val;
                l2 = l2->next;
            }
            sum->next = new ListNode(carry % 10);
            sum = sum->next;
            carry = carry / 10;
        }
        return ans->next;
    }
};

int main()
{
    Solution obj;
    ListNode *l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
    ListNode *l2 = new ListNode(5, new ListNode(6, new ListNode(4)));
    ListNode *ans = obj.addTwoNumbers(l1, l2);
    while (ans)
    {
        cout << ans->val << " ";
        ans = ans->next;
    }
}