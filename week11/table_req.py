from bs4 import BeautifulSoup
import requests
def main():

    # TODO error handling
    # TODO select a table from list of tables
    # TODO visualize table as output in terminal

    # page = requests.get("https://www.finder.com/gas-prices")
    # page = requests.get("https://afd.calpoly.edu/web/sample-tables")
    requested_url = input("Please enter your desired URL: [linux: ctrl+shift+v, windows: right-click]")
    page = requests.get(requested_url)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # div = soup.find('div.me')
    data = []
    table = soup.find_all('table')
    
    # data_from_table = get_cell_text(table, data)
    # print(data)


def get_cell_text(table, data_list):

    for row in table.find_all('tr'):
        for cell in row.find_all('td'):
            data_list.append(cell.get_text())

    return data_list

if __name__ == "__main__":
    main()