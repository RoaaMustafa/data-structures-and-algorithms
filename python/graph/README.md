# Graphs

A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

## Challenge

Implement a graph, that is represented as an adjacency list, and should include the following methods:

add node add edge get nodes get neighbors size

### Approach & Efficiency

+ Time Complexity: O(N^2)

+ Space Complexity: O(N^2)

## API

Graph Implementation

+ AddNode(): Adds a new node to the graph
Takes in the value of that node
Returns the added node

+ AddEdge(): Adds a new edge between two nodes in the graph
Include the ability to have a “weight”
Takes in the two nodes to be connected by the edge
Both nodes should already be in the Graph

+ GetNodes(): Returns all of the nodes in the graph as a collection (set, list, or similar)

+ GetNeighbors(): Returns a collection of edges connected to the given node
Takes in a given node
Include the weight of the connection in the returned collection

+ Size(): Returns the total number of nodes in the graph


## Graph Breadth First

[link](graph-breadth-first.md)
