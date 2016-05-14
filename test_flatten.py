from .flattener import flatten
from random import random

import numpy.random as npr
import numpy as np


def rnd_arr(dim0, dim1):
    """
    Returns an 2-dim matrix of random numbers in the shape specified.
    dim0 = number of rows
    dim1 = number of columns
    """
    matrix = []
    for i in range(dim0):
        row = []
        for j in range(dim1):
            row.append(random())
        matrix.append(row)
    return matrix


def test_flatten():
    val = (npr.randn(10, 2),
           [2.5], (),
           (2.0, [1.0, rnd_arr(1, 3)]),
           )
    vect, unflatten = flatten(val)
    val_recovered = unflatten(vect)
    vect_2, _ = flatten(val_recovered)
    assert np.all(vect == vect_2)


def test_flatten_dict():
    val = {'k1':  rnd_arr(4, 4),
           'k2': rnd_arr(3, 3),
           'k3': 3.0,
           'k4': [1.0, 4.0, 7.0, 9.0]}

    vect, unflatten = flatten(val)
    val_recovered = unflatten(vect)
    vect_2, _ = flatten(val_recovered)
    assert np.all(vect == vect_2)
