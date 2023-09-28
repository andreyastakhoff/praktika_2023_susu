import tkinter as tk
import tkinter.filedialog as tfd
import tkinter.messagebox as tkm

# Создаем главное окно
window = tk.Tk()
window.geometry("400x400")
window.title("Блокнот")

file_name = ""  # Имя текущего файла


# Функция для отображения справки
def help():
    tkm.showinfo("Помощь",
                 "Новый - создать новый файл\nОткрыть - открыть существующий файл\nСохранить - сохранить файл\n"
                 "Сохранить как - сохранить файл с новым именем")


# Функция для отображения информации о программе
def about():
    tkm.showinfo("Блокнот: сведения", "Версия: 1.0\nРазработано: Астахов Андрей Олегович КЭз-395")


# Функция для записи текста в файл
def write_to_file(file_name):
    content = content_text.get(1.0, "end")
    with open(file_name, "w") as file:
        file.write(content)


# Функция для открытия файла
def open_file():
    content_text.delete(1.0, "end")
    global file_name
    file_name = tfd.askopenfilename()
    file_label["text"] = "Файл: " + file_name
    with open(file_name) as file:
        content_text.insert(1.0, file.read())


# Функция для сохранения файла с новым именем
def save_as_file():
    global file_name
    file_name = tfd.asksaveasfilename()
    file_label["text"] = "Файл: " + file_name
    write_to_file(file_name)
    tkm.showinfo("Сохранение файла", f"Сохранения записаны в файл {file_name}")


# Функция для сохранения файла
def save_file():
    global file_name
    if file_name == "":
        save_as_file()
    else:
        write_to_file(file_name)
        tkm.showinfo("Файл сохранен", "Сохранения записаны в файл " + file_name)


# Функция для создания нового файла
def new_file():
    global file_name
    if tkm.askokcancel("Создание нового файла", "Вы уверены? Несохраненный текст будет удален"):
        file_name = ""
        file_label["text"] = "Файл: " + file_name
        content_text.delete(1.0, "end")


# Создаем текстовое поле
content_text = tk.Text(window, wrap="word")
content_text.place(relx=0, rely=0, relwidth=1, relheight=1)

# Создаем меню
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Справка", menu=help_menu)

# Добавляем команды в меню
help_menu.add_command(label="Помощь", compound="left", command=help)
help_menu.add_command(label="О программе", compound="left", command=about)

file_menu.add_command(label="Новый", compound='left', command=new_file)
file_menu.add_command(label="Открыть", compound='left', command=open_file)
file_menu.add_command(label="Сохранить", compound='left', command=save_file)
file_menu.add_command(label="Сохранить как", compound='left', command=save_as_file)

# Создаем метку для отображения текущего файла
file_label = tk.Label(window, text="Файл: " + file_name)
file_label.place(relx=0, rely=1, anchor="sw")

# Отображаем приветственное сообщение
tkm.showinfo("Добро пожаловать!", "Вас приветствует программа\"Мой блокнот\"")

# Запускаем главный цикл окна
window.mainloop()
