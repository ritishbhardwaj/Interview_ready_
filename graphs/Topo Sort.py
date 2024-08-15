class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        
        vis=[0 for i in range(V)]
        
        def dfs(node,vis,mat,st:list):
            vis[node]=1
            
            for n in mat[node]:
                if not vis[n]:
                    dfs(n,vis,mat,st)
            st.append(node)
            
        
        stack=[]
        for i in range(V):
            if vis[i]==0:
                node=i
                dfs(node,vis,adj,stack)
        
        return stack
    
obj=Solution()
print(obj.topoSort(4,[[],[0],[0],[0]]))
print(obj.topoSort(6,[[],[3],[],[2],[1,0],[2,0]]))
