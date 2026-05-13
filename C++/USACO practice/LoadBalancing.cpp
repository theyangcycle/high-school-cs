#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream read("balancing.in");
    int n; read >> n;
    vector<int> xv;
    vector<int> yv;
    vector<vector<int>> cows;
    vector<int> m;
    for (int i = 0;i<n;i++)
    {
        int x;
        int y;
        read >> x >> y;
        xv.push_back(x);
        yv.push_back(y);
        cows.push_back({x,y});
    }
    set<int> xvals{xv.begin() , xv.end()};
    set<int> yvals{yv.begin() , yv.end()};
    for(int a : xvals)
    {
        for(int b : yvals)
        {
            int bl = 0; int br = 0; int tl = 0; int tr = 0;
            for (vector<int> j : cows)
            {
                if (j[0] < a)
                {
                    if (j[1] < b){bl++;}
                    else {tl++;}
                }
                else if (j[0] > a)
                {
                    if (j[1] < b){br++;}
                    else {tr++;}
                }
            }
            vector<int> elements = {bl,br,tl,tr};
            m.push_back(*max_element(elements.begin(),elements.end()));
        }
    }
    ofstream("balancing.out") << *min_element(m.begin(),m.end()) << endl;
    return 0;
}