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
    ListNode *rotateRight(ListNode *head, int k)
    {
        if (!head || head->next == nullptr)
            return head;

        int length = 1;
        ListNode *tail = head;
        while (tail->next)
        {
            ++length;
            tail = tail->next;
        }

        k = k % length;
        if (k == 0)
            return head;

        ListNode *temp = head;
        for (int i = 0; i < length - k - 1; i++)
        {
            temp = temp->next;
        }
        ListNode *ans = temp->next;
        temp->next = NULL;
        tail->next = head;

        return ans;
    }
};

int main()
{
    Solution obj;
    ListNode *input = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
    ListNode *ans = obj.rotateRight(input, 2);
    while (ans)
    {
        cout << ans->val << "\t";
        ans = ans->next;
    }
}

// Input: head = [1,2,3,4,5], k = 2
// Output: [4,5,1,2,3]