import PySimpleGUI as sg

# Указываем тему окна
sg.theme('DarkGrey5')

# Объявляем элементы в интерфейсе приложения.
layout = [  [sg.Text('Калькулятор')],
            [sg.Text('Введите выражение: '), sg.InputText('', k='in0')],
            [sg.Text('', k='out0')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Создаём окно программы
window = sg.Window('Title Program', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Ok':
        val = 'Ответ: ' + str(eval(values['in0']))
        window.Element('out0').update(val)

window.close()