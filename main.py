import pandas as pd

from data_cleaner import (
    load_data,
    inspect_data,
    filter_by_category,
    filter_high_value_orders,
    add_tax_column,
    clean_data,
    calculate_total_sales,
    category_summary,
    monthly_summary,
)


def main():
    file_path = "sales_data.csv"

    print("Loading sales data...")

    data = load_data(file_path)

    print("Data loaded successfully!")

    inspect_data(data)

    print("\n--- Selected Columns ---")
    print(data[["product", "amount"]])

    print("\n--- Orders Above $1000 ---")
    high_value_orders = filter_high_value_orders(data, 1000)
    print(high_value_orders)

    print("\n--- Electronics Orders ---")
    electronics = filter_by_category(data, "Electronics")
    print(electronics)

    print("\n--- Amount With Tax ---")
    data = add_tax_column(data, 0.18)
    print(data[["product", "amount", "amount_with_tax"]])

    print("\n--- Sorted By Amount ---")
    sorted_data = data.sort_values(by="amount", ascending=False)
    print(sorted_data[["product", "amount"]])

    print("\n--- Messy Data ---")
    messy_data = load_data("messy_sales_data.csv")
    print(messy_data)

    print("\n--- After Removing Duplicates ---")
    no_duplicates = messy_data.drop_duplicates()
    print(no_duplicates)

    print("\n--- Messy Data ---")
    messy_data = load_data("messy_sales_data.csv")
    print(messy_data)

    print("\n--- After Removing Duplicates ---")
    no_duplicates = messy_data.drop_duplicates()
    print(no_duplicates)

    print("\n--- After Filling Missing Amounts ---")
    filled_data = no_duplicates.copy()

    filled_data["amount"] = filled_data["amount"].fillna(
        filled_data["amount"].median()
)

    print(filled_data)

    print("\n--- After Cleaning Categories ---")

    cleaned_categories = filled_data.copy()

    cleaned_categories["category"] = (
        cleaned_categories["category"]
        .str.strip()
        .str.lower()
)

    print(cleaned_categories)

    print("\n--- After Cleaning Dates ---")

    cleaned_dates = cleaned_categories.copy()

    cleaned_dates["date"] = pd.to_datetime(
        cleaned_dates["date"],
        errors="coerce",
        format="mixed"
)

    print(cleaned_dates)

    print("\n--- Final Cleaned Data ---")

    messy_data = load_data("messy_sales_data.csv")
    cleaned_data = clean_data(messy_data)

    print(cleaned_data)

    cleaned_data.to_csv("cleaned_sales_data.csv", index=False)

    print("\nCleaned data saved successfully!")

    print("\n--- Total Sales ---")
    total_sales = cleaned_data["amount"].sum()
    print(total_sales)

    print("\n--- Average Order Value ---")
    average_order = cleaned_data["amount"].mean()
    print(average_order)

    print("\n--- Sales By Category ---")
    category_sales = cleaned_data.groupby("category")["amount"].sum()
    print(category_sales)

    print("\n--- Sales By Month ---")
    cleaned_data["month"] = cleaned_data["date"].dt.to_period("M")
    monthly_sales = cleaned_data.groupby("month")["amount"].sum()
    print(monthly_sales)

    print("\n--- Category Summary Table ---")

    category_summary_table = cleaned_data.groupby("category")["amount"].agg(
        ["sum", "mean", "count"]
)

    print(category_summary_table)

    print("\n--- Total Sales Function ---")
    print(calculate_total_sales(cleaned_data))

    print("\n--- Category Summary Function ---")
    print(category_summary(cleaned_data))

    print("\n--- Monthly Summary Function ---")
    print(monthly_summary(cleaned_data))

    

    

if __name__ == "__main__":
    main()