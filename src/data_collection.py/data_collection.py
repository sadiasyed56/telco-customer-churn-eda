import pandas as pd

def load_data(path):
    """
    Load dataset from a given path.
    Returns a pandas DataFrame.
    """
    df = pd.read_csv(path)
    return df
