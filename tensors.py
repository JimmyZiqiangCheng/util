"""
MIT License

Copyright (c) 2018 Rafael Felix Alves

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
def merge_array(x, y, axis=0):
    import numpy as np
    if np.shape(x)[0]:
        if np.shape(y)[0]:
            return np.concatenate([x,y], axis)
        else:
            return x
    elif np.shape(y)[0]:
        return y
    else:
        return np.array([])


def normalize(x, ord=1,axis=-1):
    '''
    Normalize is a function that performs unit normalization
    Please, see http://mathworld.wolfram.com/UnitVector.html
    :param x: Vector
    :return: normalized x
    '''
    from numpy import atleast_2d, linalg, float
    return (atleast_2d(x) / atleast_2d(linalg.norm(atleast_2d(x), ord=ord, axis=axis)).T).astype(float)