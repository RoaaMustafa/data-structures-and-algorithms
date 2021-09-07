from hashmap_left_join import __version__
from hashmap_left_join.hashmap_left_join import *
from hashmap_left_join.hashtable import *
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_left_join():
    hash1 = HashTable()
    hash1.add('fond', 'enamored')
    hash1.add('wrath', 'anger')
    hash1.add('diligent', 'employed')
    hash1.add('outfit', 'garb')
    hash1.add('guide', 'usher')

    hash2 = HashTable()
    hash2.add('fond', 'averse')
    hash2.add('wrath', 'delight')
    hash2.add('diligent', 'idle')
    hash2.add('guide', 'follow')
    hash2.add('flow', 'jam')


    assert hashmap_left_join(hash1, hash2) == [['outfit', 'garb', 'Null'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse']]


