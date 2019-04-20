def start_check():
    # import libraries
    try:
        import os
        import requests
        import bs4
    except Exception as e:
        print(e, "\nYou have to install this library.")
        _exit = input('Hit Enter to exit.')
        exit()

    # checking connection
    try:
        test = requests.get('http://www.google.com')
    except Exception as e:
        print(e)
        print('You have to connected to internet.')
        _exit = input('Make sure you are connected. Hit Enter to exit.')
        exit()
