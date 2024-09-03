import matplotlib.pyplot as plt

class GraphNavigation:
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
        self.current_view = (0, len(data))

    def show(self):
        plt.plot(self.data[self.x][self.current_view[0]:self.current_view[1]], 
                 self.data[self.y][self.current_view[0]:self.current_view[1]])
        plt.show()

    def zoom_in(self):
        pass

    def zoom_out(self):
        pass

    def pan(self, direction):
        pass
