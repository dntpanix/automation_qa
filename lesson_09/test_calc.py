import unittest
import calc

class PositiveTests(unittest.TestCase):

    def test_add(self):
        """Test additonal of numbers"""
        input_a = 2
        input_b = 3
        expected = 5
        actutal_result = calc.add(input_a, input_b)
        self.assertEqual(expected, actutal_result, msg=f"Additional operation FAIL {input_a}+{input_b}={actutal_result} ")

    def test_dif(self):
        """Test minus of numbers"""
        input_a = 2
        input_b = 3
        expected = 1
        actutal_result = calc.dif(input_b, input_a)
        self.assertTrue(actutal_result == expected, msg="Minus operation FAIL")

    def test_div_negative(self):
        input_a = 2
        input_b = 0
        expected = 0
        # actutal_result = calc.div(input_a, input_b)
        # self.assertTrue(actutal_result == expected, msg=f"operation FAIL:{actutal_result}")
        with self.assertRaises(ZeroDivisionError):
            result = calc.div(input_a, input_b)

    def test_div_negative_2(self):
        input_a = 2
        input_b = -1
        expected = 0
        # actutal_result = calc.div(input_a, input_b)
        # self.assertTrue(actutal_result == expected, msg=f"operation FAIL:{actutal_result}")
        with self.assertRaises(ValueError):
            result = calc.div(input_a, input_b)

if __name__ == '__main__':
    unittest.main(verbosity=2)