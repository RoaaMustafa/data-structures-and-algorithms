from typing import List
from graph import __version__

from graph.graph import *
import pytest
def test_version():
    assert __version__ == '0.1.0'




@pytest.fixture
def date():

    ver=Vertex('a')
    ver2=Vertex('c')
    ver3=Vertex('d')
    ver4=Vertex('p')

    graph=Graph()
    graph.add_vertex(ver)
    graph.add_vertex(ver2)
    graph.add_vertex(ver3)
    graph.add_vertex(ver4)

    graph.add_edges(ver,ver2)
    graph.add_edges(ver,ver3)
    graph.add_edges(ver,ver4)

    return graph

# Node can be successfully added to the graph
def test_node_successfully_added(date):
     vertex=Vertex("z")
     assert date.add_vertex(vertex)




# An edge can be successfully added to the graph
def test_edge_successfully_added(date):

     ver=Vertex('a')
     assert type(date.get_neighbors(ver))==type([])
     assert len(date.get_neighbors(ver))==3


# A collection of all nodes can be properly retrieved from the graph
def test_get_all_node_successfully_added(date):

     assert date.get_nodes()==['a', 'c', 'd', 'p']
     assert len(date.get_nodes())==4


# All appropriate neighbors can be retrieved from the graph
def test_retrieved_neighbors_successfully(date):

     ver=Vertex('c')
     assert type(date.get_neighbors(ver))==type([])
     assert len(date.get_neighbors(ver))==1



# Neighbors are returned with the weight between nodes included
def test_retrieved_neighbors_successfully(date):

     ver=Vertex('c')
     ver2=Vertex('a')
     assert date.get_neighbors(ver)[0].vertex.value==ver2.value
     assert date.get_neighbors(ver)[0].weight==1




# The proper size is returned, representing the number of nodes in the graph
def test_retrieved_size_successfully(date):
     assert date.size()==4




# A graph with only one node and edge can be properly returned
def test_retrieved_onenode_edge_successfully():
    graph=Graph()

    ver=Vertex('a')
    graph.add_vertex(ver)
    graph.add_edges(ver,ver)

    assert len(graph.get_neighbors(ver))==1
    assert graph.add_vertex(ver)


# An empty graph properly returns null
def test_empty_graph():
    graph=Graph()


    assert graph.get_nodes()==None
