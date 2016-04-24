import numpy as np
import nose
import unittest
from possibilities.posibility_generator import possibilities

class test_absolute_value(unittest.TestCase):
    def test_abs():
        start = np.array([-5])
        finish = np.array([5])
        assert(possibilities(start = start, finish=finish, libs=[np])

class test_transpose(unittest.TestCase):
    
    def test_transpose():
        start = np.arange(6).reshape(2, 3)
        finish = np.array([[0, 3],
                                        [1, 4],
                                        [2, 5]]
        )
        self.assert_in('transpose',possibilities(start = start, finish=finish, libs=[np]))


