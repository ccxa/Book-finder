import os


def check_connection(requests):
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
