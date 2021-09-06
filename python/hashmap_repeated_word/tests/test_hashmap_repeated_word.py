from hashmap_repeated_word import __version__
from hashmap_repeated_word.hashtable import HashTable
from hashmap_repeated_word.linked_list import *
from hashmap_repeated_word.hashmap_repeated_word import *
import re

def test_version():
    assert __version__ == '0.1.0'


def test_repeated_Word():
    assert repeated_word("welcome to jordan and welcome again")[0]== "welcome"

def test_number_of_word_in_string():
    test=HashTable()
    assert repeated_word("welcome to jordan and welcome again")[1]== 6

def test_no_repeated_Word():
    test=HashTable()
    assert repeated_word("welcome to jordan and  again")== "None"


def test_empty_string():
    test=HashTable()
    assert repeated_word("")== "None"
