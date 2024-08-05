import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Akash_RJ"
        test_upper = to_upper(name)
        self.assertEqual(test_upper,"AKASH_RJ")

if __name__=='__main__':
    unittest.main()
