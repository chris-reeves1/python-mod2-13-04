# Testing: 

# - Evaluating software for correctness(do things function as they should), 
#   meeting requirements. 

# - unit tests (static)
# - int tests (cloud, dbs, external api's - static + mocked)
# - automation testing - selenium/playwright - just 1-2 main flows. 

# - system testing
# - load/performamce testing
# - stress testing
# - UAT testing  
# - QA testing
# - staging
# - Security testing. 

# TDD:
# Write tests, get them to fail, then write code only to pass the test.

# Techincal:  
# goals:
# - Prove one behaviour at a time. 
# - Isolated, reapeatable, fast(<100m/s)
# - Document tests. Name per behaviour/intent. 

# Rules:
# - AAA
#     - arrange
#     - act
#     - assert
# - isolation: 
#     - filesystem, time, environment, network, -- all must be faked!
# - small, keep it meaningful:
#     do test:
#         - happy path: typical usage/data.
#         - bounarieas/edge cases. - empty, null/None, min/max, diff data types. 
#         - Error handling: test for correct exceptions/validation message.
#         - Repeatability.
#         - interactions.     
#     dont test:
#         - devs QOL functions/cosmetic/trivial
#         - language/libraries
#         - private - test the public api that then calls it. 
#         - dont test tests!! - keep it simple - NO imperitive LOGIC!!!!
#         - clever never. 
         
# - check inputs
# - check outputs
# - decide inputs
# - Oracle - what is the equality you will check for.
# - what to isolate?
# - AAA - data/setup/names etc
# - Dont overspecify - we want to refactor code later! 
# - negatives paths
# - paramtrization, scope. 


# unitest:
# python3 -m unittest file_name

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_calc_class_exists(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_add_method_exists(self):
        calc = Calculator()
        self.assertTrue(callable(getattr(calc, "add", False)))
    
    def test_add_method_input_validation(self):
        calc = Calculator()
        with self.assertRaisesRegex(TypeError, "input type error"):
            calc.add("a", 1)

    def test_add_method_logic(self):
        calc = Calculator()
        self.assertEqual(calc.add(5, 4), 9)
        self.assertEqual(calc.add(-5, -4), -9)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(400, 400), 800)