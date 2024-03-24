from tabulate import tabulate
import json
import random
import inventory_dictionary
items_dictionary = {}

def intro():
    from tabulate import tabulate
    x=[
     ["••••••••••••••••••••••••••••••••••••••••••••••••WELCOME TO ONE NET CAFE - INVENTORY SYSTEM•••••••••••••••••••••••••••••••••••••••••••••••"],
        ]
    table1=tabulate(x,tablefmt="rounded_outline")
    print(table1)
    #table = tabulate(data, tablefmt="grid")

def main():
    #from colorama import Fore
    print( """\033[1m\033[32m
           • Type AID for adding item details.
           • Type DID for deleting item details.
           • Type UID for updating item details.
           • Type VID for viewing the items table.  
           • Type SID for saving the item details to the text file at any time.
           • Type SDD for selecting four dealers randomly from a file.
           • Type VRL for displaying all the details of the randomly selected dealers.  
           • Type LDI for display the items of the given dealer.
           • Type ESC to exit the program.
           \033[0m""")

def load_inventory():
    global items_dictionary
    try:
        with open("inventory.txt", "r") as file:
            item_dic = json.load(file)
    except FileNotFoundError:
        pass

def save_inventory():
    with open("inventory.txt", "w") as f:
        for item_code, item_details in items_dictionary.items():
            item_record = f"Item code: {item_code}|Item Name: {item_details['Item Name']}|Item Brand: {item_details['Item Brand']}|Item Price: {item_details['Item Price']}|Item Quantity: {item_details['Item Quantity']}|Item Category: {item_details['Item Category']}|Purchased Date: {item_details['Purchased Date']}\n"
            f.write(item_record)

def add_item():
    item_code = ""
    while not item_code:
        item_code = input("Enter Item Code: ")
        item_code=item_code.strip()
        if item_code in items_dictionary:
            print(f"\033[1m\033[94m{item_code} item already in inventory.\033[0m")
            item_code = ""
            continue

    item_name = ""
    while not item_name:
        item_name = input("Enter Item Name: ")
        item_name=item_name.strip()

    item_brand = ""
    while not item_brand:
        item_brand = input("Enter Item Brand: ")
        item_brand=item_brand.strip()

    item_price = ""
    while not item_price:
        try:
            item_price = float(input("Enter Item Price: "))
            #item_price=item_price.strip()
        except ValueError:
            print(f"\033[1m\033[31mInvalid input. Please enter a valid number value.\033[0m")
            continue

    item_quantity = ""
    while not item_quantity:
        try:
            item_quantity = int(input("Enter Item Quantity: "))
            #item_quantity=item_quantity.strip()
        except ValueError:
            print(f"\033[1m\033[31mInvalid input. Please enter a valid integer value.\033[0m")
            continue

    item_category = ""
    while not item_category:
        item_category = input("Enter Item Category: ")
        item_category=item_category.strip()

    purchased_date = ""
    while not purchased_date:
        purchased_date = input("Enter Purchased Date (DD/MM/YYYY): ")
        purchased_date=purchased_date.strip()

        item_details = {"Item Name": item_name,
                        "Item Brand": item_brand,
                        "Item Price": item_price,
                        "Item Quantity": item_quantity,
                        "Item Category": item_category,
                        "Purchased Date": purchased_date}

        items_dictionary[item_code] = item_details
        print(f"\033[1m\033[92m{item_name} ({item_code}) added to inventory.\033[0m")
        save_inventory()

def delete_item():
    item_code = input("Enter Item Code: ")
    if item_code in items_dictionary:
        del items_dictionary[item_code]
        #print(f"{item_code} deleted from inventory.")
        print(f"\033[1m\033[93m{item_code} deleted from inventory.\033[0m")
        save_inventory()
    else:
        #print(f"{item_code} not found in inventory.")
        print(f"\033[1m\033[31m{item_code} not found in inventory.\033[0m")

def update_item():
    item_code = input("Enter Item Code: ")
    if item_code in items_dictionary:
        print(f"\033[1m\033[36mEnter new details for the item (Leave blank for no change):\033[0m")
        item_name = input(f"Current Item Name: {items_dictionary[item_code]['Item Name']}\nNew Item Name: ")
        item_name=item_name.strip()
        item_brand = input(f"Current Item Brand: {items_dictionary[item_code]['Item Brand']}\nNew Item Brand: ")
        item_brand=item_brand.strip()
        while True:
            try:
                item_price = float(input(f"Current Item Price: {items_dictionary[item_code]['Item Price']}\nNew Item Price: "))
                break
            except ValueError:
                print(f"\033[1m\033[31mInvalid input. Please enter a valid number value.\033[0m")
        while True:
            try:
                item_quantity = int(input(f"Current Item Quantity: {items_dictionary[item_code]['Item Quantity']}\nNew Item Quantity: "))
                break
            except ValueError:
                print(f"\033[1m\033[31mInvalid input. Please enter a valid number value.\033[0m")
        item_category = input(f"Current Item Category: {items_dictionary[item_code]['Item Category']}\nNew Item Category: ")
        item_category=item_category.strip()
        purchased_date = input(f"Current Purchased Date: {items_dictionary[item_code]['Purchased Date']}\nNew Purchased Date (DD/MM/YYYY): ")
        purchased_date=purchased_date.strip()

        if item_name:
            items_dictionary[item_code]['Item Name'] = item_name
        if item_brand:
            items_dictionary[item_code]['Item Brand'] = item_brand
        if item_price:
            items_dictionary[item_code]['Item Price'] = float(item_price)
        if item_quantity:
            items_dictionary[item_code]['Item Quantity'] = int(item_quantity)
        if item_category:
            items_dictionary[item_code]['Item Category'] = item_category
        if purchased_date:
            items_dictionary[item_code]['Purchased Date'] = purchased_date
        save_inventory()
        print(f"\033[1m\033[92m {item_code} ({item_name}) details updated.\033[0m")
        #print(f"{item_code}{item_name} details updated.")
    else:
        print(f"\033[1m\033[31m{item_code} not found in inventory.\033[0m") #red

def view_items():
    if not items_dictionary:
       # print("No items found!")
        print("\033[1m\033[31mNo items found!\033[0m")
    else:
        items = []
        total_purchased_items = 0
        for item_code, item_details in items_dictionary.items():
            items.append([item_code, item_details["Item Name"], item_details["Item Brand"], item_details["Item Price"], item_details["Item Quantity"], item_details["Item Category"], item_details["Purchased Date"]])
            total_purchased_items += item_details["Item Quantity"]
        #headers = ["Item ID", "Item Name", "Item Brand", "Item Price", "Item Quantity", "Item Category", "Purchased Date"]
        #print(tabulate(items, headers=headers, tablefmt="heavy_grid"))
        items = sorted(items, key=lambda x: x[0], reverse=True)

        headers = ["\033[1mItem ID\033[0m", "\033[1mItem Name\033[0m", "\033[1mItem Brand\033[0m","\033[1mItem Price\033[0m", "\033[1mItem Quantity\033[0m", "\033[1mItem Category\033[0m","\033[1mPurchased Date\033[0m"]
        print(tabulate(items, headers=headers, tablefmt="heavy_grid"))
        #print("Total Purchased Items: {}".format(total_purchased_items))
        print("\033[1m\033[93mTotal Purchased Items: {}\033[0m".format(total_purchased_items))

while True:

    intro()
    main()

    choice = input("Enter your choice: ")
    choice = choice.upper()
    if choice == 'AID':
        add_item()
        print()

    elif choice == 'DID':
        delete_item()
    elif choice == 'VID':
        view_items()
        print()
    elif choice == 'UID':
        update_item()
        print()


    elif choice == 'SDD':
        dictionary.ddd()
        try:

            with open('dealers.txt', 'r') as file:
                dealers_json = file.read()
                dealers = json.loads(dealers_json)

            random_dealers = random.sample(list(dealers.keys()), 4)
            print("\033[1m\033[34m4 Dealers are selected Randomly\033[0m")
            print()
        except:
            print("\033[1m\033[31mFile Not Found!\033[0m")


    elif choice == 'VRL':

        try:
            for i in range(len(random_dealers)):
                for j in range(len(random_dealers) - i - 1):
                    if dealers[random_dealers[j]]['Location'] > dealers[random_dealers[j + 1]]['Location']:
                        random_dealers[j], random_dealers[j + 1] = random_dealers[j + 1], random_dealers[j]

            rows = []
            for dealer in random_dealers:
                dealer_row = [dealer, dealers[dealer]['Contact_Number'], dealers[dealer]['Location']]
                rows.append(dealer_row)
                for item in dealers[dealer]['items']:
                    item_row = [None, None, None, item['Item_name'], item['brand'],item['price'], item['quantity']]
                    rows.append(item_row)

            headers = ['Dealer Name', 'Contact Number', 'Location', 'Item Name', 'Brand','price', 'Quantity']
            print(tabulate(rows, headers=headers))
        except:
            print("\033[1m\033[31mYou have not selected any dealers yet!!!\033[0m")

    elif choice == 'LDI':
        try:
            dealer_name = input("Enter Dealer Name ( Please select from the randomly selected dealer table ) : ")
            dealer_name=dealer_name.strip()

            if dealer_name in random_dealers:
                print(f"\033[1m\033[36mDealer name:  {dealer_name}\033[0m ")


                get_dealer=[]

                for item in dealers[dealer_name]['items']:
                    item_row = [item['Item_name'], item['brand'], item['quantity'],item['price']]
                    get_dealer.append(item_row)
                headers = ['\033[1mItem Name\033[0m', '\033[1mBrand\033[0m', '\033[1mQuantity\033[0m','\033[1mPrice\033[0m']
                print(tabulate(get_dealer, headers=headers, tablefmt='heavy_grid'))

            else:
                #print("Dealer not found!")
                print("\033[1m\033[31mDealer not found! (Please use randomly selected deslers...) \033[0m")
        except:
            print("\033[1m\033[31mThere are no Randomly Selected Dealers. Please go through the 'SDD' Operation...\033[0m")

    elif choice=='SID':
        save_inventory()
        print(f"\033[1m\033[92mInventory saved to file.\033[0m")

    elif choice == 'ESC':
        #print("Good Bye! Have a nice Day")
        print("\033[1m\033[36mGood Bye! Have a nice Day...\033[0m")
        break

    else:
        #print("Invalid choice. Please try again.")
        print("\033[1m\033[31mInvalid choice. Please try again.\033[0m")

