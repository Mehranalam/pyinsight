import pandas as pd

class QuickSummary:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize with a pandas DataFrame.
        
        :param data: DataFrame to summarize.
        """
        self.data = data
    
    def show(self):
        """
        Display a quick summary of the DataFrame.
        """
        print("Quick Summary\n" + "-"*50)
        
        # General info
        print(f"Total Rows: {self.data.shape[0]}")
        print(f"Total Columns: {self.data.shape[1]}")
        print("\nData Types:\n", self.data.dtypes)
        
        # Missing values
        missing_values = self.data.isnull().sum()
        print("\nMissing Values:\n", missing_values[missing_values > 0])
        
        # Statistical summary for numerical columns
        print("\nStatistical Summary (Numerical Data):\n", self.data.describe().T)
