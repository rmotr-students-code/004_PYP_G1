"""
Write a function that receives a list of numbers
and a list of terms and returns only the elements that are divisible
by all of those terms. You must use two nested list comprehensions to solve it.

Example:
    divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3])  # [12, 6]

"""
import unittest


def divisible_numbers(a_list, a_list_of_terms):
    return [x for x in a_list if all(x % k == 0 for k in a_list_of_terms)]


class DivisibleNumbersTestCase(unittest.TestCase):
    def test_divisible(self):
        self.assertEqual(set(divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3])), 
                         set([6, 12]))

    def test_one_divisible_numbers(self):
        self.assertEqual(divisible_numbers([16, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3, 4]), [12])

    def test_empty_list(self):
        self.assertEqual(divisible_numbers([], [5, 7]),  [])
        
    def test_both_empty_lists(self):
        self.assertEqual(divisible_numbers([], []),  [])
            
    def test_no_result(self):
        self.assertEqual(divisible_numbers([2, 4, 8], [5, 7]),  [])
        
#OH I remember now. why is it '__main__' instead of 'self'?        
if __name__ == '__main__':
    unittest.main()
    
    
#  remember: when you import module it executes every code once. this prevent  unittest.main() from running when importing.
def print_elem(elem):
        print elem
        
def assignment5(a_list):
    return [print_elem(elem) for elem in a_list]