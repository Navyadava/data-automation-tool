# Data Automation Tool

A Python-based data automation project that cleans, validates, analyzes, and exports sales data.

The tool uses Pandas for data processing, logging for tracking program activity, error handling for invalid input, and a public API for currency conversion.

## Features

* Load sales data from CSV files
* Inspect datasets using Pandas
* Remove duplicate records
* Handle missing values
* Clean category names
* Convert date values into a consistent format
* Validate required columns
* Validate numeric data types
* Calculate total sales
* Calculate average order value
* Create category summaries
* Create monthly sales summaries
* Fetch the current USD to EUR exchange rate using an API
* Add an `amount_in_eur` column
* Export cleaned data to CSV
* Export summary reports to CSV
* Create an Excel report with multiple sheets
* Write program activity and errors to `automation.log`

## Technologies Used

* Python
* Pandas
* Requests
* OpenPyXL
* Python Logging
* CSV
* Excel
* Git
* GitHub

## Project Structure

```text
data-automation-tool/
│
├── main.py
├── data_cleaner.py
├── api_test.py
├── README.md
├── sales_data.csv
├── messy_sales_data.csv
├── automation.log
├── reports/
│   ├── cleaned_sales.csv
│   ├── sales_summary.csv
│   └── sales_report.xlsx
└── tests/
```

## Installation

Clone the repository and open the project folder.

Install the required packages:

```bash
python -m pip install pandas openpyxl requests
```

## How to Run

Run the program from the terminal:

```bash
python main.py
```

When prompted, enter the input CSV file:

```text
messy_sales_data.csv
```

Then enter the output folder:

```text
reports
```

## Example Input

```csv
order_id,date,product,category,amount,city
2001,2026-09-01,Burger,Food,15.99,Miami
2002,09/02/2026,Pizza,food,22.50,Orlando
2003,September 3 2026,Pasta,FOOD,,Tampa
```

## Example Output

The cleaned data includes standardized categories, cleaned dates, filled missing values, and EUR conversion.

```text
product   amount   amount_in_eur
Burger     15.99       13.84
Pizza      22.50       19.48
Pasta      25.99       22.50
Laptop    850.00      735.92
```

The program generates:

* `cleaned_sales.csv`
* `sales_summary.csv`
* `sales_report.xlsx`
* `automation.log`

## Error Handling

The program handles common problems such as:

* Missing input files
* Missing required columns
* Invalid values in the `amount` column
* API connection errors

Errors and important program actions are recorded in `automation.log`.

## API Integration

The project uses a public exchange-rate API to retrieve a USD-to-EUR exchange rate.

The returned rate is used to create an additional column:

```text
amount_in_eur
```

## Future Improvements

Possible future improvements include:

* Support Excel input files
* Add more currencies
* Create charts and dashboards
* Add a graphical user interface
* Automate processing of multiple files

## Author

Navya Dava
