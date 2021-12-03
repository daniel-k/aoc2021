from itertools import tee
from typing import Iterable, List

def flatten(iterable: Iterable) -> List:
    return [e for sub_iterable in iterable for e in sub_iterable]

# from more-itertools:
# https://more-itertools.readthedocs.io/en/stable/_modules/more_itertools/recipes.html#pairwise


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def triplets(iterable):
    "s -> (s0,s1,s2), (s1,s2,s3), (s2, s3,s4), ..."
    a, b, c = tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)
