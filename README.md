# pyflatten

A utility for flattening nested data structures into an array, and providing an "un-flattening" function to get back the original.

## package authors

I dare not take credit for the idea or code. Original heroes are:

- [David Duvenaud][1] (Harvard, Univ. Toronto)
- [Dougal Maclaurin][2] (Harvard)
- [Matt J. Johnson][3] (Harvard)

[1]: http://people.seas.harvard.edu/~dduvenaud/
[2]: http://users.physics.harvard.edu/~maclaurin/
[3]: http://people.csail.mit.edu/mattjj/

I only decided to package this up as an independent, general purpose utility with David's permission.

## installation

From PyPI:

    $ pip install pyflatten

To get whatever's the latest:

    $ cd /path/to/some/directory
    $ git clone git@github.com:ericmjl/pyflatten
    $ cd pyflatten
    $ python setup.py develop  # in the future, you can simply git pull to get more latest goodies.

## usage example

    In [1]: import numpy.random as npr
    In [2]: import numpy as np
    In [3]: from pyflatten import flatten
    In [4]: paste
        val = {'k1': npr.randn(4, 4),
               'k2': npr.randn(3, 3),
               'k3': 3.0,
               'k4': [1.0, 4.0, 7.0, 9.0]}
    ## -- End pasted text --
    In [5]: vect, unflatten = flatten(val)  # returns a vector and an "unflatten" function.
    In [6]: vect
    Out[6]:
    array([-1.20274831,  0.44300699,  0.77940526, -1.40760001,  1.14251971,
            1.5118117 ,  1.37962866, -1.96744147, -1.14790883,  2.09023223,
            0.97555019, -0.14938287, -0.86665878,  0.14522684, -3.97717104,
            1.82750609, -0.1126678 ,  1.70907273,  0.81590652,  0.80267297,
            1.75690624,  0.54103164,  1.11719463,  2.34272313, -0.44388167,
            3.        ,  1.        ,  4.        ,  7.        ,  9.        ])
    In [7]: unflatten(vect)  # use the unflatten function to get back the original data structure. 
    Out[7]:
    {'k1': array([[-1.20274831,  0.44300699,  0.77940526, -1.40760001],
            [ 1.14251971,  1.5118117 ,  1.37962866, -1.96744147],
            [-1.14790883,  2.09023223,  0.97555019, -0.14938287],
            [-0.86665878,  0.14522684, -3.97717104,  1.82750609]]),
     'k2': array([[-0.1126678 ,  1.70907273,  0.81590652],
            [ 0.80267297,  1.75690624,  0.54103164],
            [ 1.11719463,  2.34272313, -0.44388167]]),
     'k3': 3.0,
     'k4': [1.0, 4.0, 7.0, 9.0]}

## contributing

Pull requests are welcome!
