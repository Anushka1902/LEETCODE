#User function Template for python
class Solution:
    def check(self, n, m, e): 
        #code here
        def btrack(s,vis,adj,count,v):
            if count == v:
                return True
            vis[s] = True
            for neighbour in adj[s]:
                if not vis[neighbour] and btrack(neighbour,vis,adj,count + 1,v):
                    return True
            vis[s] = False
            return False
        adj = [[] for i in range(n + 1)]
        v = n
        for edge in e:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        vis = [False] * (v + 1)
        for i in range(1,v):
            if not vis[i] and btrack(i,vis,adj,1,v):
                return True
        return False
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,M = map(int,input().strip().split())
        Edges=[]
        e = list(map(int,input().strip().split()))
        for i in range(M):
            Edges.append([e[2*i],e[2*i+1]])
        ob = Solution()
        if ob.check(N, M, Edges):
            print(1)
        else:
            print(0)
# } Driver Code Ends