    import unittest
    from my_module import add_numbers, subtract_numbers

    class TestMyModule(unittest.TestCase):
        def test_add_numbers(self):
            self.assertEqual(add_numbers(2, 3), 5)
            self.assertEqual(add_numbers(-1, 1), 0)

        def test_subtract_numbers(self):
            self.assertEqual(subtract_numbers(5, 2), 3)
            self.assertEqual(subtract_numbers(10, 10), 0)

    if __name__ == '__main__':
        unittest.main()
