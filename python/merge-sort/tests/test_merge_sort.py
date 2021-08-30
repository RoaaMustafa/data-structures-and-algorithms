from merge_sort import __version__

from merge_sort.merge_sort import *

def test_version():
    assert __version__ == '0.1.0'

def test_check_merge_sort():

    arr=[8,4,23,42,16,15]
    Mergesort(arr)

    actual=arr
    expected=[4, 8, 15, 16, 23, 42]

    assert  actual==expected

def test_check_merge_sort_reversed():
  reversed_arr=[20,18,12,8,5,-2]
  Mergesort(reversed_arr)
  actual=reversed_arr
  expected=[-2, 5, 8, 12, 18, 20]

  assert  actual==expected

def test_check_merge_sort_Few_uniques():
        Few_uniques=[5,12,7,5,5,7]
        Mergesort(Few_uniques)
        actual=Few_uniques
        expected=[5, 5, 5, 7, 7, 12]

        assert  actual==expected

def test_unhappy():
    arr=[]
    Mergesort(arr)
    actual=arr
    expected=[]
    assert actual==expected
