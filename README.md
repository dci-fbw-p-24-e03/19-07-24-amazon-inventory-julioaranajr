# Warehouse Inventory Management System

This Python project simulates a warehouse inventory management system similar to Amazon's warehouse. It allows users to add, remove, update items, generate fake data using Faker, and save/load data to/from a CSV file.

## Features

- **Add Item**: Add a new item to the inventory.
- **Search for an Item**: Search for an item by name.
- **Remove Item**: Remove an item from the inventory.
- **Update Item**: Update the quantity, expiration date, or price of an existing item.
- **View All Items**: Display all items currently in the inventory.
- **Sort Items by Expiration Date**: Sort and display items based on their expiration dates.
- **Generate Fake Data**: Automatically generate fake inventory data using Faker.
- **Save/Load Data**: Data is saved and loaded from a CSV file (`warehouse_inventory.csv`).
- **Export Full Report to PDF**: Export the full inventory report to a PDF file.

## Dependencies

- Python 3.x
- Faker library (`pip install faker`)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

## Usage

1. **Generate Fake Data**: Run `data_faker.py` to populate `warehouse_inventory.csv` with fake data.

   ```bash
   python data_faker.py
   ```

2. **Run the Warehouse Management System**:

   ```bash
   python main.py
   ```

3. Follow the on-screen instructions to interact with the system:
   - Add, remove, update items.
   - View all items or sort them by expiration date.
   - Use the search function to find specific items.

## Example

Here's an example of how to add an item using the command line interface:

```bash
$ python main.py

Warehouse Inventory Management

1. Add Item
2. Remove Item
3. Update Item
4. View All Items
5. Get Full Report
6. Get Expired Items
7. Search for an Item
8. Export Full Report to PDF
q. Exit

Choose an option: 

Enter item name: Laptop
Enter quantity: 10
Enter expiration date (YYYY-MM-DD): 2024-12-31
Enter price: 999.99

Item 'Laptop' added successfully.
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

### Notes

- Replace `<repository_url>` and `<repository_name>` with your actual repository URL and name.
- Ensure to update the example with relevant command outputs and interactions based on your project's functionality.

This README template provides a structured overview of your project, including installation instructions, usage examples, and licensing information. Adjust it further based on any specific details or additional features your project may have.
