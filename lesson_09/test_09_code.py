import unittest

# import sys
# import pathlib
# sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
# from lesson_07 import lesson_07
from importlib.machinery import SourceFileLoader

package_name = 'automation_qa_copy'
folder_mame = 'lesson_07'
module_name = folder_mame

lesson_07 = SourceFileLoader(module_name, f'{folder_mame}\{module_name}.py').load_module()
square = getattr(lesson_07, "square")
a_plus_b = getattr(lesson_07, "a_plus_b")


class HomeworksTesting(unittest.TestCase):

    PI = 3.14

    def test_task01(self):
        """Square of 2"""
        print("test1")
        actual_result = square(2)
        expected_result = 4
        self.assertEqual(actual_result, expected_result, f"Square of 2 is {square(2)}")

    def test_task02(self):
        """Square of 3"""
        actual_result = square(3)
        expected_result = 9
        self.assertEqual(actual_result, expected_result)

    def test_task03(self):
        """avg_arifmethic, positive num"""
        actual_result = a_plus_b(1,1,1,1,1)
        print("Я друкуюся на екран!!!")
        expected_result = 2
        self.assertEqual(actual_result, expected_result)
        self.assertTrue(actual_result == expected_result, msg="")
        self.assertEqual(self.PI, 3.14)

if __name__ == "__main__":
    unittest.main(verbosity=2)
