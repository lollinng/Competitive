#include <iostream>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr){};
    ListNode(int x) : val(x), next(nullptr){};
    ListNode(int x, ListNode *next) : val(x), next(next){};
};

int main()
{
    ListNode *x = new ListNode(0);
    ListNode *z = new ListNode(100);
    ListNode *y = new ListNode(10, z);

    x->next = y;
    while (x)
    {
        cout << x->val << "\t";
        x = x->next;
    }

    return 0;
}