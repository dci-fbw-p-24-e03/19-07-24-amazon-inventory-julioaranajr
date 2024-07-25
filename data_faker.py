"""
This module provides functions to generate and save fake inventory data using the Faker library.

The module includes the following functions:
- generate_fake_data(INVENTORY_RECORDS): Generates a specified number of fake inventory records.
- save_fake_data(data): Saves the generated fake inventory data to a CSV file.

Requires the Faker library to be installed. You can install it using pip:
    
    pip install Faker

Example usage:
    INVENTORY_RECORDS = 100  # Specify the number of records you want to generate
    fake_data = generate_fake_data(INVENTORY_RECORDS)
    save_fake_data(fake_data)
    print(f"Generated {INVENTORY_RECORDS} fake records and saved to {FILENAME}.")
"""

from datetime import datetime, timedelta
import csv
import random
from faker import Faker


FILENAME = "warehouse_inventory.csv"

def generate_fake_data(quantity=100):
    """Generates a specified number of fake inventory records.

    Args:
        quantity (int, optional): The number of records to generate. Defaults to 100.

    Returns:
        list: A list of dictionaries representing the generated inventory records.
    """
    fake = Faker()
    data = []

    for _ in range(quantity):
        item_id = fake.uuid4()
        item = fake.word().capitalize()
        gtin = fake.ean13()
        mpn = fake.ean8()
        company = fake.company()
        quantity = random.randint(1, 100)
        expiration_date = (
            datetime.now() + timedelta(days=random.randint(-365, 365))
        ).strftime("%Y-%m-%d")
        price = round(random.uniform(1.0, 100.0), 2)
        data.append(
            {
                "id": item_id,
                "item": item,
                "gtin": gtin,
                "mpn": mpn,
                "brand": company,
                "quantity": quantity,
                "expiration_date": expiration_date,
                "price": price,
            }
        )

    return data


def save_fake_data(data):
    """Saves the generated fake inventory data to a CSV file.

    Args:
        data (list): A list of dictionaries representing the inventory data to be saved.
    """
    with open(FILENAME, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = ["id", "item", "gtin", "mpn", "brand", "quantity", "expiration_date", "price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    INVENTORY_RECORDS = 100  # Specify the number of records you want to generate
    fake_data = generate_fake_data(INVENTORY_RECORDS)
    save_fake_data(fake_data)
    print(f"Generated {INVENTORY_RECORDS} fake records and saved to {FILENAME}.")
