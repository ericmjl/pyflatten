"""
Authors: David K. Duvenaud, Dougal MacLaurin, Matt J. Johnson (Harvard
Intelligent & Probabilistic Systems Group)

Packaged by: Eric J. Ma (MIT)
"""
import numpy as np
from operator import itemgetter


def flatten(value):
    """value can be any nesting of tuples, arrays, dicts.
       returns 1D numpy array and an unflatten function."""
    if isinstance(value, np.ndarray):
        def unflatten(vector):
            return np.reshape(vector, value.shape)
        return np.ravel(value), unflatten

    elif isinstance(value, float):
        return np.array([value]), lambda x: x[0]

    elif isinstance(value, tuple):
        if not value:
            return np.array([]), lambda x: ()

        flattened_first, unflatten_first = flatten(value[0])
        flattened_rest, unflatten_rest = flatten(value[1:])

        def unflatten(vector):
            N = len(flattened_first)
            return (unflatten_first(vector[:N]),) + unflatten_rest(vector[N:])

        return np.concatenate((flattened_first, flattened_rest)), unflatten

    elif isinstance(value, list):
        if not value:
            return np.array([]), lambda x: []
        flattened_first, unflatten_first = flatten(value[0])
        flattened_rest, unflatten_rest = flatten(value[1:])

        def unflatten(vector):
            N = len(flattened_first)
            return [unflatten_first(vector[:N])] + unflatten_rest(vector[N:])

        return np.concatenate((flattened_first, flattened_rest)), unflatten

    elif isinstance(value, dict):
        flattened = []
        unflatteners = []
        lengths = []
        keys = []
        for k, v in sorted(value.items(), key=itemgetter(0)):
            cur_flattened, cur_unflatten = flatten(v)
            flattened.append(cur_flattened)
            unflatteners.append(cur_unflatten)
            lengths.append(len(cur_flattened))
            keys.append(k)

        def unflatten(vector):
            split_ixs = np.cumsum(lengths)
            pieces = np.split(vector, split_ixs)
            return {key: unflattener(piece)
                    for piece, unflattener, key in zip(pieces,
                                                       unflatteners,
                                                       keys)}

        return np.concatenate(flattened), unflatten

    else:
        raise Exception("Don't know how to flatten type {}".format(type(value))
                        )
