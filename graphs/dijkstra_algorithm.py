from typing import *
from sys import maxsize as mx
import heapq
from queue import PriorityQueue

class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        # Your code here
        pq=PriorityQueue()
        dist=[mx for i in range(len(adj))]
        dist[src]=0
        pq.put((src,0)) #node,dist

        while not pq.empty():
            node,d=pq.get()

            for i in adj[node]:
                nnode=i[0]
                distance=i[1]
                if d+distance<dist[nnode]:
                    dist[nnode]=d+distance
                    pq.put((nnode,dist[nnode]))

        return dist
    
obj=Solution()
V = 3
E = 3
adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
S = 2
print(obj.dijkstra(adj,S))



import atexit
def save_state():
  print("Saving application state...")

def close_file():
    print("Closing file handlers...")


atexit.register(close_file)
atexit.register(save_state)