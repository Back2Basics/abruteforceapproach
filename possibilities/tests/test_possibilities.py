import numpy as np
from nose import with_setup
from possibilities.posibility_generator import possibilities
import unittest
def setup_transpose():
    start = np.arange(6).reshape(2, 3)
    finish = np.array([[0, 3],
                                    [1, 4],
                                    [2, 5]]
    )
    


class test_unary_possibilities(unittest.TestCase):
    def setUp(self):
        self.start = np.array([-5])
        self.finish = np.array([5])
    
    def tearDown(self):
        del(self.start)
        del(self.finish)
    

    def test_abs(self):
        self.assertTrue(possibilities(start = self.start, finish=self.finish, libs=[np]))
    
    def test_transpose(self):
        self.assertIn('transpose' , possibilities(start = self.start, finish=self.finish, libs=[np]))
    
    
if __name__ == '__main__':
    unittest.main()
    