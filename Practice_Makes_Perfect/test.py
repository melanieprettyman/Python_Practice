import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print("about to run a test")
    def test_main(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
    def test_error_thrown(self):
        test_param ="blah"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    #----------test game--------
    def test_input(self):
        result = main.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = main.run_guess(0, 5)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = main.run_guess(11, 5)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = main.run_guess('11', 5)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

