#! python3

# insecure password locker

PASSWORDS = {'email': 'abcdefge1234kajaja',
             'blog': 'srog123gors',
             'luggage': '00112233'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python passwordLocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # 1st command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
    print(sys.argv[0])
else:
    print('There is no account name ' + account)

