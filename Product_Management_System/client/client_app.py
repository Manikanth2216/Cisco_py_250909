import repo

def menu():
    message = '''

options
1 - Create Product
2 - List All Products
3 - Read Product By Id
4 - Update Product
5 - Delete Product
6 - Exit
Your Option:'''
    choice = int(input(message))
    if choice == 1:
        id = int(input('ID:'))
        name = input('Name:')
        price = float(input('Price:'))
        quantity = int(input('Quantity:'))  

        product = {'id':id, 'name':name, 'price':price, 'quantity':quantity}

        createdProduct = repo.create_product(product)
        print(f'Created:{createdProduct}')
        print('Product Created Successfully.')
    elif choice == 2:
        print('List of Products:')
        for product in repo.read_all_product():
            print(product)
    elif choice == 3:
        id = int(input('ID:'))
        product = repo.read_by_id(id)
        if product == None:
            print('Product not found.')
        else:
            print(product)
    elif choice == 4:
        id = int(input('ID:'))
        product = repo.read_by_id(id)
        if product == None: 
            print('Product Not Found')
        else:
            print(product)
            price = float(input('New Price:'))
            quantity = int(input('New Quantity:'))
            new_product = {
                'price':price,
                'quantity':quantity}
            updatedProduct = repo.update(id, new_product)
            print(f'Updated:{updatedProduct}')
            print('Product updated successfully.')
    elif choice == 5:
        id = int(input('ID:'))
        product = repo.read_by_id(id)
        if product == None: 
            print('Product Not Found')
        else:
            messageDict = repo.delete_product(id)
            #print('Product Deleted Succesfully.')
            print(messageDict['message'])
    elif choice == 6:
        print('Thank you for using the application.')
    return choice

def run_menu():
    choice = menu
    while choice != 6:
        choice = menu()
run_menu()
