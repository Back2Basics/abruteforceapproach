from mock import mock
import numpy as np
from possibilities.posibility_generator import possibility_libs, args_possibilities
import unittest
from _collections import defaultdict

class test_multiple_arguments(unittest.TestCase):
    def setUp(self):
        self.start = np.arange(6)
        self.finish = np.add(self.start,1)
        self.data_options = [self.start, 1, -1, 0]
        self.my = mock.ModuleType('my')
        self.my.transpose = np.transpose
 
    def test_arguments(self):
        #returns a tuple of the function and an ordered dict of the args that worked
        possibility_libs(start = self.start, finish=self.finish, libs=[self.my])
 
        self.assertIn(('transpose',{1: self.start}), list(args_possibilities(self.my.transpose)))
#         test_fn = kwargs['test_fn'] #used only for testing a particular function  example: np.add
#         test_args = kwargs['test_args'] #used only for testing the arguments to the test_function example = [
#         test_fn_signature = signature(test_fn)
#         for param in test_fn_signature.parameters.values():
#             #if (param.kind == param.KEYWORD_ONLY and param.default is param.empty):
#             print(param)
         
         


class test_matrix_possibilities(unittest.TestCase):
    def setUp(self):
        self.start = np.arange(6).reshape(2, 3)
        self.finish = np.array([[0, 3],
                                        [1, 4],
                                        [2, 5]]
        )

    def tearDown(self):
        del(self.start)
        del(self.finish)

    def test_transpose(self):
        d = defaultdict(list)
        for k,v in possibility_libs(start = self.start, finish=self.finish, libs=[np]):
            d[k].append(v)
        self.assertIn('transpose' , d)
    

class test_unary_possibilities(unittest.TestCase):
    def setUp(self):
        self.start = np.array([-5])
        self.finish = np.array([5])
    
    def tearDown(self):
        del(self.start)
        del(self.finish)

    def test_abs(self):
        self.assertTrue(possibility_libs(start = self.start, finish=self.finish, libs=[np]))
    
    
if __name__ == '__main__':
    unittest.main()


