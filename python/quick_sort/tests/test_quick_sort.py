from quick_sort import __version__
from quick_sort.quick_sort import *

def test_version():
    assert __version__ == '0.1.0'


def test_check_quick_sort():

    arr=[8,4,23,42,16,15]
    QuickSort(arr,0,5)

    actual=arr
    expected=[4, 8, 15, 16, 23, 42]

    assert  actual==expected

def test_check_quick_sort_reversed():
  reversed_arr=[20,18,12,8,5,-2]
  QuickSort(reversed_arr,0,5)
  actual=reversed_arr
  expected=[-2, 5, 8, 12, 18, 20]

  assert  actual==expected

def test_check_quick_sort_Few_uniques():
        Few_uniques=[5,12,7,5,5,7]
        QuickSort(Few_uniques,0,5)
        actual=Few_uniques
        expected=[5, 5, 5, 7, 7, 12]

        assert  actual==expected

def test_unhappy():
    arr=[]
    QuickSort(arr,0,0)
    actual=arr
    expected=[]
    assert actual==expected
