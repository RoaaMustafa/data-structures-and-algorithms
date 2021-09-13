import sys

sys.path.append("/home/roaa/401/data-structures-and-algorithms/python/graph")

from graph.graph import *


def business_trip(graph,arr):
    """
    Determine whether the trip is possible with direct flights, and how much it would cost.
    Args:
        graph (Graph): contains all the list of the cities and its cost
        arr (list): List of the cities
    Return
        tuple : (cost, Bool).
            cost: Total cost for Trip.
            Bool: True or False.
    """

    cost=0
    i=0
    length=len(arr)-1

    def check_cost(city1,city2):
     ''' Calculate the Cost value for the Trip between two City  '''
     neighbors=graph.get_neighbors(city1)
     for city in neighbors:
            if city.vertex.value == city2:
             nonlocal cost , i
             cost += city.weight
             i+=1

            if i == length:
                return
     check_cost(arr[length-i-1],arr[length-i])


    try:
     check_cost(arr[length-1],arr[length])
    except:
     return (bool(cost),cost)

    return (bool(cost),cost)



