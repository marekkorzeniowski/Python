#! python3
import time, pyautogui

formData = [{
    'name': 'Marek',
    'fear': 'wand',
    'source': 'wand',
    'robocop': 4,
    'comments': 'Tell mum I am comming!'
},
{
    'name': 'Kasia',
    'fear': 'amulet',
    'source': 'wand',
    'robocop': 2,
    'comments': 'Tell mum I am not comming!'
},
{
    'name': 'Kazik',
    'fear': 'money',
    'source': 'wand',
    'robocop': 3,
    'comments': ' mum I am not comming!'
}]

pyautogui.PAUSE = 1

pyautogui.hotkey('alt', '\t')

nameField = (396,553)
submitAnotherLink = (433,438)

for person in formData:

    pyautogui.click(nameField[0], nameField[1])
    pyautogui.typewrite(person['name'] + '\t')

    pyautogui.typewrite(person['fear'] + '\t')

    time.sleep(1)
    if person['source'] == 'wand':
        pyautogui.typewrite(['down','down'])
        pyautogui.press('enter')
        pyautogui.press('\t')
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down','down','down','\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down', 'down', 'down', '\t'])
    else:
        pyautogui.typewrite(['down', '\t'])

    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right','right','\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right','right','\t'])

    pyautogui.typewrite(person['comments'] + '\t')

    pyautogui.press('enter')

    print('Clicked submit.')
    time.sleep(1)

    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])



