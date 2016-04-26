import os
from inspect import getmembers, isfunction, ismethod, signature
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
                      if isfunction(o[1]) or ismethod(o[1]) or (type(o[1]) is 'numpy.ufunc')
#                      and o[0].islower()
                      and o[0] not in deprecated_fns
                      and o[0] not in non_calculating]
    for fn in functions_list:
        yield fn

# sys.stdout = sys.stdin
def possibility_libs(libs = [np], **kwargs):
    """if you want to run through several libraries to search for combinations"""
    for lib in libs:
        yield from possibility_from_fns(lib=lib, **kwargs)
        
def possibility_from_fns(**kwargs):
    """ generate possibile functions or combinations of functions
    using combinations of arguments of those functions,
    to get from start to finish with your scope limited to list of modules in libs.
    """
    sys.stdout = sys.stderr = shut_up
    lib = kwargs['lib']
    start = kwargs['start']
    finish = kwargs['finish']
    fn_arguments_possibilities = [start, 0,1,-1, 1/np.e**-1]
    #     test_fn = kwargs['test_fn'] #used only for testing a particular function  example: np.add
    #     test_args = kwargs['test_args'] #used only for testing the arguments to the test_function example = [
    #     test_fn_signature = signature(test_fn)
    #     for param in test_fn_signature.parameters.values():
    #         #if (param.kind == param.KEYWORD_ONLY and param.default is param.empty):
    #         print(param)
    
    for x in fns(lib): # x is a tuple of (str(name), function_object)
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
    

def try_the_thing(fn, args):
    try:
        yield (fn, args)
    except:
        pass
    
def args_possibilities(fn):
    sig = signature(fn)
    print(sig) # (a, axes=None)
    for x in sig:
        if x has type_information:
            #get attributes with that type:
            yield from try_the_thing(fn, x)
        else:
            #gotta try them all
                yield from try_the_thing(fn, x)
            
    yield (fn, sig)
    
    
    