"""
This is the main file that will be run to start the program. 
It will display a menu of options to the user and allow them 
to interact with the inventory management system.
"""
import pprint
from amazon_inventory import load_data, add_item, remove_item, update_item
from amazon_inventory import get_full_report, get_expired_items, search_item
from amazon_inventory import export_to_pdf

pprint = pprint.PrettyPrinter(indent=4)

def main():
    """
    The main function that will be run to start the program.
    """
    data = load_data()
    while True:
        print("\nWarehouse Inventory Management\n")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View All Items")
        print("5. Get Full Report")
        print("6. Get Expired Items")
        print("7. Search for an Item")
        print("8. Export Full Report to PDF")
        print("q. Exit\n")
        choice = input("Choose an option: ")
        if choice == '1':
            item = input("Enter item name: ")
            quantity = input("Enter quantity: ")
            expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
            price = input("Enter price: ")
            data = add_item(data, item, quantity, expiration_date, price)
        elif choice == '2':
            item = input("Enter item name to remove: ")
            data = remove_item(data, item=item)
        elif choice == '3':
            item = input("Enter item name to update: ")
            quantity = input("Enter new quantity (leave blank to keep current): ")
            expiration_date = input("Enter new expiration date (YYYY-MM-DD, leave blank to keep current): ")
            price = input("Enter new price (leave blank to keep current): ")
            update_item(data, item=item, quantity=quantity if quantity else None,
                               expiration_date=expiration_date if expiration_date else None,
                               price=price if price else None)
        elif choice == '4':
            pprint.pprint(data)
        elif choice == '5':
            get_full_report(data)
        elif choice == '6':
            get_expired_items(data)
        elif choice == '7':
            item_name = input("Enter the name of the item to search for: ")
            search_item(data, item_name)
        elif choice == '8':
            export_to_pdf(data)
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
