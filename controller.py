
import operations as o
import user_interface as ui
import time
import log

def notes():
    ui.hello()
    while True:        
        command=ui.phone_menu()
        if command==1:            
            o.print_note(o.notes)
            log.log('Просмотр списка заметок','успешно')
            time.sleep(1)              
        elif command == 2:
            note=ui.search()
            note1=o.search_note(note)
            if note1==note:
                print('Запись не найдена!')
                time.sleep(1) 
            else:
                c=ui.search_submenu()
                if c==1:
                    log.log('Удаление заметки',f'{note1}')
                    o.del_note(note1)
                else:                
                    new_note=ui.input_new_note()
                    o.replace_note(note1,new_note)
                    log.log(f'Заметка <{note1}>',f' изменена на <{new_note}>')
        elif command == 3:
            note=ui.input_new_note()
            o.save_note(note)
            log.log(f'Добавлена заметка',f'{note}') 
        else:
            ui.by()
            break

    