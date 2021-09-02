import pytest
from hashtable import __version__
from hashtable.hash_table import *

def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def hashtable_addition():
    ht=HashTable()
    ht.add("hello",44)
    ht.add("world",55)
    return ht


def test_add():
  ht=HashTable()
  ht.add('ahmad',555)
  assert ht.contains('ahmad')==True

def test_hash():
  ht=HashTable()
  assert  ht.hash("roaa")==885

def test_find(hashtable_addition):
    ht=hashtable_addition
    assert ht.find("hello") == 44
    assert ht.find("world")==55


def test_not_find(hashtable_addition):
    ht=hashtable_addition
    assert ht.find("test") == None

def test_contains(hashtable_addition):
    ht=hashtable_addition
    assert ht.contains("hello")
    assert ht.contains("world")

def test_collision():
    ht=HashTable(3)
    ht.add("roaa",4444)
    ht.add("ro",5555)
    assert ht.find("ro")==5555

def test_collision2(hashtable_addition):
    ht=hashtable_addition
    ht.add("40",44)
    ht.add("31",55)
    assert ht.find("31")==55
