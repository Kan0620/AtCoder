#include <iostream>
#include <vector>

using namespace std;

struct edge {
    int to, cost;
};

vector<edge> graph[1050];//構造体にて二つの成分を持てるようになった

int main() {

    int a = 2, b = 3, co = 6;//町aから町bに行くときのコストco
    edge e = { b,co };
    graph[a].push_back(e);

    a = 2, b = 4, co = 5;
    edge e0 = { b,co };
    graph[a].push_back(e0);

    a = 1, b = 4, co = 5;
    graph[a].push_back(e0);

    cout << graph[a].size() << endl;

    for (int i = 0; i < graph[a].size(); i++) {
        edge e = graph[a][i];//aからの行き先とaからのコストを取り出せる
        cout << e.to << ' ' << e.cost << endl;
    }
}