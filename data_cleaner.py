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


def filter_by_category(df, category):
    return df[df["category"] == category]


def filter_high_value_orders(df, threshold):
    return df[df["amount"] > threshold]


def add_tax_column(df, tax_rate):
    df["amount_with_tax"] = df["amount"] * (1 + tax_rate)
    return df