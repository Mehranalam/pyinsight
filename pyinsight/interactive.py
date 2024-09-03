import pandas as pd
import matplotlib.pyplot as plt

class InteractiveTable:
    def __init__(self, data):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise ValueError("Data should be a pandas DataFrame")

    def show(self):
        print(self.data.to_string())

    def filter(self, column, value):
        filtered_data = self.data[self.data[column] == value]
        return InteractiveTable(filtered_data)

class InteractivePlot:
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y

    def show(self):
        plt.plot(self.data[self.x], self.data[self.y])
        plt.xlabel(self.x)
        plt.ylabel(self.y)
        plt.title(f'{self.y} vs {self.x}')
        plt.show()

    def interactive_zoom(self):
        print("Use the arrow keys to zoom in and out.")
        # اینجا می‌توانید منطق مربوط به تعامل را پیاده‌سازی کنید
