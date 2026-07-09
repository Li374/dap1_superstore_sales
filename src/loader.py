import pandas as pd

DATE_COLUMNS = [
    "Order Date",
    "Ship Date"
]

DTYPE_MAP = {
    "Postal Code": "string"
}

def load_clean_data(path):
    return pd.read_csv(
        path,
        parse_dates=DATE_COLUMNS,
        dtype=DTYPE_MAP
    )