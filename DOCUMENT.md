# **PyInsight** Documentation

**PyInsight** is a Python library designed for interactive data analysis and visualization directly within the console. It provides a suite of tools for displaying tables, creating plots, analyzing text data, and managing live data streams, all with interactive capabilities.

## **Table of Contents**

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Getting Started](#getting-started)
    - [Basic Usage](#basic-usage)
5. [Detailed Usage](#detailed-usage)
    - [Interactive Tables](#interactive-tables)
    - [Interactive Plots](#interactive-plots)
    - [Text Analysis](#text-analysis)
    - [Live Data](#live-data)
6. [Examples](#examples)
7. [API Reference](#api-reference)
    - [InteractiveTable](#interactivetable)
    - [InteractivePlot](#interactiveplot)
    - [TextAnalysis](#textanalysis)
    - [LiveDataPlot](#livedataplot)
8. [Development](#development)
9. [Contributing](#contributing)
10. [License](#license)

## **Introduction**

**PyInsight** offers powerful tools for interactive data manipulation and visualization. Whether you're working with static datasets, visualizing data trends, analyzing textual information, or monitoring live data, **PyInsight** simplifies these tasks with a user-friendly interface.

## **Features**

- **Interactive Tables**: Display and filter tabular data interactively in the console.
- **Interactive Plots**: Generate and interact with various types of plots, such as line charts and bar charts.
- **Text Analysis**: Analyze text data for sentiment and extract keywords.
- **Live Data**: Monitor and visualize real-time data streams, ideal for monitoring live metrics or data feeds.

## **Installation**

### **Using pip**

The simplest way to install **PyInsight** is via pip:

```bash
pip install pyinsight
```

### **Installing from Source**

To install **PyInsight** from the source code, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mehranalam/pyinsight.git
   cd pyinsight
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install the Package**:
   ```bash
   pip install .
   ```

## **Getting Started**

To get started with **PyInsight**, you need to understand the basic components and how to use them. Here's a brief overview:

1. **Create a DataFrame**: Use `pandas` to create a DataFrame.
2. **Initialize and Use Classes**: Create instances of classes provided by **PyInsight** to interact with your data.

### **Basic Usage**

```python
import pandas as pd
from pyinsight.interactive import InteractiveTable, InteractivePlot

# Sample DataFrame
data = pd.DataFrame({
    "Name": ["mehran", "ali", "matin", "elnaz"],
    "Age": [24, 27, 22, 32],
    "City": ["tehran", "gilan", "boshehr", "karaj"]
})

# Create and display an interactive table
table = InteractiveTable(data)
table.show()

# Filter table data and display
filtered_table = table.filter("City", "karaj")
filtered_table.show()

# Create and display an interactive plot
plot = InteractivePlot(data, "Name", "Age")
plot.show()
```

## **Detailed Usage**

### **Interactive Tables**

The `InteractiveTable` class provides methods to display and filter tabular data.

#### **Creating and Displaying a Table**

```python
from pyinsight.interactive import InteractiveTable
import pandas as pd

# Initialize with DataFrame
data = pd.DataFrame({
    "Name": ["mehran", "ali", "matin", "elnaz"],
    "Age": [24, 27, 22, 32],
    "City": ["tehran", "gilan", "boshehr", "karaj"]
})
table = InteractiveTable(data)

# Display the table
table.show()
```

#### **Filtering Data**

```python
# Filter rows where 'City' is 'karaj'
filtered_table = table.filter("City", "karaj")
filtered_table.show()
```

### **Interactive Plots**

The `InteractivePlot` class allows for interactive plotting of data.

#### **Creating and Displaying a Plot**

```python
from pyinsight.interactive import InteractivePlot

# Initialize plot with data
plot = InteractivePlot(data, "Name", "Age")

# Display the plot
plot.show()
```

#### **Interactive Features**

The `interactive_zoom` method enables zooming within the plot.

```python
plot.interactive_zoom()
```

### **Text Analysis**

The `TextAnalysis` class provides tools for analyzing textual data, including sentiment analysis and keyword extraction.

#### **Performing Sentiment Analysis**

```python
from pyinsight.text_analysis import TextAnalysis

text = "Python is a great programming language."
analysis = TextAnalysis(text)

# Get sentiment
sentiment = analysis.sentiment()
print("Sentiment:", sentiment)
```

#### **Extracting Keywords**

```python
# Extract keywords
keywords = analysis.keywords()
print("Keywords:", keywords)
```

### **Live Data**

The `LiveDataPlot` class is used for displaying and updating live data in real-time.

#### **Starting Live Data Feed**

```python
from pyinsight.live_data import LiveDataPlot

# Initialize live data plot with an update interval of 2 seconds
live_plot = LiveDataPlot(update_interval=2)

# Start the live data feed
live_plot.start()
```

## **Examples**

Here are some comprehensive examples demonstrating how to use **PyInsight** in various scenarios.

### **Example 1: Data Table and Plot**

```python
import pandas as pd
from pyinsight.interactive import InteractiveTable, InteractivePlot

# Sample DataFrame
data = pd.DataFrame({
    "Name": ["mehran", "ali", "matin", "elnaz"],
    "Age": [24, 27, 22, 32],
    "City": ["tehran", "gilan", "boshehr", "karaj"]
})

# Display interactive table
table = InteractiveTable(data)
table.show()

# Filter and display
filtered_table = table.filter("City", "karaj")
filtered_table.show()

# Plotting
plot = InteractivePlot(data, "Name", "Age")
plot.show()
```

### **Example 2: Text Analysis**

```python
from pyinsight.text_analysis import TextAnalysis

text = "Python is a versatile language used in many fields including data science, web development, and automation."
analysis = TextAnalysis(text)

# Sentiment analysis
print("Sentiment:", analysis.sentiment())

# Keyword extraction
print("Keywords:", analysis.keywords())
```

### **Example 3: Live Data Visualization**

```python
from pyinsight.live_data import LiveDataPlot

# Initialize and start live data feed
live_plot = LiveDataPlot(update_interval=1)
live_plot.start()
```

## **API Reference**

### **InteractiveTable**

- **Constructor**: `InteractiveTable(data: pd.DataFrame)`
  - **Parameters**:
    - `data`: A pandas DataFrame to display.
- **Method**: `show()`
  - Displays the table in the console.
- **Method**: `filter(column: str, value: Any) -> InteractiveTable`
  - **Parameters**:
    - `column`: Column name to filter on.
    - `value`: Value to filter by.
  - **Returns**: A new `InteractiveTable` instance with filtered data.

### **InteractivePlot**

- **Constructor**: `InteractivePlot(data: pd.DataFrame, x: str, y: str)`
  - **Parameters**:
    - `data`: A pandas DataFrame containing the data.
    - `x`: Column name for x-axis.
    - `y`: Column name for y-axis.
- **Method**: `show()`
  - Displays the plot.
- **Method**: `interactive_zoom()`
  - Enables zoom functionality for the plot.

### **TextAnalysis**

- **Constructor**: `TextAnalysis(text: str)`
  - **Parameters**:
    - `text`: The text to analyze.
- **Method**: `sentiment() -> Sentiment`
  - **Returns**: A `Sentiment` object with polarity and subjectivity scores.
- **Method**: `keywords(num: int = 5) -> List[str]`
  - **Parameters**:
    - `num`: Number of keywords to return.
  - **Returns**: List of keywords.

### **LiveDataPlot**

- **Constructor**: `LiveDataPlot(update_interval: int = 1)`
  - **Parameters**:
    - `update_interval`: Interval in seconds for data updates.
- **Method**: `start()`
  - Starts the live data feed and prints updates to the console.

## **Development**

To contribute to **PyInsight**, please follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mehranalam/pyinsight.git
   cd pyinsight
   ```

2. **Install Development Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Tests**:
   ```bash
   pytest
   ```

4

. **Make Changes**:
   - Create a feature branch for your changes.
   - Implement and test your modifications.
   - Commit your changes and push them to the branch.

5. **Submit a Pull Request**:
   - Provide a clear description of your changes.
   - Ensure your code adheres to the project's coding standards.
   - Include relevant tests and documentation updates.

## **Contributing**

We welcome contributions to **PyInsight**. To ensure a smooth contribution process:

- Follow the development guidelines.
- Ensure your changes are well-documented and tested.
- Submit a pull request with a detailed description of your changes.

## **License**

**PyInsight** is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for full details.
