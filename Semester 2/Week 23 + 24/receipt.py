import csv
import webbrowser
from datetime import datetime
current_date_and_time = datetime.now()

filename = 'products.csv'
key_column_index = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary

def main(filename, key_column_index): 
    try:
        products_dict = read_dictionary(filename, key_column_index)
        with open('request.csv', 'rt') as request_file:
            reader = csv.reader(request_file)
            next(reader)
            print('Inkom Emporium\n')
            items = 0
            subtotal = 0
            for row_list in reader:
                key = row_list[0]
                product_name = products_dict[key]
                name = product_name[1]
                requested_quantity = row_list[1]
                product_price = products_dict[key]
                price = product_price[2]
                print(f'{name.capitalize()}: {requested_quantity} @ {price}')
                items += int(requested_quantity)
                subtotal += float(price)
            print(f'\nNumber of Items: {items}')
            print(f'Subtotal: {subtotal:.2f}')
            salestax = subtotal * .06
            print(f'Salestax: {salestax:.2f}')
            total = subtotal + salestax
            if datetime.today().weekday() == 1:
                total = total * .1
            elif datetime.now().hour < 11:
                total = total * .1
            print(f'Total: {total:.2f}')
            print('\nThank you for shopping at the Inkom Emporium.')
            print(f"{current_date_and_time:%A %B %d %I:%M:%S %Y}")
            yes = input('\nWould you like to complete an online survey for rewards? ').lower()
            if yes.startswith('y'):
                webbrowser.open('https://shanebasham.github.io/PythonMessingAround/wdd130/wwr/contactus.html')

    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print('No such file or directory. Please choose a different file.')
    except (KeyError) as key_error:
        print(f'{type(key_error).__name__}: unknown product ID in the request.csv file {key_error}')
        
if __name__ == "__main__":
    main(filename, key_column_index)