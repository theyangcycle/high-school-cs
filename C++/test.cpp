#include <bits/stdc++.h>
using namespace std;

void myFunc(string name){
    cout<<name;
}

int main()
{
    string name;
    getline(cin,name);
    myFunc(name);
    return 0;
}