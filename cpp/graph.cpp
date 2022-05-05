#include <bits/stdc++.h>
#include <time.h> 
using namespace std;
#define INF 1000000
//////////////
/* dijkstra */
//////////////

struct edge{
        int to;
        int cost;
    };

int dijkstra(int n_node, vector<edge> edges_dict[INF], int start_node, int goal_node){
    
    typedef pair<int, int> P; //(最短距離, ノードのindex)
    int d[n_node];
    priority_queue<P, vector<P>, greater<P> > que;
    fill(d, d+n_node, INF);
    d[start_node] = 0;
    que.push(P(0, start_node));

    while (!que.empty()){
        P p = que.top();
        que.pop();
        int v = p.second;
        if (d[v] < p.first) continue;
        for (int i=0; i<edges_dict[v].size(); i++){
            edge e = edges_dict[v][i];
            if (d[e.to] > d[v] + e.cost){
                d[e.to] = d[v] + e.cost;
                que.push(P(d[e.to], e.to));
            }
        }
    }
    return d[goal_node];
}

int main(){
    clock_t start = clock();
    int n_node = 7;
    int start_node = 0;
    int goal_node = 3;
    int edges[10][3] = {
            {0, 1, 2},
            {0, 2, 5},
            {1, 2, 4},
            {1, 3, 6},
            {2, 3, 2},
            {1, 4, 1},
            {3, 5, 1},
            {4, 5, 3},
            {4, 6, 5},
            {5, 6, 9}
    };

    vector<edge> edges_dict[n_node];
    for (int i=0; i<sizeof(edges) / sizeof(edges[0]); i++){

        int from_node = edges[i][0];
        int to_node = edges[i][1];
        int cost = edges[i][2];
        edge e;
        e.cost = cost;
        e.to = to_node;
        edges_dict[from_node].push_back(e);
        e.to = from_node;
        edges_dict[to_node].push_back(e);
    }
    
    
    int min_d = dijkstra(n_node, edges_dict, start_node, goal_node);
    cout << min_d << endl;
    clock_t end = clock();
    std::cout << "duration = " << (double)(end - start) / CLOCKS_PER_SEC << "sec.\n";
    return 0;
}