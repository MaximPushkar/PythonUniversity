from tkinter import *
from tkinter import messagebox
import new_grand_system, old_grand_system

root = Tk()

root.resizable(width=False, height=False)
root.geometry("800x500")
root['bg'] = '#abc'
root.title("Менеджер стипендії")


# Functions
def do_all_work(event):
    path_from = from_file.get()
    path_to = to_file.get()
    system_type = var1.get()
    answer_questions = var2.get()

    if path_from == "d":  # default
        path_from = "Students.txt"
    if path_to == "d" and system_type == 0:
        path_to = "Students with grants (old system).txt"
    elif path_to == "d" and system_type == 1:
        path_to = "Students with grants (new system).txt"

    if not path_from and not path_to:
        messagebox.showerror('Проблеми вводу',
                             'Введіть назву файлу з інформацією та назву файлу для запису результатів')
    elif not path_from:
        messagebox.showerror('Проблеми вводу', 'Введіть назву файлу з інформацією')
    elif not path_to:
        messagebox.showerror('Проблеми вводу', 'Введіть назву файлу для запису результатів')
    else:
        try:
            if system_type == 0:
                t = old_grand_system.StipendManager(path_from)
            else:
                t = new_grand_system.ModernStipendManager(path_from)
        except FileNotFoundError:
            messagebox.showerror('Відкриття файлу', 'Виникла проблема з відкриттям файлу з данними')
        except IndexError:
            messagebox.showerror('Читання файлу',
                                 'Виникла проблема з читанням файлу з данними, перевірте формат данних у файлі')
        except Exception as e:
            messagebox.showerror('Відкриття-читання файлу',
                                 'Виникла помилка \"' + str(e) + '\" при відкритті-читанні-обробці файлу з данними')
        else:
            try:
                t.print_results_to_the_file(path_to)
            except Exception as e:
                messagebox.showerror('Отримання результатів',
                                     'Виникла помилка \"' + str(e) +
                                     '\" при друкуванні результатів роботи программи до файлу')
            else:
                if answer_questions:
                    answers_for_the_questions['bg'] = '#aaa'
                    answers_for_the_questions['text'] = f"""    Відповіді на запитання до задачі:
1) Отримують академічну стипендію: {t.number_of_granted_students("Академічна стипендія")} 
2) Отримують соціальну стипендію: {t.number_of_granted_students("Соціальна стипендія")} 
3) Виплачено загалом: {t.sum_of_grants()} грн.
4) Середній бал академ. стипендія:  {round(t.average_mark("Академічна стипендія"), 2)}    
5) Середній бал соц. стипендія:  {round(t.average_mark("Соціальна стипендія"), 2)}"""

                messagebox.showinfo('Успіх!', 'Операція виконана')


# Events
text_from_file = Label(text='Прочитати інформацію з файлу: ', font='courier 13', fg='#3d3d42', bg='#abc')
from_file = Entry(root, font='courier 13', relief='raised', justify='center', width=40)

text_to_file = Label(text='Записати результати до файлу: ', font='courier 13', fg='#3d3d42', bg='#abc')
to_file = Entry(root, font='courier 13', relief='raised', justify='center', width=40)

var1 = IntVar()
var1.set(0)
old = Radiobutton(text="Стара система", variable=var1, value=0,
                  font='courier 13',
                  fg='#3d3d42', bg='#abc',
                  activeforeground='#3d3d42',
                  activebackground='#abc')
new = Radiobutton(text="Нова система", variable=var1, value=1,
                  font='courier 13',
                  fg='#3d3d42', bg='#abc',
                  activeforeground='#3d3d42',
                  activebackground='#abc')

# text_type_of_system = Label(text='Система (1) стара (2) нова: ', font='courier 13', fg='#3d3d42', bg='#abc')
# type_of_system = Entry(root, font='courier 13', relief='raised', justify='center')

var2 = BooleanVar()
var2.set(0)
print_boring_stuff = Checkbutton(text='Вивести на екран відповіді на запитання',
                                 font='courier 13',
                                 fg='#3d3d42', bg='#abc',
                                 activeforeground='#3d3d42',
                                 activebackground='#abc',
                                 variable=var2, onvalue=1, offvalue=0)

enter = Button(text='виконати', font='courier 15', fg='#612835', bg='#abc', relief='raised')

answers_for_the_questions = Label(text='', font='courier 13', fg='#3d3d42', bg='#abc', justify='left')


# Packer
text_from_file.place(x=10, y=10)
from_file.place(x=340, y=10)

text_to_file.place(x=10, y=40)
to_file.place(x=340, y=40)

old.place(x=60, y=70)
new.place(x=300, y=70)

# text_type_of_system.place(x=10, y=70)
# type_of_system.place(x=340, y=70)

print_boring_stuff.place(x=10, y=100)

enter.place(x=320, y=130)

answers_for_the_questions.place(x=10, y=190)


# Bind
enter.bind('<Button-1>', do_all_work)

root.mainloop()
