#include <bits/stdc++.h>
using namespace std;
//cppの基本 参考↓
//https://somachob.com/basic-cpp/#toc2

int main(){
    string a;
    vector<int>  v;
    v.push_back(0);
    cout << v[0] << endl;
    
    pair<int, string> p;
    p = make_pair(1, "one");
    p.first = 100;
    cout << p.first << endl;  // 100
    cout << p.second << endl; // one
    
    //値の受け取り
    

    //複数
    /*
    for (int i=0; i<3; i++){
        cin >> v[i];
    }
    */
    
    //ソート
    /*
    sort(v.begin(), v.end());
    reverse(v.begin(), v.end());
    */

    //配列の重複削除
    /*
    v.erase(unique(v.begin(), v.end()), v.end());
    */




    cout << a << endl;
    cout << v[1] << endl;

    cout << "jjj" << endl;

    vector<int> G[3];
    int s = 1;
    int t = 2;

    // G[s].push_back(t);
    // for (int i=0; i<G.size(); i++){
    //     cout << G[i] << endl;
    // }




}
