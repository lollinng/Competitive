#include <iostream>
#include <queue>

using namespace std;

int main()
{
    queue<pair<int, int>> q;
    queue<int> Q;
    q.push({5, 3});
    cout << q.size();
    q.push({53, 32});
    Q.push(3);
    Q.push(5);
    cout << "Queue size before printing the elements: " << Q.size() << endl;
    cout << "Queue element are..." << endl;
    while (!Q.empty())
    {
        cout << " " << Q.front();
        Q.pop();
    }
}