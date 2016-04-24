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
    """generate a list of functions from the library or module (shortened libr)"""
    
    functions_list = [o for o in getmembers(libr) 
                      if isfunction(o[1]) or (type(o[1]) is 'numpy.ufunc')   
                      and o[0].islower()
                      and o[0] not in deprecated_fns
                      and o[0] not in non_calculating]
    for fn in functions_list:
        yield fn

# sys.stdout = sys.stdin

def possibilities(libs = [np], **kwargs):
    """ generate possibile functions or combinations of functions
    using combinations of arguments of those functions,
    to get from start to finish with your scope limited to list of modules in libs.
    """
    sys.stdout = sys.stderr = shut_up
    libs = kwargs['libs']
    start = kwargs['start']
    finish = kwargs['finish']

    for lib in libs:
        for x in fns(lib):
            try:
                if lib == np:
                    fn_start = x[1](start)
                    a = np.all(np.equal(fn_start, finish))
                    b = np.ndim(fn_start) == np.ndim(finish)
                    if a and b:
                        yield x
                else:
                    if x[1](start) == finish:
                        yield x
            except:
                pass
    sys.stdout, sys.stderr = ok_start_talking
    

