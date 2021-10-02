#include <stdio.h>
#include <limits.h>
#define V 9

int distance(int dist[], bool set[])
{
   int min = INT_MAX, index;
   for (int v = 0; v < V; v++)
     if (set[v] == false && dist[v] <= min)
         min = dist[v], index = v;
 
   return index;
}

int print(int dist[])
{
   printf("Vertex   Distance from Source\n");
   for (int i = 0; i < V; i++)
      printf("%d \t\t %d\n", i, dist[i]);
return 0;
}

void dijkstra(int graph[V][V], int src)
{
     int dist[V];
     bool set[V]; 
     for (int i = 0; i < V; i++)
        dist[i] = INT_MAX, set[i] = false;
     dist[src] = 0;
     for (int c = 0; c < V-1; c++)
     {
       int m = distance(dist, set);
       set[m] = true;
       for (int n = 0; n < V;n++)

         if (!set[n] && graph[m][n] && dist[m] != INT_MAX && dist[m]+graph[m][n] < dist[n])
            dist[n] = dist[m] + graph[m][n];
     }
 
     print(dist);
}
 
int main()
{
   int graph[V][V] = {{0, 4, 0, 0, 0, 0, 0, 8, 0},
                      {4, 0, 8, 0, 0, 0, 0, 11, 0},
                      {0, 8, 0, 7, 0, 4, 0, 0, 2},
                      {0, 0, 7, 0, 9, 14, 0, 0, 0},
                      {0, 0, 0, 9, 0, 10, 0, 0, 0},
                      {0, 0, 4, 0, 10, 0, 2, 0, 0},
                      {0, 0, 0, 14, 0, 2, 0, 1, 6},
                      {8, 11, 0, 0, 0, 0, 1, 0, 7},
                      {0, 0, 2, 0, 0, 0, 6, 7, 0}
                     };
 
    dijkstra(graph, 0);
 
    return 0;
}