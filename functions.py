import os


def check_connection(requests):
    clear_console()
    print("Checking connection ... ")
    # checking connection
    try:
        test = requests.get('http://www.google.com')
    except Exception as e:
        print(e)
        print('You have to connected to internet.')
        _exit = input('Make sure you are connected. Hit Enter to exit.')
        exit()


def clear_console():
    command = 'clear'
    # use cls on windows systems instead
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def help_message():
    clear_console()

    print('''Book finder > How to use.
------------------------------------------------------
>This program will find authors who are compatible with your
 first & last names first letter.
 !!! you may receive unwanted results those are not related to authors.
 and your searched author may not be found on goodreads or wikipedia.

>Used websites:
 goodreads.com
 wikipedia.com

>Developed by: Janel > find me at:
 [Github]: github.com/ccxa

>Special thanks to: Jadi > help: Educational video
 [Twitter]: twitter.com/jadi

    ''')
    wait = input('Hit enter to go back.')


def loading_screen(_percent):
    clear_console()
    print('Loading ['
          + ('IIIIII' * _percent)
          + ('      ' * (4 - _percent)) + '] '
          + '{}/4\n'.format(_percent)
          )


def get_authors_name(requests, bs4):
    clear_console()
    # authors name

    # Getting first letter of users first & last name
    first_name = input('Enter your First name:\n>> ').upper()
    last_name = input('Enter your last name\n>> ').upper()
    ffl, lfl = first_name[0], last_name[0]

    # Getting authors names | Extracting data from wikipedia
    base_url = 'https://en.m.wikipedia.org'
    page = requests.get(base_url + '/wiki/List_of_authors_by_name:_' + lfl)
    soup = bs4.BeautifulSoup(page.content)
    names = soup.findAll('a')

    print('\nLoading ...\n')
    clear_console()

    # Getting authors names | Extracting names from data
    writer_list = []
    counter = 1
    for name in names:
        if name.string is None:
            continue
        elif name.string[0] == ffl and len(name.string) > 1:
            print(str(counter).zfill(2), end='')
            print('-', name.string)
            counter += 1
            writer_list.append(name.string)

    return writer_list


def get_authors_books(requests, bs4, writer):
    loading_screen(1)

    # getting authors books from goodReads

    base_url = 'https://www.goodreads.com'
    query = base_url + '/search?utf8=%E2%9C%93&q=' \
        + writer \
        + '&search_type=lists'
    page = requests.get(query)
    soup = bs4.BeautifulSoup(page.content)
    link = soup.find('a', 'listTitle')

    loading_screen(2)

    link = str(link).split('"')
    page2 = requests.get(base_url + link[3])

    loading_screen(3)

    soup2 = bs4.BeautifulSoup(page2.content)

    loading_screen(3)

    books = soup2.findAll('a', 'bookTitle')

    try:
        print('Writen by:', writer.replace('+', ' '), '\n')

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

    except IndexError:
        clear_console()
        wait = input('Error!\nThere is not books for this author in goodreads.com')
