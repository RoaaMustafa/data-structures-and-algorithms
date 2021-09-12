from graph.stack_and_queue import *

class Vertex:

      def __init__(self,value):
          self.value=value

      def __str__(self):
         return self.value


class Edge:

  def __init__(self, vertex, weight=1):
    self.vertex=vertex
    self.weight=weight



class Graph:
  def __init__(self):
    self._adjacency_list = {
      # node: [edge1, edge2]
    }

  def __str__(self):
        all_vertex=list(self._adjacency_list.keys())
        strr=""
        for ver in all_vertex:
            strr+=str(ver)+" -> "

        strr += " None"
        return strr

  def add_vertex(self, vertex: Vertex):
    """
    Adds a vertex to the graph

    arguments
    vertex: Vertex

    retrun: added vertex


    """
    self._adjacency_list[f"{vertex}"]=[]
    return vertex


  def add_edges(self, vertex1, vertex2, weight=1):
    """
    Adds an edge to our graph

    """
    all_vertex=list(self._adjacency_list.keys())

    if (vertex1.value in all_vertex) and (vertex2.value in all_vertex):

        edge1=Edge(vertex1,weight)
        self._adjacency_list[f"{vertex2}"].append(edge1)

        # print(edge1.vertex)
        if not (vertex1 == vertex2) :

            edge2=Edge(vertex2,weight)
            self._adjacency_list[f"{vertex1}"].append(edge2)


        # print(edge2.vertex)



  def get_nodes(self):
      try:
        vertices=[]

        def append_tolist(vertex):
            vertices.append(vertex)

        self._breadthFirst(append_tolist)


        return vertices

      except :
          return None



  def size(self):

      counter=0

      def get_size(x):

          nonlocal counter
          counter+=1

      self._breadthFirst(get_size)

      return counter




  def get_neighbors(self,vertex):

    return self._adjacency_list[f'{vertex}']





  def to_adj_list(self):
    return self._adajacency_list




  def _breadthFirst(self, action=lambda x: print(x)):
    """
    Performs a level order traversal of the graph and calls action at each node
    """


    breadth=Queue()
    visited=[]

    vertex=list(self._adjacency_list.keys())[0]
    vertex=Vertex(vertex)
    breadth.enqueue(vertex)

    visited.append(vertex.value)

    while not breadth.is_empty():

        front=breadth.dequeue()
        # print(front)

        action(front.value)

         # call action here
        list_edges=self._adjacency_list[f"{front}"]

        for edge in list_edges:
            if not (edge.vertex.value in  visited):
                # print(edge.vertex)
                visited.append(edge.vertex.value)
                breadth.enqueue(edge.vertex)
    return visited



  def _depthFirst(self, action=lambda x: print(x)):
    """
    Performs a depth first travesal of the graph and calls action at each node
    """
    depthFirst=Stack()
    visited=[]


    vertex=list(self._adjacency_list.keys())[0]
    vertex=Vertex(vertex)
    depthFirst.push(vertex)

    visited.append(vertex.value)


    while not depthFirst.is_empty():
        top=depthFirst.peek()

        action(top.value)

         # call action here
        list_edges=self._adjacency_list[f"{top}"]

        for edge in list_edges:
            if not (edge.vertex.value in  visited):
                # print(edge.vertex)
                visited.append(edge.vertex.value)
                depthFirst.push(edge.vertex)
        depthFirst.pop()




if __name__ == '__main__':

    ver=Vertex('a')
    ver2=Vertex('c')
    ver3=Vertex('d')
    ver4=Vertex('p')

    graph=Graph()
    graph.add_vertex(ver)

    # graph.add_vertex(ver2)
    # graph.add_vertex(ver3)
    # graph.add_vertex(ver4)

    graph.add_edges(ver,ver)
    graph.add_edges(ver,ver3)
    graph.add_edges(ver,ver4)

    # print(len(graph.get_neighbors(ver)))

    # print(graph.size()

    # )
    # print(graph._adjacency_list[f'{ver}'])



    # graph._depthFirst(test)
    print(graph._breadthFirst())
    # print(graph)
