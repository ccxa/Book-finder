import requests
import bs4
import functions

# checking internet connection
functions.check_connection(requests)


def run():

    # getting authors name from wikipedia
    writer_list = functions.get_authors_name(requests, bs4)

    # selecting author by user inputted number
    writer_number = int(input('\nSelect an writer by its number\n>> ')) - 1
    writer = str(writer_list[writer_number]).replace(' ', '+')

    # Extract & print books of selected author from GoodReads
    functions.get_authors_books(requests, bs4, writer)

    functions.clear_console()

while True:
    functions.clear_console()
    print('Ready! > Book finder > menu')
    menu = input('[1]: Run\n[2]: How to use\n[3]: Exit\n>> ')

    if menu == '1':
        run()
    elif menu == '2':
        functions.help_message()
    elif menu == '3':
        functions.clear_console()
        exit()
    else:
        wait = input('Use numbers to select, Hit enter to try again.')
