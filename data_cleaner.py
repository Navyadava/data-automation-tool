import pandas as pd
import os


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

def clean_data(df):
    df = df.copy()

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing amounts
    df["amount"] = df["amount"].fillna(df["amount"].median())

    # Clean category names
    df["category"] = df["category"].str.strip().str.lower()

    # Convert dates
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce",
        format="mixed"
    )

    return df

def calculate_total_sales(df):
    return df["amount"].sum()


def category_summary(df):
    return df.groupby("category")["amount"].agg(
        ["sum", "mean", "count"]
    )


def monthly_summary(df):
    df = df.copy()
    df["month"] = df["date"].dt.to_period("M")
    return df.groupby("month")["amount"].sum()

def export_reports(df_clean, summaries, output_dir):
    # Create output folder if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # File paths
    cleaned_file = os.path.join(output_dir, "cleaned_sales.csv")
    summary_file = os.path.join(output_dir, "sales_summary.csv")
    excel_file = os.path.join(output_dir, "sales_report.xlsx")

    # Export cleaned data
    df_clean.to_csv(cleaned_file, index=False)

    # Export category summary
    summaries["category"].to_csv(summary_file)

    # Export Excel report with multiple sheets
    with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
        df_clean.to_excel(
            writer,
            sheet_name="Cleaned Data",
            index=False
        )

        summaries["category"].to_excel(
            writer,
            sheet_name="Category Summary"
        )

        summaries["monthly"].to_excel(
            writer,
            sheet_name="Monthly Summary"
        )

    print(f"Cleaned data saved to {cleaned_file}")
    print(f"Summary saved to {summary_file}")
    print(f"Excel report saved to {excel_file}")