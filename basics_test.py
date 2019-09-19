import unittest
import math
import numpy as np
import get_column_stats as stats


class TestGetColumnStats(unittest.TestCase):

    def test_stats_constant(self):
        """ This function tests the method column_stats in
            get_column_stats.py with a list of constants
        """
        data = []
        for i in range(1000):
            data.append(i)
        [mean_calc, std_calc] = stats.column_stats(data)
        self.assertEqual(mean_calc, np.mean(data))
        self.assertEqual(std_calc, np.std(data))

    def test_stats_random(self):
        """ This function tests the method column_stats in
            get_column_stats.py with a list of random numbers
        """
        data = []
        for i in range(1000):
            data.append(np.random.randint(1000))
        [mean_calc, std_calc] = stats.column_stats(data)
        self.assertEqual(mean_calc, np.mean(data))
        self.assertAlmostEqual(std_calc, np.std(data))
        # use assertAlmostEqual to compare floating point numbers

    def test_exceptions(self):
        """This function tests if an exception is raised.
        """
        # One way to use assertRaises
        with self.assertRaises(ZeroDivisionError) as ex:
            stats.column_stats([])
        # Another way to use assertRaises
        self.assertRaises(TypeError, stats.column_stats, 'a')


class ParserTest(unittest.TestCase):

    def setUp(self):
        """This function set up the parser for the unit test of argparse.
        """
        self.parser = stats.initialize()

    def test_file_name(self):
        """This function test if the parser works properly.
        """
        parsed = self.parser.parse_args(['-f', 'data.txt', '-c', '2'])
        self.assertEqual(parsed.file_name, 'data.txt')
        self.assertEqual(parsed.column_number, '2')


if __name__ == '__main__':
    unittest.main()
