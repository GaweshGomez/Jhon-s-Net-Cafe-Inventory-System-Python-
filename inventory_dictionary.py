import json
dealers = {
    'Gawesh Gomes': {
        'Telephone_Number': '+94761328236',
        'Dealer_Location':'Colombo',
        'items': [
            {
                'name': 'dell XPS Laptop',
                'brand': 'DELL',
                'price': 'RS. 590000.00',
                'quantity': '50'
            },
            {
                'name': 'Gaming keyboard',
                'brand': 'asus',
                'price': 'RS. 4900.00',
                'quantity': '30'
            },
            {
                'name': 'CPU',
                'brand': 'DELL',
                'price': 'RS. 220000.00',
                'quantity': '20'
            }
        ]
    },
    'Radil Damsara': {
        'Telephone_Number': '+94714325437',
        'Dealer_Location':'Kaluthara',
        'items': [
            {
                'name': 'flash drive',
                'brand': 'HP',
                'price': 'Rs. 12000.00',
                'quantity': '40'
            },
            {
                'name': 'Dell XPS 13',
                'brand': 'Dell',
                'price': 'Rs. 550000.00',
                'quantity': '15'
            },
            {
                'name': 'Air pods pro',
                'brand': 'APPLE',
                'price': 'Rs. 90000.00',
                'quantity': '40 '
            }
        ]
    },
    'Devindi_Perera': {
        'Telephone_Number': '+94754567242',
        'Dealer_Location':'Kiribathgoda',
        'items': [
            {
                'name': 'Redmi note 9 pro',
                'brand': 'Redmi',
                'price': 'Rs. 70000.00',
                'quantity': '8'
            },
            {
                'name': 'Gaming mouse',
                'brand': 'Asus',
                'price': 'Rs. 3900',
                'quantity': '16'
            },
            {
                'name': 'monitor',
                'brand': 'HP',
                'price': 'Rs. 80000.00',
                'quantity': '12'
            }
        ]
    },
    'Diyathma_wijewardhana': {
        'Telephone_Number': '+94769765434',
        'Dealer_Location':'Moratuwa',
        'items': [
            {
                'name': 'Iphone 14 pro max',
                'brand': 'Apple',
                'price': 'Rs. 649000.00',
                'quantity': '10'
            },
            {
                'name': 'computer lamp',
                'brand': 'orange',
                'price': 'Rs. 4800.00',
                'quantity': '50'
            },
            {
                'name': 'Iphone charger',
                'brand': 'apple',
                'price': 'Rs. 12000.00',
                'quantity': '40'
            }
        ]
    },
    'Sehandu_Siriwardhana': {
        'Telephone_Number': '+94786756453',
        'Dealer_Location':'kurunagala',
        'items': [
            {
                'name': 'laptop bags',
                'brand': 'asus',
                'price': 'Rs. 2500.00',
                'quantity': '50'
            },
            {
                'name': 'Headphone',
                'brand': 'samsung',
                'price': 'Rs. 3000.00',
                'quantity': '24'
            },
            {
                'name': 'SSD',
                'brand': 'Sandisk',
                'price': 'Rs. 10000.00',
                'quantity': '35'
            }
        ]
    },
    'Malindu_Dilshan': {
        'Telephone_Number': '+94772534657',
        'Dealer_Location':'Panadura',
        'items': [
            {
                'name': 'Memory card',
                'brand': 'Sandisk',
                'price': 'Rs. 4000.00',
                'quantity': '20'
            },
            {
                'name': 'Memory card readers',
                'brand': 'Ugreen',
                'price': 'Rs. 1000.00',
                'quantity': '45'
            },
            {
                'name': 'projector',
                'brand': 'ViewSonic',
                'price': 'Rs. 120000.00',
                'quantity': '18'
            }
        ]
    }
}



# Convert dictionary to JSON string
def ddd():
    dealers_json = json.dumps(dealers)

    # Write JSON string to file
    with open('dealers.txt', 'w') as file:
        file.write(dealers_json)




