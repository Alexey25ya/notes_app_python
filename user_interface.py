from colorama import *
import emoji as e
import check as ch
from datetime import datetime as dt

def hello():
    '''
    Приветсвует пользователя
    
    '''
    print(e.emojize(f'{Style.BRIGHT + Fore.GREEN}Добро пожаловать!:raising_hands:{Style.RESET_ALL}'))
def by():
    '''
    Прощается с пользователем
    
    '''
    print(e.emojize(f'{Style.BRIGHT + Fore.GREEN}До встречи!:raising_hands:{Style.RESET_ALL}'))


def phone_menu(number: str = '') -> int:
    '''
    Вывод в консоль меню. Запускает модуль, где функция принимает число от пользователя, проверяет и возвращает его.
    '''
    
    print(e.emojize(f'{Style.BRIGHT + Fore.YELLOW}Выберите действие со списком заметок (введите цифру от 1 до 4): \n{Style.RESET_ALL}'
          '1 - :busts_in_silhouette: Просмотреть все заметки \n'
                    '2 - :eyes: Поиск, удаление и редактирование заметки \n'
                    '3 - :writing_hand:  Добавить новую заметку \n'
                    '4 - :airplane:  Завершить работу справочника\n'
                    f'{Style.RESET_ALL}'))
    return ch.check_note_menu(number,5)

def search_submenu(number: str = '') -> int:
    '''
    Подменю после вызова поиска контакта
    '''
    print(e.emojize(f'{Style.BRIGHT + Fore.YELLOW}:eyes:  Выберите действия для работы: {Style.RESET_ALL} \n'
                    '1 - :broom:  Удалить заметку \n'
                    '2 - :pencil:  Редактировать заметку'))
    return ch.check_note_menu(number,3)


def print_all(data_list: list) -> None:
    '''
    Вывод списка всех заметок
    '''
    print(e.emojize(f'{Style.BRIGHT + Fore.YELLOW}:busts_in_silhouette:  Ваши контакты: {Style.RESET_ALL}'))
    for line in data_list:
        print(line)


def print_note(note_data: str = '') -> None:
    '''
    Выводит определенную заметку в консоль после поиска, или редактирования, или добавления.
    '''
    print(e.emojize(
        f'{Style.BRIGHT + Fore.YELLOW}:heart_decoration:  Карточа заметки: \n {note_data}{Style.RESET_ALL}'))


def input_new_note() -> str:
    '''
    Функция добавляет новые данные, возвращает строку.
    '''
    note = []
    time = dt.now().strftime('%d.%m.%Y - %H:%M')
    note.append(time)
    note.append('; ')
    print(e.emojize(f'{Style.BRIGHT + Fore.YELLOW}:writing_hand:  Добавьте новую заметку: {Style.RESET_ALL}'))
    text = ch.record_length('Заголовок: ',20)
    text = text.capitalize()
    note.append(text)
    note.append('; ')
    text = ch.record_length('Текст заметки: ',50)
    text = text.capitalize()
    note.append(text)
    print(e.emojize(
        f'{Style.BRIGHT + Fore.YELLOW}:check_mark_button: Заметка добавлена{Style.RESET_ALL}'))
    return ''.join(note)


def edit_data(note_data: str = '') -> str:
    '''
    Функция перезаписывает новые данные поверх имеющейся записи
    '''
    print(e.emojize(f'{Style.BRIGHT + Fore.YELLOW}:card_index_dividers:  Введите новые данные: {Style.RESET_ALL}'))
    return ch.record_length(note_data)

def search(note: str = '') -> None:
    '''
    Ввод в поисковую строку и поиск
    '''
    note=str(input(e.emojize(f'{Style.BRIGHT + Fore.YELLOW}:writing_hand: Введите искомую заметку: {Style.RESET_ALL} '))).capitalize()
    return note