import pandas as pd
import pytest

from data_cleaner import (
    clean_data, 
    category_summary,
    validate_required_columns,
    validate_data_types,
)


def test_clean_data_removes_duplicates():
    data = pd.DataFrame({
        "order_id": [1, 1],
        "date": ["2026-09-01", "2026-09-01"],
        "product": ["Laptop", "Laptop"],
        "category": ["Electronics", "Electronics"],
        "amount": [100.0, 100.0],
        "city": ["Miami", "Miami"]
    })

    cleaned = clean_data(data)

    assert len(cleaned) == 1

def test_clean_data_fills_missing_amount():
    data = pd.DataFrame({
        "order_id": [1, 2, 3],
        "date": ["2026-09-01", "2026-09-02", "2026-09-03"],
        "product": ["Laptop", "Mouse", "Keyboard"],
        "category": ["Electronics", "Electronics", "Electronics"],
        "amount": [10.0, None, 30.0],
        "city": ["Miami", "Orlando", "Tampa"]
    })

    cleaned = clean_data(data)

    assert cleaned["amount"].isnull().sum() == 0
    assert cleaned.loc[1, "amount"] == 20.0

def test_category_summary():
    data = pd.DataFrame({
        "order_id": [1, 2, 3],
        "date": ["2026-09-01", "2026-09-02", "2026-09-03"],
        "product": ["Laptop", "Mouse", "Chair"],
        "category": ["electronics", "electronics", "furniture"],
        "amount": [100.0, 50.0, 200.0],
        "city": ["Miami", "Orlando", "Tampa"]
    })

    summary = category_summary(data)

    assert summary.loc["electronics", "sum"] == 150.0
    assert summary.loc["furniture", "sum"] == 200.0

def test_missing_required_column():
    data = pd.DataFrame({
        "order_id": [1],
        "date": ["2026-09-01"],
        "product": ["Laptop"],
        "category": ["electronics"],
        "city": ["Miami"]
    })

    with pytest.raises(ValueError):
        validate_required_columns(data)

def test_invalid_amount_data_type():
    data = pd.DataFrame({
        "order_id": [1],
        "date": ["2026-09-01"],
        "product": ["Laptop"],
        "category": ["electronics"],
        "amount": ["wrong"],
        "city": ["Miami"]
    })

    with pytest.raises(ValueError):
        validate_data_types(data)