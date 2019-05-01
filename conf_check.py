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


# clearing console by the os type
if os.system('clear') == 0:
    clearIt = 'clear'
else:
    clearIt = 'cls'