import unittest

from abw_helpers.plusframe import PlusFrame


class TestPlusFrame(unittest.TestCase):

    def test_new_col(self):

        items = ['a', 'b', 'c', 'd', 'e', 'f']
        pf = PlusFrame({
            'heroes': ['dr strange', 'spider man', 'silver surfer', 'thor', 'blade', 'hulk'],
            'villains': ['dormamu', 'mysterio', 'galactus', 'ultron', 'dracula', 'red hulk']
        })
        # ensure pf is created with proper column names
        self.assertEqual(list(pf.columns), ['heroes', 'villains'])
        self.assertEqual(len(items), 6)

        pf.new_col(items)
        # ensure there is a "new_column" column
        self.assertEqual(
            list(
                pf.columns), [
                'heroes', 'villains', 'new_column'])
        self.assertEqual(len(list(pf.columns)), 3)

        # ensure the values in "new_column" match values in items
        self.assertEqual(pf["new_column"][0], "a")
        self.assertEqual(len(pf["new_column"]), len(items))

    def test_nulls(self):
        pf = PlusFrame({
            'heroes': ['dr strange', 'spider man', 'silver surfer', 'thor', 'blade', 'hulk'],
            'villains': ['dormamu', 'mysterio', 'galactus', 'ultron', 'dracula', 'red hulk']
        })

        example = pf.nulls()
        # ensure that first line includes two values (number of nans, and
        # number of columns)
        self.assertEqual(example[0], 2)


if __name__ == "__main__":
    unittest.main()
