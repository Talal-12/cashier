def get_invoice_items(items):
    # Items is a dictionary with a quantity and price key, and a name key
    # Return a list of all the invoice line items in the following format:
    # quantity name subtotal currency
    # For example, if we had the following:
    # [
    #   {'name': 'Apple', 'quantity': 1, price: 0.2 },
    #   {'name': 'Orange', 'quantity': 4, price: 0.3 },
    # ]
    # We should return the following:
    # ['1 Apple 0.200KD', '4 Orange 1.200KD']
    # ---
    # Write your code here
    items = [
        {"name" : "Apple", "quantity" : 1, "price" : .2},
        {"name" : "Orange", "quantity" : 4, "price" : .3},
             ]

    for item in items:
        invoice_items = [item['quantity'], item['name'], float(item['quantity'] * item['price'])]
    return invoice_items
    
    
    

def get_total(items):
    # Items is a dictionary with a quantity and price key
    # Calculate the total of all items in the cart
    # Write your code here
    total = 0
    for item in items:
        subtotal = [item['quantity'] * item['price']]
        return total + subtotal
    return total


def print_receipt(invoice_items, total):
    # invoice_items will be the list of formatted items received from
    # `get_invoice_items`, and total will be a float. Print out a nice receipt
    # displaying a title, all the invoice items on separate lines, and the
    # total at the end.
    # ---
    # Write your code here
    print("--------------------------")
    print("Receipt")
    print("--------------------------")
    
    for item in invoice_items:
        print(item[get_invoice_items])

    print("--------------------------")
    print("Total Price: " + float(total) + "KD")



def main():
    # Write your main logic here
    items = [
    {
        "name": "apples",
        "price": .2,
        "quantity": 4
    },
    {
        "name": "carrot",
        "price": .1,
        "quantity": 1 
    },
    {
        "name": "flour",
        "price": 1.3,
        "quantity": 2
    },
    {
        "name": "water bottles",
        "price": .05,
        "quantity": 10
    },
            ]

    while not "done":
        items["name"] = input('Item (enter "done" when finished): ')
        items["price"] = input("Price: ")
        items["quantity"] = input("Quantity: ")
    else:
        print(print_receipt)




if __name__ == "__main__":
    main()
