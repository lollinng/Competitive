// Dictionary in cpp

#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    unordered_map<string, int> m;

    m["i value for this key"] = 5; // inserting value in dict
    m["2"] = 2;                    // inserting value in dict

    // Built in functions
    m.count("is this key present"); // to check if certain t key is present in the map returns 1 when true
    cout << m["i value for this key"];

    for (auto const &pair : m)
    {
        std::cout << "{" << pair.first << ": " << pair.second << "}\n";
    }
}