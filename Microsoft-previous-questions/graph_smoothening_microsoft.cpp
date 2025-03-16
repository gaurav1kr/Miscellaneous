#include <vector>
#include <unordered_map>
#include <string>
#include <iostream>

using namespace std;

const int dimensions = 7;

void SmoothGraph(unordered_map<int, pair<string, vector<double>>> &nodes, 
                 unordered_map<int, vector<int>> &edges, 
                 int iterations) 
{
    for (int iter = 0; iter < iterations; iter++) 
    {
        unordered_map<int, vector<double>> new_values;

        for (auto it = nodes.begin(); it != nodes.end(); it++) 
        {
            new_values[it->first] = vector<double>(dimensions, 0.0);
        }

        // Computation logic
        for (auto it = nodes.begin(); it != nodes.end(); ++it) 
        {
            int node = it->first;
            string place_name = it->second.first; 
            vector<double> &properties = it->second.second;
            int num_neighbors = edges[node].size(); 

            double weight = 1.0 / (num_neighbors + 1);

            // Updating for itself (first iteration)
            for (int i = 0; i < dimensions; i++) 
            {
                new_values[node][i] += weight * properties[i];
            }

            // Updating for neighbors
            for (int neighbor : edges[node]) 
            {
                for (int i = 0; i < dimensions; i++) 
                {
                    new_values[node][i] += weight * nodes[neighbor].second[i];
                }
            }
        }

        // Update the original values
        for (auto it = nodes.begin(); it != nodes.end(); ++it) 
        {
            it->second.second = new_values[it->first];
        }
    }
}

int main() 
{
    unordered_map<int, pair<string, vector<double>>> nodes = {
        {1, {"Bengaluru", {1, 1, 0, 1, 0, 0, 0}}},
        {2, {"Mysore", {1, 0, 1, 0, 0, 0, 1}}},
        {3, {"SFO", {0, 1, 0, 1, 0, 0, 0}}} // Fixed duplicate key (was 2, changed to 3)
    };

    unordered_map<int, vector<int>> edges = {
        {1, {2, 3}}, // Fixed incorrect syntax
        {2, {1}}, 
        {3, {1}}
    };

    int iterations = 10;
    SmoothGraph(nodes, edges, iterations);

    // Printing the result
    for (auto &node_data : nodes) 
    {
        int node = node_data.first;
        cout << "Node: " << node << " (" << node_data.second.first << ") -> Values: ";

        for (double val : node_data.second.second) 
        {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}
