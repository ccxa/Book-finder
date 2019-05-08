import os


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
