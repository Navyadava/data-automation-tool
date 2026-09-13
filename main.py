from data_cleaner import (
    load_data,
    inspect_data,
    filter_by_category,
    filter_high_value_orders,
    add_tax_column,
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


if __name__ == "__main__":
    main()