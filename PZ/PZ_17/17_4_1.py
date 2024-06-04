# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1).
# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ NoNo 2 – 9.


import tkinter as tk 
from tkinter import ttk

root = tk.Tk() 
root.title("Форма регистрации пользователя")

frame = tk.Frame(root, borderwidth=2, relief="groove", padx=10, pady=10) 
frame.grid(row=0, column=0, padx=10, pady=10)

title_label = tk.Label(frame, text="Форма регистрации пользователя", font=("Helvetica", 16, "bold")) 
title_label.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(frame, text="Ваше имя:", font=("Helvetica", 12)).grid(row=1, column=0, pady=5, sticky="e") 
entry_name = tk.Entry(frame, width=40) 
entry_name.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Пароль:", font=("Helvetica", 12)).grid(row=2, column=0, pady=5, sticky="e") 
entry_password = tk.Entry(frame, show='*', width=40) 
entry_password.grid(row=2, column=1, pady=5)

tk.Label(frame, text="Возраст:", font=("Helvetica", 12)).grid(row=3, column=0, pady=5, sticky="e") 
entry_age = tk.Entry(frame, width=40) 
entry_age.grid(row=3, column=1, pady=5)
tk.Label(frame, text="Пол:", font=("Helvetica", 12)).grid(row=4, column=0, pady=5, sticky="e") 
gender_frame = tk.Frame(frame) 
gender_frame.grid(row=4, column=1, pady=5, sticky="w", padx=70) 
gender_var = tk.StringVar(value="Мужской") 
tk.Radiobutton(gender_frame, text="Мужской", variable=gender_var, value="Мужской").pack(side="left") 
tk.Radiobutton(gender_frame, text="Женский", variable=gender_var, value="Женский").pack(side="left")

tk.Label(frame, text="Ваши увлечения:", font=("Helvetica", 12)).grid(row=5, column=0, pady=5, sticky="e") 
hobbies_frame = tk.Frame(frame) 
hobbies_frame.grid(row=5, column=1, pady=5, sticky="w", padx=70) 
music_var = tk.BooleanVar() 
video_var = tk.BooleanVar() 
drawing_var = tk.BooleanVar() 
tk.Checkbutton(hobbies_frame, text="Музыка", variable=music_var).pack(side="left") 
tk.Checkbutton(hobbies_frame, text="Видео", variable=video_var).pack(side="left") 
tk.Checkbutton(hobbies_frame, text="Рисование", variable=drawing_var).pack(side="left")
tk.Label(frame, text="Ваша страна:", font=("Helvetica", 12)).grid(row=6, column=0, pady=5, sticky="e") 
country_combobox = ttk.Combobox(frame, values=[""], width=37) 
country_combobox.grid(row=6, column=1, pady=5) 
country_combobox.current(0)

tk.Label(frame, text="Ваш город:", font=("Helvetica", 12)).grid(row=7, column=0, pady=5, sticky="e") 
city_combobox = ttk.Combobox(frame, values=[""], width=37) 
city_combobox.grid(row=7, column=1, pady=5) 
city_combobox.current(0)

tk.Label(frame, text="Кратко о себе:", font=("Helvetica", 12)).grid(row=8, column=0, pady=5, sticky="e")
about_text = tk.Text(frame, height=4, width=30, wrap="word") 
about_text.grid(row=8, column=1, pady=5) 
about_text.insert("1.0", "Краткая информация о ваших увлечениях")
tk.Label(frame, text="Решите пример, запишите результат в поле ниже:", font=("Helvetica", 12)).grid(row=9, column=1, pady=5, sticky="e")

captcha_entry = tk.Entry(frame, width=40) 
captcha_entry.grid(row=10, column=1, pady=5, padx=20, sticky="w")

buttons_frame = tk.Frame(frame) 
buttons_frame.grid(row=11, column=0, columnspan=2, pady=10) 
cancel_button = tk.Button(buttons_frame, text="Отменить ввод", width=20) 
cancel_button.pack(side="left", padx=5) 
submit_button = tk.Button(buttons_frame, text="Данные подтверждаю", width=20) 
submit_button.pack(side="left", padx=5, pady=5)

root.mainloop()