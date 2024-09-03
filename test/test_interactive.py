import unittest
import pandas as pd
from pyinsight.interactive import InteractiveTable, InteractivePlot

class TestInteractiveTable(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "Name": ["Alice", "Bob", "Charlie", "David"],
            "Age": [24, 27, 22, 32],
            "City": ["New York", "Los Angeles", "Chicago", "Houston"]
        })
        self.table = InteractiveTable(self.data)

    def test_show(self):
        self.assertEqual(self.table.data.shape, (4, 3))

    def test_filter(self):
        filtered_table = self.table.filter("City", "Chicago")
        self.assertEqual(filtered_table.data.shape, (1, 3))

class TestInteractivePlot(unittest.TestCase):
    def setUp(self):
        self.data = pd.DataFrame({
            "Name": ["Alice", "Bob", "Charlie", "David"],
            "Age": [24, 27, 22, 32]
        })

    def test_show_plot(self):
        plot = InteractivePlot(self.data, "Name", "Age")

if __name__ == '__main__':
    unittest.main()
