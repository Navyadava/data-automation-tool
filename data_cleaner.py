import pandas as pd


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def inspect_data(data):
    print("\n--- First 5 Rows ---")
    print(data.head())

    print("\n--- Data Information ---")
    data.info()

    print("\n--- Missing Values ---")
    print(data.isnull().sum())

    print("\n--- Basic Statistics ---")
    print(data.describe())