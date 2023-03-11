import csv
import datetime

def main():
    filename = 'request.csv'
    receipt_index = 0
    products_dict = read_dictionary('products.csv', receipt_index)
    # print('All Products')
    # print(products_dict)
    print()
    print("Fallmart Store")

    P_NUMBER_INDEX = 0
    QUANTITY_INDEX = 1
    
    subtotal = 0
    with_tax = 0
    tax_rate = .06
    quantity_total = 0
    thank_you_msg = 'Thank you for choosing Fallmart, your local neighborhood grocery.'
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime('%m-%d-%Y %H:%M')
    # TODO complete survey module after total amount prints
    
    print('\nRequested Items')
    try:
        with open(filename, 'rt') as f:
            reader = csv.reader(f)
            next(reader)
            for row_list in reader:
                # print(products_dict[row_list[0]])
                requested_item = products_dict[row_list[0]]
                requested_qty = row_list[1]
                quantity_total += int(requested_qty)
                product_price = requested_item[2]
                subtotal += float(product_price) * int(requested_qty)
                product_name = requested_item[1]
                print(f'{product_name}: {requested_qty} @ {product_price}')
    except FileNotFoundError as not_file:
        print()
        print(f"The file, {filename} does not exist.")
        print(f'Python sees this instead{not_file}')
    except PermissionError as perm_err:
        print()
        print(f'You do not have correct permissions to read {filename}.')
        print('Try again or fix your file permissions.')
    except KeyError as key_err:
        print()
        print(f'Python had a key error: {key_err}.')
        print('Please check your file data to make sure everything is correct.')

    print()
    print(f'Total number of items: {quantity_total}')
    with_tax = subtotal * (1 + tax_rate)
    print()
    print(f'Subtotal: {subtotal:.2f}')
    print(f'Total (6% Tax): {with_tax:.2f}')
    print()
    print(thank_you_msg)
    print()
    print(' As our valued customer, we invite you to take a survey \n \
today at https://tinyurl.com/2y9zk233. With every survey,\n \
we will enter you in our raffle to win a new GMC.')
    print()
    print(formatted_date)

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
    dict = {}

    with open(filename, "rt") as f:
        reader = csv.reader(f)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dict[key] = row_list
    return dict

if __name__ == "__main__":
    main()