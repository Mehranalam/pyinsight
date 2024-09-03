from pyinsight.interactive import InteractiveTable, InteractivePlot
from pyinsight.text_analysis import TextAnalysis
from pyinsight.live_data import LiveDataPlot
import pandas as pd

data = pd.DataFrame({
    "Name": ["mehran", "ali", "matin", "elnaz"],
    "Age": [24, 27, 22, 32],
    "City": ["tehran", "gilan", "boshehr", "karaj"]
})

table = InteractiveTable(data)
table.show()

filtered_table = table.filter("City", "Chicago")
filtered_table.show()

plot = InteractivePlot(data, "Name", "Age")
plot.show()

text = "Python is a great programming language. It is widely used in data science."
analysis = TextAnalysis(text)
print("Sentiment:", analysis.sentiment())
print("Keywords:", analysis.keywords())

live_plot = LiveDataPlot(update_interval=2)
live_plot.start()
