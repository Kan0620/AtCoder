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
    bt.insert(7);
    //count
    cout << bt.count(3) << endl;
    cout << bt.count(4) << endl;
    // 削除
    int c = bt.erase(4);      //  4を全て削除、2 が返ってくる
    // 値の検索
    multiset<int>::iterator itr1 = bt.lower_bound(8);   // 2以上の最初の要素へのイテレータを返す
    cout << *itr1 << endl;
    multiset<int>::iterator itr2 = bt.upper_bound(2);   // 2より大きい最初の要素へのイテレータを返す
    cout << *itr2 << endl;
    
}