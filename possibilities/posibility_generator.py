import os
from inspect import getmembers, isfunction
import pandas as pd
import sys
import numpy as np
from collections import deque
import math
from pprint import pprint

deprecated_fns = ['rank', ]
non_calculating = ['warnings', 'who', 'version', 'lookfor' , 'info']

shut_up = open(os.devnull, 'w')
ok_start_talking = sys.stdout, sys.stderr

def fns(libr):
    # if libr == np:
    functions_list = [o for o in getmembers(libr) 
                      if (isfunction(o[1]) is o[0].islower()
                      or (type(o[1]) is 'numpy.ufunc'  and o[0].islower()))
                      and o[0] not in deprecated_fns
                      and o[0] not in non_calculating]
    for fn in functions_list:
        yield fn

# sys.stdout = sys.stdin

def possibilities(**kwargs):
    sys.stdout = sys.stderr = shut_up
    libs = kwargs['libs']
    start = kwargs['start']
    finish = kwargs['finish']

    for lib in libs:
        for x in fns(lib):
            try:
                if lib == np:
                    if np.all(x[1](start) == finish) and \
                        np.equal(x[1](start) == finish) and \
                        np.ndim(x[1](start) == finish):
                        yield x
                else:
                    if x[1](start) == finish:
                        yield x
            except:
                pass
    sys.stdout, sys.stderr = ok_start_talking
    
if __name__ == "__main__":
    pprint(list(possibilities(libs=[np, ], start=start, finish=finish)))

