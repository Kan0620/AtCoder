#include <bits/stdc++.h>
using namespace std;
//二分探索木
// NOTE 辞書を使ってうまくできないか考えてみる！
//http://vivi.dyndns.org/tech/cpp/multiset.html
int main(){
    //初期化
    multiset<int> bt;
    //値の追加
    bt.insert(2);
    bt.insert(2);
    bt.insert(3);
    bt.insert(4);
    bt.insert(4);
    //count
    cout << bt.count(3) << endl;
    cout << bt.count(4) << endl;
    
}