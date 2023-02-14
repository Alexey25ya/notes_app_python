from colorama import *

def record_length(length:str,num)->str:
    '''Проверка длины вводимой строки и тут же проверка на пустую строку'''
    
    while True:
        try:
            l = input(length)
            if len(l)==0:
                print(Fore.RED + 'Вы ничего не ввели!'+ Style.RESET_ALL)
            elif len(l)<num:
                return l
            else:
                print(Fore.RED + 'Вы ввели слишком много символов '+ Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Неверно! Повторите ввод!'+ Style.RESET_ALL)

def check_note_menu(num:str,m)->int:
 
    while True:
        try:
            n = int(input(num))
            if 0<int(n)<m:
                return n
            else:
                print(Fore.RED + f'Неверно! Введите число от 1 до {m-1} в соответствии с пунктами меню!'+ Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + f'Неверно!Введите число от 1 до {m-1} в соответствии с пунктами меню!' + Style.RESET_ALL)

