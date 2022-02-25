#include <iostream>
using namespace std;

// Definition for singly-linked list.// just for testing
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
    int getDecimalValue(ListNode *head)
    {
        int ans = 0;
        while (head)
        {
            ans = ans * 2 + head->val;
            head = head->next;
        }
        return ans;
    }
};

// just for testing
int main()
{
    Solution s;
    // for a linked list with 101 binary values in diff nodes
    ListNode *head = new ListNode(0, new ListNode(0, new ListNode(1)));
    int ans = s.getDecimalValue(head);
    cout << ans;
}