from data_cleaner import load_data, inspect_data


def main():
    file_path = "sales_data.csv"

    print("Loading sales data...")

    data = load_data(file_path)

    print("Data loaded successfully!")

    inspect_data(data)


if __name__ == "__main__":
    main()