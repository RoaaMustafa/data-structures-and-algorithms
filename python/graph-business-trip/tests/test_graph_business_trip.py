from graph_business_trip import __version__
from graph_business_trip.graph_business_trip import *
import pytest


def test_version():
    assert __version__ == '0.1.0'




@pytest.fixture
def data():
    ver=Vertex('Metroville')
    ver2=Vertex('Pandora')
    ver3=Vertex('Arendelle')
    ver4=Vertex('Monstropolis')
    ver5=Vertex('Naboo')
    graph=Graph()
    graph.add_vertex(ver)
    graph.add_vertex(ver2)
    graph.add_vertex(ver3)
    graph.add_vertex(ver4)
    graph.add_vertex(ver5)
    graph.add_edges(ver,ver2,50)
    graph.add_edges(ver3,ver4,150)
    graph.add_edges(ver5,ver4,250)
    return graph


def test_correct_cost(data):
    graph=data
    arr=['Arendelle','Monstropolis', 'Naboo']
    assert business_trip(graph,arr) == (True,400)

    
def test_unable_to_trip():
    graph=data
    arr=['Arendelle','Amman', 'Naboo']
    assert business_trip(graph,arr) == (False,0)
def test_not_connected_city():
    graph=data
    arr=['Arendelle','Monstropolis', 'Metroville']
    assert business_trip(graph,arr) == (False,0)
def test_empty_list_city():
    graph=data
    arr=[]
    assert business_trip(graph,arr) == (False,0)
