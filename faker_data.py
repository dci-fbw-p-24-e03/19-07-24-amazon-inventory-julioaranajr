import csv
from faker import Faker
from datetime import datetime, timedelta
import random

FILENAME = 'warehouse_inventory.csv'

def generate_fake_data(num_records=100):
    fake = Faker()
    data = []

    for _ in range(num_records):
        item = fake.word().capitalize()
        quantity = random.randint(1, 100)
        expiration_date = (datetime.now() + timedelta(days=random.randint(-365, 365))).strftime('%Y-%m-%d')
        price = round(random.uniform(1.0, 100.0), 2)
        data.append({
            'item': item,
            'quantity': quantity,
            'expiration_date': expiration_date,
            'price': price
        })
    
    return data

def save_fake_data(data):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['item', 'quantity', 'expiration_date', 'price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    num_records = 100  # Specify the number of records you want to generate
    fake_data = generate_fake_data(num_records)
    save_fake_data(fake_data)
    print(f"Generated {num_records} fake records and saved to {FILENAME}.")
