# Scraping website from phone numbers in format 123.456.7890
# and e-mail addresses
# test website: https://nostarch.com/contactus


import re, pyperclip
text = pyperclip.paste()

phoneNumerCompiler = re.compile(r'(\d{3})\.(\d{3})\.(\d{4})')
mo_phone = phoneNumerCompiler.findall(text)

matches = []
for number in mo_phone:
    newString = number[0] + ' - ' + number[1] + ' - ' + number[2]
    matches.append(newString)

emailComplier = re.compile(r'\w+@\w+\.\w{0,4}')
mo_email =emailComplier.findall(text)

matches = matches + mo_email

listToString = '\n'.join(matches)
print(listToString)

pyperclip.copy(listToString)
