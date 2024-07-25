"""
This module provides functions to manage inventory data in a CSV file.

The module includes the following functions:
- load_data(): Load data from the CSV file.
- save_data(data): Save data to the CSV file.
- add_item(data, item, quantity, expiration_date, price): Add an item to the data.
- remove_item(data, item): Remove an item from the data.
- update_item(data, item, quantity, expiration_date, price): Update an item in the data.
- get_full_report(data): Generate and print a full inventory report.
- search_item(data,item): search for an item in the data.
- get_expired_items(data): Get a list of expired items from the data.

Example usage:
    data = load_data()
    add_item(data, "Laptop", 10, "2023-12-31", 899.99)
    remove_item(data, "Tablet")
    update_item(data, "Phone", price=599.99)
    get_full_report(data)
    search_item(data,"laptop")
    get_expired_items(data)
"""

import csv
from datetime import datetime
import functools
import sys
import time
import pprint
from faker import Faker
from fpdf import FPDF


pprint = pprint.PrettyPrinter(indent=4)

FILENAME = 'warehouse_inventory.csv'

fake = Faker()

def load_data():
    """
    Load data from the CSV file.

    Returns:
        list: A list of dictionaries representing the data from the CSV file.
    """
    with open(FILENAME, mode='r', encoding="utf-8", newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

# Test the load_data function, you need to import pprint 1st.
# data = load_data()
# pprint(data, indent=4)

def save_data(data):
    """
    Save data to the CSV file.

    Args:
        data (list): A list of dictionaries representing the data to be saved.
    """
    with open(FILENAME, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = ["id", "item", "gtin", "mpn", "brand", "quantity", "expiration_date", "price"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def progress_bar(func):
    """
    Decorator function to display a progress bar while executing a function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('\nProcessing...')
        for i in range(21):
            time.sleep(0.1)
            sys.stdout.write('\r')
            sys.stdout.write("[%-20s] %d%%" % ('=' * i, 5 * i))
            sys.stdout.flush()
        print('\nDone')
        result = func(*args, **kwargs)
        return result
    return wrapper

def check_item_present(func):
    """
    Decorator function to check if an item is present in the data.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.
    """
    def wrapper(data, *args, **kwargs):
        item = kwargs.get('item')
        if any(d['item'] == item for d in data):
            return func(data, *args, **kwargs)
        else:
            print(f'Item {item} not found.')
            return
    return wrapper

@progress_bar
def add_item(data, item, quantity, expiration_date, price):
    """
    Add an item to the data.

    Args:
        data (list): A list of dictionaries representing the data.
        item (str): The name of the item to be added.
        quantity (int): The quantity of the item.
        expiration_date (str): The expiration date of the item in the format 'YYYY-MM-DD'.
        price (float): The price of the item.
    """
    data.append({
                "id": fake.uuid4(),
                "item": item,
                "gtin": fake.ean13(),
                "mpn": fake.ean8(),
                "brand": fake.company(),
                "quantity": quantity,
                "expiration_date": expiration_date,
                "price": price,
    })
    save_data(data)
    print(f"Item '{item}' added successfully.")

# Test the add_item function
# data = load_data()
# add_item(data, "Laptop", 10, "2023-12-31", 499.99)
# print(data)

@progress_bar
@check_item_present
def remove_item(data, item):
    """
    Remove an item from the data.

    Args:
        data (list): A list of dictionaries representing the data.
        item (str): The name of the item to be removed.
    """
    data = [d for d in data if d['item'].lower() != item.lower()]
    save_data(data)
    print(f"Item '{item}' removed successfully.")

@progress_bar
@check_item_present
def update_item(data, item, quantity=None, expiration_date=None, price=None):
    """
    Update an item in the data.

    Args:
        data (list): A list of dictionaries representing the data.
        item (str): The name of the item to be updated.
        quantity (int, optional): The new quantity of the item. Defaults to None.
        expiration_date (str, optional): 
        The new expiration date of the item in the format 'YYYY-MM-DD'. Defaults to None.
        price (float, optional): The new price of the item. Defaults to None.
    """
    for d in data:
        if d['item'] == item:
            if quantity is not None:
                d['quantity'] = quantity
            if expiration_date is not None:
                d['expiration_date'] = expiration_date
            if price is not None:
                d['price'] = price
    save_data(data)

def sort_by_expiration_date(data):
    """
    Sort the data by expiration date.

    Args:
        data (list): A list of dictionaries representing the data.

    Returns:
        list: The sorted data.
    """
    return sorted(data, key=lambda x: datetime.strptime(x['expiration_date'], '%Y-%m-%d'))

@progress_bar
def get_full_report(data) -> None:
    """
    Generate and print a full inventory report.

    Args:
        data (list): A list of dictionaries representing the data.
    """
    if not data:
        print("No items in the inventory.")
        return None
    data = sort_by_expiration_date(data)
    print("\nFull Inventory Report")
    print("-" * 71)
    print(f"|{'Item':<20} | {'Quantity':<10} | {'Expiration Date':<20} | {'Price':<10}|")
    print("-" * 71)
    for item in data:
        print(f"|{item['item']:<20} | {item['quantity']:<10} | {item['expiration_date']:<20} | {item['price']:<10}|")
    print("-" * 71)
# Test the get_full_report function
# data = load_data()
# get_full_report(data)


@progress_bar
def search_item(data, item) -> None:
    """
    Search for an item in the data.
    
    Args:
        data (list): A list of dictionaries representing the data.
        item (str): The name of the item to be searched.
    """
    found_items = [d for d in data if d['item']==item]
    print(f"\nSearch Results for '{item}'")
    print(f"{'Item':<20} {'Quantity':<10} {'Expiration Date':<20} {'Price':<10}|")
    print("-" * 71)
    for item in found_items:
        print(f"{item['item']:<20} {item['quantity']:<10} {item['expiration_date']:<20} {item['price']:<10}|")

@progress_bar
def get_expired_items(data) -> list:
    """
    Get a list of expired items from the data.
    
    Args:
        data (list): A list of dictionaries representing the data.
        
    Returns:
        list: A list of dictionaries representing the expired items.
    """
    today=datetime.today().date()
    expired_items =[d for d in data  if datetime.strptime(d['expiration_date'],'%Y-%m-%d').date() < today]
    if not expired_items:
        print('No expired items found.')
        return []
    expired_items=sort_by_expiration_date(expired_items)
    print("\nExpired Items")
    print("-" * 70)
    print(f"{'Item':<20} | {'Quantity':<10} | {'Expiration Date':<20} | {'Price':<10}|")
    print("-" * 70)
    for item in expired_items:
        print(f"{item['item']:<20} | {item['quantity']:<10} | {item['expiration_date']:<20} | {item['price']:<10}|")
    print("-" * 70)
    return expired_items

# Test the get_expired_items function
# data = load_data()
# get_expired_items(data)

def export_to_pdf(data):
    """
    Export the data to a PDF file.

    Args:
        data (list): A list of dictionaries representing the data.
    """
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Warehouse Inventory Report", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt="Full Inventory Report", ln=True, align="L")
    pdf.ln(5)
    pdf.cell(200, 10, txt="Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"), ln=True, align="L")
    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    col_width = 50
    row_height = 12
    for item in data:
        pdf.cell(col_width, row_height, txt=item['item'], border=1)
        pdf.cell(col_width, row_height, txt=str(item['quantity']), border=1)
        pdf.cell(col_width, row_height, txt=item['expiration_date'], border=1)
        pdf.cell(col_width, row_height, txt=str(item['price']), border=1)
        pdf.ln(row_height)
    pdf.output("inventory_report.pdf")

# Test the export_to_pdf function
# data = load_data()
# export_to_pdf(data)
