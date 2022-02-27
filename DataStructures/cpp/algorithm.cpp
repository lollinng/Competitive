#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    // REVERSE OF A STRING
    string s = "I am Prathamesh";
    reverse(s.begin() + 6, s.begin() + 9);
    cout << s << endl;

    // max
    cout << max(1, 4) << endl;
}