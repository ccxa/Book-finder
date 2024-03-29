import os


def check_connection(requests):
    clear_console()
    print("Checking connection ... ")
    try:
        requests.get('http://www.google.com')
    except Exception as e:
        clear_console()
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

    first_name_first_letter = first_name[0]
    last_name_first_letter =  last_name[0]

    # Getting authors names | Extracting data from wikipedia
    base_url = 'https://en.m.wikipedia.org'
    request_url = base_url + '/wiki/List_of_authors_by_name:_'
    page = requests.get(request_url + last_name_first_letter)
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
        elif name.string[0] == first_name_first_letter and len(name.string) > 1:
            print(str(counter).zfill(2), end='')
            print('-', name.string)
            counter += 1
            writer_list.append(name.string)

    return writer_list


def get_authors_books(requests, bs4, writer):
    loading_screen(1)
    try:
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
        loading_screen(4)
        books = soup2.findAll('a', 'bookTitle')
        clear_console()
        print('Writen by:', writer.replace('+', ' '), '\n')

        # Extract and cleaning book names from downloaded data
        counter = 1
        for book in books:

            book = str(book).split('"')
            book = book[3][11:]

            forbidden_list = '0123456789.'
            book_name = ''
            for w in book:
                if w not in forbidden_list:
                    book_name = book_name + w

            book_name = book_name.replace('_', ' ').replace('-', ' ')
            if book_name[0] == ' ':
                book_name = book_name[1:]

            print(str(counter).zfill(2), '-', book_name)
            counter += 1

            if counter > 10:
                break
        wait = input('\nHit enter to go menu.')

    except IndexError:
        clear_console()
        wait = input('Error!\nNo books found for this author at goodreads.com')
