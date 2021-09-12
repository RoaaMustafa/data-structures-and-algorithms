from insertion_sort import __version__
from insertion_sort.insertion_sort import *


def test_version():
    assert __version__ == '0.1.0'


def test_insertionsort():

    arr=[7,8,9,0,4,2]
    actual=insertionSort(arr)
    expected=[0, 2, 4, 7, 8, 9]

    assert expected==actual

def test_edge_insertionsort():

    arr=[]
    actual=insertionSort(arr)
    expected=[]

    assert expected==actual

def test_edge_odd_insertionsort():

    arr=[13]
    actual=insertionSort(arr)
    expected=[13]

    assert expected==actual

