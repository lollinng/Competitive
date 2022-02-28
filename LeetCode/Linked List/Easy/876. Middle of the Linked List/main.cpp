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
    ListNode *middleNode(ListNode *head)
    {
        ListNode *tail = head;
        int length = 0;
        while (tail->next)
        {
            length++;
            tail = tail->next;
        }
        if (length % 2 == 0)
            length = int(length / 2);
        else
            length = int(length / 2 + 1);

        for (int i = 0; i < length; i++)
        {
            head = head->next;
        }
        return head;
    }
};

int main()
{
    Solution s;
    // input  - [1,2,3,4,5,6]
    ListNode *input = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6))))));
    ListNode *ans = s.middleNode(input);
    while (ans)
    {
        cout << ans->val << "\t";
        ans = ans->next;
    }
}