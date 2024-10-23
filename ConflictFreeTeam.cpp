#include <iostream> 
#include <vector> 
#include <algorithm> 
 
using namespace std; 
 
int n, c; 
vector<int> expertise; 
vector<vector<int>> adj; 
vector<bool> visited; 
void dfs(int node, vector<int>& component) { 
    visited[node] = true; 
    component.push_back(node); 
    for (int neighbor : adj[node]) { 
        if (!visited[neighbor]) { 
            dfs(neighbor, component); 
        } 
    } 
} 
 
int main() { 
    cin >> n >> c; 
    adj.resize(n); 
    expertise.resize(n); 
 
    for (int i = 0; i < c; ++i) { 
        int u, v; 
        cin >> u >> v; 
        adj[u - 1].push_back(v - 1); 
        adj[v - 1].push_back(u - 1); 
    } 
 
    for (int i = 0; i < n; ++i) { 
        cin >> expertise[i]; 
    } 
 
    visited.resize(n, false); 
    int max_total_expertise = 0; 
    for (int i = 0; i < n; ++i) { 
        if (!visited[i]) { 
            vector<int> component; 
            dfs(i, component); 
            int component_size = component.size(); 
            int max_expertise_component = 0; 
            int subset_count = 1 << component_size; 
            for (int mask = 0; mask < subset_count; ++mask) { 
                bool conflict = false; 
                int sum_expertise = 0; 
                for (int j = 0; j < component_size; ++j) { 
                    if (mask & (1 << j)) { 
                        sum_expertise += expertise[component[j]]; 
                        for (int k = j + 1; k < component_size; ++k) { 
                            if (mask & (1 << k)) { 
                                if (find(adj[component[j]].begin(), adj[component[j]].end(), component[k]) != adj[component[j]].end()) { 
                                    conflict = true; 
                                    break; 
                                } 
                            } 
                        } 
                    } 
                    if (conflict) break; 
                } 
 
                if (!conflict) { 
                    max_expertise_component = max(max_expertise_component, sum_expertise); 
                } 
            } 
            max_total_expertise += max_expertise_component; 
        } 
    } 
 
    cout << max_total_expertise; 
    return 0; 
}
