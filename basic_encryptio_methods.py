import sys
from rich.table import Table
from rich.console import Console
from rich import print
from encryption_caesar import encode_caesar
from encryption_caesar import decoding_caesar

from encryption_playfire import encode_playfire

console = Console()


def method_encod(method, title, t_key=False):
    b1 = True
    while (b1):
        str_out = ''
        try:
            console.print("*", title)
            str_in = input("Введите строку для обработка : ")

            if (t_key):
                key_in = ''
                key_in = input("Введите строку для ключения : ")
                str_out = method(str_in, key_in)
            else:
                str_out = method(str_in)
            console.print("Расшифрованный текст: ", str_out)

        except:
            console.print("Введенная вами строка недействительна,", "произошла ошибока ", sys.exc_info()[0], '!!!!')

        b11 = True
        while (b11):
            contin = console.input("Попробовать ещё раз ? (y/n - д/н)")

            if contin == 'y' or contin == 'Y' or contin == 'д' or contin == 'Д':
                b1 = True
                b11 = False
            elif contin == 'n' or contin == 'N' or contin == 'н' or contin == 'Н':
                b1 = False
                b11 = False
            else:
                console.print("Недействительное значение, попробуйте еще раз!!!")
                b11 = True


def select_method():
    console.print("***Добро пожаловать в программу, которая синииезирует самые простые методы шифрования.****")
    table = Table(title="Списоки методы шифра:")
    table.add_column("№", justify="center", style="cyan", no_wrap=True)
    table.add_column("Название метода шифрования", style="magenta")

    table.add_row("1", "Шифр Цезаря.")
    table.add_row("2", "Шифр Плейфейера.")
    table.add_row("3", "Квадрат Полибия.")
    table.add_row("4", "Шифры полиалфавитные. Шифр Виженера.")
    table.add_row("5", "Шифры перестановки.")
    table.add_row("6", "Шифр \"Поворотная решетка\"")
    table.add_row("7", "Шифр вертикальной перестановки.")
    table.add_row("8", "Кодирование текста решетка.")
    table.add_row("9", "Одноразовый шифровальный блокнот.")
    table.add_row("e", "Нажмите клавишу \"е or в\", чтобы выйти из програмы.")
    console.print(table)

    select_x = input("Какой метод вы выберете ? ")

    sel = select_x

    if sel == '1':
        method_encod(encode_caesar, "Шифр Цезаря")

    elif sel == '2':
        method_encod(encode_playfire, "Шифр Плейфейера", True)

    elif sel == 'e' or sel == 'E' or sel == 'в' or sel == 'В':
        exit()

    else:
        console.print(
            "Произошла ошибка. Возможно, вы ввели неправильный номер метода или метод не был разработан программистом.!!!")

    '''switcher = {
        1: 
        2: method_encod(encode_playfire, ")
    }
    return switcher.get(sel, "nothing")'''


def loop_method():
    while True:
        select_method()


loop_method()
