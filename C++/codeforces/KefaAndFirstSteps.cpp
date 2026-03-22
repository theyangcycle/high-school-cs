//include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int n;cin>>n;
    
    vector<int>nums(n);
    for (int _;_<n;_++)
    {
        cin>>nums[_];
    }
    vector<int> counts = {1};
    int id = 0;
    while (id < nums.size()-1)
    {
        int count = 0;
        for (id;id<n;id++)
        {
            try
            {
                if (nums.at(id) <= nums.at(id+1)){count++;}
                else{break;}
            }
            catch (...)
            {
                break;
            }
        }
        id++;
        counts.push_back(count+1);
    }
    
    cout << *max_element(counts.begin(),counts.end());

    return 0;
}