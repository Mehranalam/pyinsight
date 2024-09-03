# **PyInsight**

**PyInsight** is a Python library designed to simplify interactive data analysis and visualization directly within the console. With tools for displaying tables, generating plots, analyzing text, and managing live data, **PyInsight** empowers you to work more efficiently with your data.

## **Features**

- **Interactive Tables**: Display and filter tabular data interactively.
- **Interactive Plots**: Create interactive visualizations and plots.
- **Text Analysis**: Analyze text for sentiment and extract keywords.
- **Live Data**: Monitor and visualize real-time data streams.

## **Installation**

You can easily install **PyInsight** using pip:

```bash
pip install pyinsight
```

Alternatively, install from the source:

1. Clone the repository:
    ```bash
    git clone https://github.com/Mehranalam/pyinsight.git
    cd pyinsight
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install the package:
    ```bash
    pip install .
    ```

## **Getting Started**

Here’s how you can start using **PyInsight**:

1. **Import the Library**:
    ```python
    import pandas as pd
    from pyinsight.interactive import InteractiveTable, InteractivePlot
    ```

2. **Create a DataFrame**:
    ```python
    data = pd.DataFrame({
        "Name": ["mehran", "ali", "matin", "elnaz"],
        "Age": [24, 27, 22, 32],
        "City": ["tehran", "gilan", "boshehr", "karaj"]
    })
    ```

3. **Interactive Tables**:
    ```python
    table = InteractiveTable(data)
    table.show()
    
    filtered_table = table.filter("City", "karaj")
    filtered_table.show()
    ```

4. **Interactive Plots**:
    ```python
    plot = InteractivePlot(data, "Name", "Age")
    plot.show()
    ```

5. **Text Analysis**:
    ```python
    from pyinsight.text_analysis import TextAnalysis

    text = "Python is a great programming language."
    analysis = TextAnalysis(text)
    print("Sentiment:", analysis.sentiment())
    print("Keywords:", analysis.keywords())
    ```

6. **Live Data**:
    ```python
    from pyinsight.live_data import LiveDataPlot

    live_plot = LiveDataPlot(update_interval=2)
    live_plot.start()
    ```

## **Examples**

### **Example 1: Displaying and Filtering Data**

```python
import pandas as pd
from pyinsight.interactive import InteractiveTable

data = pd.DataFrame({
    "Name": ["mehran", "ali", "matin", "elnaz"],
    "Age": [24, 27, 22, 32],
    "City": ["tehran", "gilan", "boshehr", "karaj"]
})

table = InteractiveTable(data)
table.show()

filtered_table = table.filter("City", "karaj")
filtered_table.show()
```

### **Example 2: Creating Interactive Plots**

```python
from pyinsight.interactive import InteractivePlot

data = pd.DataFrame({
    "Name": ["ali", "matin", "sanaz", "javad"],
    "Age": [24, 27, 22, 32]
})

plot = InteractivePlot(data, "Name", "Age")
plot.show()
```

### **Example 3: Analyzing Text Data**

```python
from pyinsight.text_analysis import TextAnalysis

text = "Python is versatile and used in many fields."
analysis = TextAnalysis(text)

print("Sentiment:", analysis.sentiment())
print("Keywords:", analysis.keywords())
```

### **Example 4: Live Data Visualization**

```python
from pyinsight.live_data import LiveDataPlot

live_plot = LiveDataPlot(update_interval=1)
live_plot.start()
```

## **Documentation**

For detailed Documentation, please refer to the [Documentation](DOCUMENT.md).

## **Contributing**

We welcome contributions to **PyInsight**! If you would like to contribute, please:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## **License**

**PyInsight** is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## **Contact**

For any questions or feedback, please contact:

- **Author**: Mehran Alam Beigi
- **Email**: Mehraxxn@gmail.com
- **GitHub**: [Mehranalam](https://github.com/mehranalam)
