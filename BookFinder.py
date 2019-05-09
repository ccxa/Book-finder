import requests
import bs4
import functions

# checking internet connection
functions.check_connection(requests)


def run():
    functions.clear_console()
    # authors name

    # Getting first letter of users first & last name
    first_name = input('Enter your First name:\n>> ').upper()
    last_name = input('Enter your last name\n>> ').upper()
    ffl, lfl = first_name[0], last_name[0]

    base_url = 'https://en.m.wikipedia.org'
    page = requests.get(base_url + '/wiki/List_of_authors_by_name:_' + lfl)
    soup = bs4.BeautifulSoup(page.content)
    names = soup.findAll('a')
    print('\nLoading ...\n')

    functions.clear_console()

    writer_list = []
    counter = 1
    for name in names:
        if name.string is None:
            continue
        elif name.string[0] == ffl and len(name.string) > 1:
            print(str(counter).zfill(2),end='')
            print('-',name.string)
            counter+=1
            writer_list.append(name.string)
    #authors book
    try :
        writer_number = int(input('\nSelect an writer by its number\n>> ')) - 1
        writer = str(writer_list[writer_number]).replace(' ','+')
        functions.clear_console()
        print('Loading [IIIIII                  ] 1/4\n')
        base_url = 'https://www.goodreads.com'
        query = base_url + '/search?utf8=%E2%9C%93&q=' + writer + '&search_type=lists'
        page = requests.get(query)
        soup = bs4.BeautifulSoup(page.content)
        link = soup.find('a','listTitle')

        functions.clear_console()
        print('Loading [IIIIIIIIII              ] 2/4\n')

        link = str(link).split('"')
        page2 = requests.get(base_url+link[3])

        functions.clear_console()
        print('Loading [IIIIIIIIIIIIIIII        ] 3/4\n')

        soup2 = bs4.BeautifulSoup(page2.content)
        functions.clear_console()
        print('Loading [IIIIIIIIIIIIIIIIIIIIIIII] 4/4\n')
        books = soup2.findAll('a','bookTitle')
        functions.clear_console()
        print('Writen by:',writer.replace('+',' '),'\n')
        counter = 1
        for book in books:
            book = str(book).split('"')
            book = book[3][11:]
            forbidList = '0123456789.'
            bookName = ''
            for w in book:
                if w not in forbidList:
                    bookName = bookName + w
            bookName = bookName.replace('_',' ').replace('-',' ')
            if bookName[0] == ' ':
                bookName = bookName[1:]
            print(str(counter).zfill(2),'-',bookName)
            counter+=1
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
