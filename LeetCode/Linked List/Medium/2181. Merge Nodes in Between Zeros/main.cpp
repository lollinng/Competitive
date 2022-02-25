/*
Here we create a linked list sum and refer our ans linked list to it .
If the value of input node is 0 and the 0 isn't last element , we add the node to our sum list and move the sum list to next node .
Otherwise if we encounter a number we adds it value to current sum node
while returning we return ans with 2 next , coz we wanna go to sum node and print the intial 0 value that we used to intialise the sum node

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
    ListNode *mergeNodes(ListNode *head)
    {
        ListNode *sum = new ListNode(0);
        ListNode *ans = new ListNode(0, sum);
        while (head)
        {
            if (head->val == 0 && head->next)
            {
                sum->next = new ListNode(0);
                sum = sum->next;
            }
            else
            {
                sum->val = sum->val + head->val;
            }
            head = head->next;
        }
        return ans->next->next;
    }
};

// for testing
int main()
{
    Solution obj;
    ListNode *input = new ListNode(0, new ListNode(3, new ListNode(1, new ListNode(0, new ListNode(4, new ListNode(5, new ListNode(2, new ListNode(0))))))));
    ListNode *ans = obj.mergeNodes(input);
    while (ans)
    {
        cout << ans->val << "\t";
        ans = ans->next;
    }
}