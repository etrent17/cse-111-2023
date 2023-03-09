import csv

def main():
    receipt_index = 0
    products_dict = read_dictionary('products.csv', receipt_index)
    print('All Products')
    print(products_dict)

    P_NUMBER_INDEX = 0
    QUANTITY_INDEX = 1
    print('\nRequested Items')

    with open('request.csv', 'rt') as f:
        reader = csv.reader(f)
        next(reader)
        for row_list in reader:
            # print(products_dict[row_list[0]])
            requested_item = products_dict[row_list[0]]
            requested_qty = row_list[1]
            product_price = requested_item[2]
            product_name = requested_item[1]
            print(f'{product_name}: {requested_qty} @ {product_price}')




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