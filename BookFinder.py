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

    functions.clear_console()
    print('Loading [IIIIII                  ] 1/4\n')

    # getting authors books from goodReads
    base_url = 'https://www.goodreads.com'
    query = base_url + '/search?utf8=%E2%9C%93&q='\
        + writer \
        + '&search_type=lists'
    page = requests.get(query)
    soup = bs4.BeautifulSoup(page.content)
    link = soup.find('a', 'listTitle')

    functions.clear_console()
    print('Loading [IIIIIIIIII              ] 2/4\n')

    link = str(link).split('"')
    page2 = requests.get(base_url + link[3])

    functions.clear_console()
    print('Loading [IIIIIIIIIIIIIIII        ] 3/4\n')

    soup2 = bs4.BeautifulSoup(page2.content)

    functions.clear_console()
    print('Loading [IIIIIIIIIIIIIIIIIIIIIIII] 4/4\n')

    books = soup2.findAll('a', 'bookTitle')
    functions.clear_console()

    # printing authors book found on goodReads
    print('Writen by:', writer.replace('+', ' '), '\n')
    try:
        counter = 1
        for book in books:
            book = str(book).split('"')
            book = book[3][11:]
            forbidList = '0123456789.'
            bookName = ''
            for w in book:
                if w not in forbidList:
                    bookName = bookName + w
            bookName = bookName.replace('_', ' ').replace('-', ' ')
            if bookName[0] == ' ':
                bookName = bookName[1:]
            print(str(counter).zfill(2), '-', bookName)
            counter += 1
            if counter > 10:
                break
        wait = input('\nHit enter to go menu.')
    except:
        wait = input('Error!\nThere is not books for this author in goodreads.com')


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
