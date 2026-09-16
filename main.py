import pandas as pd
import logging
import requests

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
    export_reports,
    validate_required_columns,
    validate_data_types,
    fetch_exchange_rate,
)

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    # DAY 15 - Load and inspect data
    file_path = "sales_data.csv"

    logging.info("Loading sales data")

    data = load_data(file_path)

    logging.info("Sales data file loaded successfully")

    logging.info("Data loaded successfully")

    inspect_data(data)

    # DAY 16 - Selecting and filtering
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
    sorted_data = data.sort_values(
        by="amount",
        ascending=False
    )
    print(sorted_data[["product", "amount"]])

    # DAY 17 - Clean messy data
    print("\n--- Messy Data ---")

    messy_data = load_data("sample_data/messy_sales_data.csv")
    original_rows = len(messy_data)

    print(messy_data)

    print("\n--- Final Cleaned Data ---")

    cleaned_data = clean_data(messy_data)

    cleaned_rows = len(cleaned_data)
    duplicates_removed = original_rows - cleaned_rows

    logging.info(f"Rows before cleaning: {original_rows}")
    logging.info(f"Rows after cleaning: {cleaned_rows}")
    logging.info(f"Duplicates removed: {duplicates_removed}")

    print(cleaned_data)

    # DAY 21 - Exchange Rate Conversion
    print("\n--- Exchange Rate Conversion ---")

    try:
        exchange_rate = fetch_exchange_rate()

        cleaned_data["amount_in_eur"] = (
            cleaned_data["amount"] * exchange_rate
        ).round(2)

        logging.info(
            f"Exchange rate fetched successfully: {exchange_rate}"
        )

        print(
            cleaned_data[
                ["product", "amount", "amount_in_eur"]
            ]
        )

    except requests.RequestException as error:
        logging.error(f"API error: {error}")
        print("Error: Could not fetch exchange rate.")

    # DAY 19 Practice 1 - Export cleaned CSV
    cleaned_data.to_csv(
        "cleaned_sales.csv",
        index=False
    )

    print("\nCleaned data exported to cleaned_sales.csv")

    # DAY 18 - Total Sales
    print("\n--- Total Sales ---")

    total_sales = calculate_total_sales(cleaned_data)

    print(total_sales)

    # Average Order Value
    print("\n--- Average Order Value ---")

    average_order = cleaned_data["amount"].mean()

    print(average_order)

    # Category Summary
    print("\n--- Category Summary ---")

    category_report = category_summary(cleaned_data)

    print(category_report)

    # Monthly Summary
    print("\n--- Monthly Summary ---")

    monthly_report = monthly_summary(cleaned_data)

    print(monthly_report)

    # DAY 19 Practice 2 - Export summary CSV
    category_report.to_csv("sales_summary.csv")

    print("\nSales summary exported to sales_summary.csv")

    # DAY 19 Practice 3 - Excel report
    print("\n--- Exporting Excel Report ---")

    with pd.ExcelWriter(
        "sales_report.xlsx",
        engine="openpyxl"
    ) as writer:

        cleaned_data.to_excel(
            writer,
            sheet_name="Cleaned Data",
            index=False
        )

        category_report.to_excel(
            writer,
            sheet_name="Category Summary"
        )

        monthly_report.to_excel(
            writer,
            sheet_name="Monthly Summary"
        )

    logging.info("Excel report exported to sales_report.xlsx")

    # DAY 19 Project Task
    print("\n--- Export Reports ---")

    input_file = input("Enter input file: ")

    output_dir = input("Enter output folder: ")

    try:
        user_data = load_data(input_file)
        logging.info(f"Input file loaded: {input_file}")

        validate_required_columns(user_data)
        validate_data_types(user_data)

        user_cleaned = clean_data(user_data)
        exchange_rate = fetch_exchange_rate()

        user_cleaned["amount_in_eur"] = (
            user_cleaned["amount"] * exchange_rate
        ).round(2)

        logging.info(
            f"EUR conversion added to exported report using rate: {exchange_rate}"
        )

    except FileNotFoundError:
        logging.error(f"File not found: {input_file}")
        print("Error: Input file not found.")
        return

    except ValueError as error:
        logging.error(str(error))
        print(f"Error: {error}")
        return
    
    summaries = {
        "category": category_summary(user_cleaned),
        "monthly": monthly_summary(user_cleaned)
}

    export_reports(
        user_cleaned,
        summaries,
        output_dir
    )


if __name__ == "__main__":
    main()