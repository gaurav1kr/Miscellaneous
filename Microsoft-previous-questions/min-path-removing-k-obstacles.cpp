class Solution {
public:
    int shortestPath(vector<vector<int>>& grid, int k) 
    {
        //BFS TRAVERSAL
        int m = grid.size();
        int n = grid[0].size();
        
        vector<vector<int>> vis(m,vector<int>(n,-1));
        queue<vector<int>> q;
        q.push({0,0,0,k});
        while(!q.empty())
        {
            vector<int> t = q.front();
            q.pop();
            int i=t[0];
            int j = t[1];
            
            if(i<0 || i>=m || j<0 || j>=n) continue;
            
            if(i==m-1 && j==n-1) return t[2];
            
         if(grid[i][j]==1)
         {
             if(t[3]>0)
             {
                 t[3]--;
             }
             else 
                continue;
         }
        if(vis[i][j]!= -1 && vis[i][j] >=t[3])  
            continue;
        
        vis[i][j] = t[3];
        
        q.push({i+1,j,t[2]+1,t[3]});   // down
        q.push({i-1,j,t[2]+1,t[3]});   // up
        q.push({i,j+1,t[2]+1,t[3]});  // right
        q.push({i,j-1,t[2]+1,t[3]});  // left
         
    }
    return -1; 
  }
};
