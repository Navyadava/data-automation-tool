import pandas as pd

from data_cleaner import (
    load_data,
    inspect_data,
    filter_by_category,
    filter_high_value_orders,
    add_tax_column,
    clean_data,
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


if __name__ == "__main__":
    main()