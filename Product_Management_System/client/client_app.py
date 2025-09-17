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
    try:
        choice = int(input(message))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0
    
    try:
        if choice == 1:
            id = int(input('ID:'))
            name = input('Name:')
            price = float(input('Price:'))
            qty = int(input('Quantity:'))  

            product = {'id':id, 'name':name, 'price':price, 'qty':qty}

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
            print(product)
        elif choice == 4:
            id = int(input('ID:'))
            product = repo.read_by_id(id)
            print(product)
            price = float(input('New Price:'))
            new_product ={
                'price':price,
            }
            updatedProduct = repo.update(id, new_product)
            print(f'Updated:{updatedProduct}')
            print('Product updated successfully.')

        elif choice == 5:
            id = int(input('ID:'))
            product = repo.read_by_id(id)
            messageDict = repo.delete_product(id)
            print('Product Deleted Succesfully.')
            print(messageDict['message'])
            
        elif choice == 6:
            print('Thank you for using the application.')
            return 6

        else:
            print("Invalid option. Please choose a number between 1 and 6.")

    
    except repo.ProductNotFound as ex:
        print(f"{ex}")
    except repo.ProductAlreadyExistError as ex:
        print(f"{ex}")
    except repo.DatabaseError as ex:
        print(f"{ex}")

def run_menu():
    while True:
        choice = menu()
        if choice == 6:
            break
run_menu()
