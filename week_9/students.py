import csv
import re

def main():
    INDEX_SDT = 0
    NAME_INDEX = 1
    student_dict = read_dictionary('students.csv', INDEX_SDT)
    # print(student_dict)

    while True:
        regex = '0-9'
        get_inumber = str(input("What is your i-number? "))
        if len(get_inumber) < 9 and re.match(regex, get_inumber):
            print('Invalid I-Number: too few digits')
        elif len(get_inumber) > 9 and re.match(regex, get_inumber):
            print('Too many digits')
        # elif not re.match(regex, get_inumber):
        elif len(get_inumber) == 9:
            if get_inumber in student_dict:
                print(student_dict[get_inumber][NAME_INDEX])
            else:
                print( 'No Such Number')
        else: 
            print('invalid inumber')


    

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
    with open(filename, 'rt') as f:
        reader = csv.reader(f)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary

if __name__ == "__main__":
    main()