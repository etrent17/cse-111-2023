import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    # with open("pupils.csv", "r") as pupil_list:
        # students_list = pupil_list
    students_list = read_compound_list("pupils.csv")
    birthdays = []
    bday_func = lambda student: student[BIRTHDATE_INDEX]
    # def birthday(c_list, b_list):
    #     for i in c_list(BIRTHDATE_INDEX):
    #                     b_list.append(i)
    # print_birthday = birthday(students_list)
    sorted_list = sorted(students_list, key=bday_func)
    reversed_list = sorted_list.reverse()
    # students_list = students_list.sort(key=birthday(students_list))
    # students_list = students_list.sort(reverse = True)

    # students_list.reverse()
    print_list(reversed_list)

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list

def print_list(compound_list):
    for i in compound_list:
        print(i)

if __name__ == "__main__":
    main()