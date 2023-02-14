global notes


notes='notes.csv'

def print_note(file):
    """
    Показывает список заметок
    """
    with open(file, encoding='utf-8') as file  :
        for line in file:
            print(line,end='')
    file.close()
    print()
    


def search_note(note):
    """
    Ищет заметку по запросу
    """
    with open(notes,'r', encoding='utf-8') as f:
        for line in f: 
            if note in line:
                print(line)
                note=line
        return note


def replace_note(note,new_note):
    """
    Редактирует заметку
    """
    f = open(notes, 'r',encoding = 'utf-8')
    lines = f.readlines()
    f.close()
    f = open(notes, 'w',encoding = 'utf-8')
    for line in lines: 
        if line!=note:
            f.write(line)
        elif line==note:
            f.write(f'{new_note}\n')
    f.close()           

def save_note(note):
    """
    Функция записывает новую заметку
    """
    with open(notes, 'a', encoding='utf-8') as data:
        data.write(f"\n{note}")


def del_note(note):
    """
    Удаляет заметку
    """
    f = open(notes, 'r',encoding = 'utf-8')
    lines = f.readlines()
    f.close()
    f = open(notes, 'w',encoding = 'utf-8')
    for line in lines: 
        if line!=note:
            f.write(line)
    f.close()
    


