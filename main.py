from tabulate import tabulate
import json
import random
import inventory_dictionary
items_dictionary = {}

def inventory_introduction():
    from tabulate import tabulate

    head=[["WELCOME TO ONE NET CAFE - INVENTORY SYSTEM" ] ]

    print(tabulate(head,tablefmt="double_grid"))

    #table = tabulate(data, tablefmt="grid")

def main():
    #from colorama import Fore
    print( """\033[3m
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

def inventory_load():
    global items_dictionary
    try:
        with open("inventory.txt", "r") as file:
            items_dictionary = json.load(file)
    except FileNotFoundError:
        pass

def inventory_save():
    with open("inventory.txt", "w") as f:
        for i_code, i_details in items_dictionary.items():
            item_record = f" 'Item code'= {i_code}, 'Item name'={i_details['I Name']},'Item brand'={i_details['I Brand']}, 'Item price'={i_details['I Price']},'Quantity'={i_details['I Quantity']}, 'category'= {i_details['I Category']} 'Purchased Date'= {i_details['I Purchased Date']}\n"
            f.write(item_record)

def adding_item_details():
    i_code = ""
    while not i_code:
        i_code = input("Enter Item Code: ")
        i_code=i_code.strip()
        if i_code in items_dictionary:
            print(f"\033[1m\033[94m{i_code} item already in inventory.\033[0m")
            i_code = ""
            continue

    i_name = ""
    while not i_name:
        i_name = input("Enter Item Name: ")
        i_name=i_name.strip()

    i_brand = ""
    while not i_brand:
        i_brand = input("Enter Item Brand: ")
        i_brand=i_brand.strip()

    i_price = ""
    while not i_price:
        try:
            i_price = float(input("Enter Item Price: "))
            #i_price=i_price.strip()
        except ValueError:
            print(f"\033[1m\033[31mInvalid input. Please enter a valid number value.\033[0m")
            continue

    i_quantity = ""
    while not i_quantity:
        try:
            i_quantity = int(input("Enter Item Quantity: "))
        except ValueError:
            print(f"\033[1m\033[31mInvalid input. Please enter a valid integer value.\033[0m")
            continue

    i_category = ""
    while not i_category:
        i_category = input("Enter Item Category: ")
        i_category=i_category.strip()

    item_purchased_date = ""
    while not item_purchased_date:
        item_purchased_date = input("Enter Purchased Date (DD/MM/YYYY): ")
        item_purchased_date=item_purchased_date.strip()

        i_details = {"I Name": i_name,
                        "I Brand": i_brand,
                        "I Price": i_price,
                        "I Quantity": i_quantity,
                        "I Category": i_category,
                        "I Purchased Date": item_purchased_date}

        items_dictionary[i_code] = i_details
        print(f"\033[1m\033[92m{i_name} ({i_code}) added to inventory.\033[0m")
        inventory_save()

def deleting_item():
    i_code = input("Enter Item Code: ")
    if i_code in items_dictionary:
        del items_dictionary[i_code]
        print(f"\033[1m\033[93m{i_code} deleted from inventory.\033[0m")
        inventory_save()
    else:
        print(f"\033[1m\033[31m{i_code} not found in inventory.\033[0m")

def updating_item():
    i_code = input("Enter Item Code: ")
    if i_code in items_dictionary:
        print(f"\033[1m\033[36mNew details for the item (Dont Enter Anything If you need to keep the recent record.):\033[0m")
        i_name = input(f"Previous Item Name: {items_dictionary[i_code]['I Name']}\nNew Item Name: ")
        i_name=i_name.strip()
        i_brand = input(f"Previous Item Brand: {items_dictionary[i_code]['I Brand']}\nNew Item Brand: ")
        i_brand=i_brand.strip()
        while True:
            try:
                i_price = float(input(f"Previous Item Price: {items_dictionary[i_code]['I Price']}\nNew Item Price: "))
                break
            except ValueError:
                print(f"\033[1m\033[31mInvalid input. Please enter a valid number value.\033[0m")
        while True:
            try:
                i_quantity = int(input(f"Previous Item Quantity: {items_dictionary[i_code]['I Quantity']}\nNew Item Quantity: "))
                break
            except ValueError:
                print(f"\033[1m\033[31mInvalid input. Please enter a valid number value.\033[0m")
        i_category = input(f"Previous Item Category: {items_dictionary[i_code]['I Category']}\nNew Item Category: ")
        i_category=i_category.strip()
        item_purchased_date = input(f"Previous Purchased Date: {items_dictionary[i_code]['I Purchased Date']}\nNew Purchased Date (DD/MM/YYYY): ")
        item_purchased_date=item_purchased_date.strip()

        if i_name:
            items_dictionary[i_code]['I Name'] = i_name
        if i_brand:
            items_dictionary[i_code]['I Brand'] = i_brand
        if i_price:
            items_dictionary[i_code]['I Price'] = float(i_price)
        if i_quantity:
            items_dictionary[i_code]['I Quantity'] = int(i_quantity)
        if i_category:
            items_dictionary[i_code]['I Category'] = i_category
        if item_purchased_date:
            items_dictionary[i_code]['I Purchased Date'] = item_purchased_date
        inventory_save()
        print(f"\033[1m\033[92m {i_code} ({i_name}) details updated.\033[0m")
        #print(f"{i_code}{i_name} details updated.")
    else:
        print(f"\033[1m\033[31m{i_code} not found in inventory.\033[0m") #red

def viewing_items():
    if not items_dictionary:
       # print("No items found!")
        print("\033[1m\033[31mNo items found!\033[0m")
    else:
        items = []
        total_purchased_items = 0
        for i_code, item_details in items_dictionary.items():
            items.append([i_code, item_details["I Name"], item_details["I Brand"], item_details["I Price"], item_details["I Quantity"], item_details["I Category"], item_details["I Purchased Date"]])
            total_purchased_items += item_details["I Quantity"]
        #headers = ["Item ID", "Item Name", "Item Brand", "Item Price", "Item Quantity", "Item Category", "Purchased Date"]
        #print(tabulate(items, headers=headers, tablefmt="heavy_grid"))
        items = sorted(items, key=lambda x: x[0], reverse=True)

        headers = ["\033[1mItem code\033[0m", "\033[1mItem Name\033[0m", "\033[1mItem Brand\033[0m","\033[1mItem Price\033[0m", "\033[1mItem Quantity\033[0m", "\033[1mItem Category\033[0m","\033[1mPurchased Date\033[0m"]
        print(tabulate(items, headers=headers, tablefmt="heavy_grid"))
        #print("Total Purchased Items: {}".format(total_purchased_items))
        print("\033[1m\033[93mTotal Purchased Items: {}\033[0m".format(total_purchased_items))

while True:

    inventory_introduction()
    main()

    choice = input("Enter your choice: ")
    choice = choice.upper()
    if choice == 'AID':
        adding_item_details()
        print()

    elif choice == 'DID':
        deleting_item()
    elif choice == 'VID':
        viewing_items()
        print()
    elif choice == 'UID':
        updating_item()
        print()


    elif choice == 'SDD':
        inventory_dictionary.ddd()
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
                    if dealers[random_dealers[j]]['Dealer_Location'] > dealers[random_dealers[j + 1]]['Dealer_Location']:
                        random_dealers[j], random_dealers[j + 1] = random_dealers[j + 1], random_dealers[j]

            rows = []
            for dealer in random_dealers:
                d_row = [dealer, dealers[dealer]['Telephone_Number'], dealers[dealer]['Dealer_Location']]
                rows.append(d_row)
                for item in dealers[dealer]['items']:
                    i_row = [None, None, None, item['name'], item['brand'], item['price'], item['quantity']]
                    rows.append(i_row)

            headers = ['Dealer Name', 'Contact Number', 'Location', 'Item Name', 'Brand','price', 'Quantity']
            print(tabulate(rows, headers=headers))
        except:
            print("\033[1m\033[91mYou have not selected any dealers yet!!!\033[0m")

    elif choice == 'LDI':
        try:
            dealer_name = input("Enter Dealer Name ( Please select from the randomly selected dealer table ) : ")
            dealer_name=dealer_name.strip()

            if dealer_name in random_dealers:
                print(f"\033[1m\033[36mDealer name:  {dealer_name}\033[0m ")


                get_dealer=[]

                for item in dealers[dealer_name]['items']:
                    i_row = [item['name'], item['brand'], item['quantity'], item['price']]
                    get_dealer.append(i_row)
                headers = ['\033[1mItem Name\033[0m', '\033[1mBrand\033[0m', '\033[1mQuantity\033[0m','\033[1mPrice\033[0m']
                print(tabulate(get_dealer, headers=headers, tablefmt='heavy_grid'))

            else:
                #print("Dealer not found!")
                print("\033[1m\033[31mDealer is not in the system (Please use randomly selected dealers...) \033[0m")
        except:
            print("\033[1m\033[31mThere are no any randomly selected dealers. Please try again the 'SDD'...\033[0m")

    elif choice=='SID':
        inventory_save()
        print(f"\033[1m\033[92mInventory saved.\033[0m")

    elif choice == 'ESC':
        print("Thankyou")
        break

    else:
        print("\033[1m\033[31mInvalid choice.Try again.\033[0m")

