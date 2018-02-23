from pyflatten import flatten
import numpy.random as npr
import numpy as np


def test_flatten():
    val = (npr.randn(10, 2),
           [2.5], (),
           (2.0, [1.0, npr.randn(1, 3)]),
           )
    vect, unflatten = flatten(val)
    val_recovered = unflatten(vect)
    vect_2, _ = flatten(val_recovered)
    assert np.all(vect == vect_2)


def test_flatten_dict():
    val = {'k1': npr.randn(4, 4),
           'k2': npr.randn(3, 3),
           'k3': 3.0,
           'k4': [1.0, 4.0, 7.0, 9.0]}

    vect, unflatten = flatten(val)
    val_recovered = unflatten(vect)
    vect_2, _ = flatten(val_recovered)
    assert np.all(vect == vect_2)
