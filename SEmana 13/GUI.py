import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
app = tk.Tk()
app.geometry('500x400')  # Ajuste de tamaño
app.configure(background='black')
app.title('Benvenid@ 🤗')

# Botón de prueba
tk.Button(
    app,
    text='Dale click 🖱️',
    font=('Calibri', 14),
    bg='#0d1b2a',
    fg='white',
    command=lambda: print('¿Qué tal tu día 🫣')
).pack(fill=tk.BOTH, expand=True)

# Crear menú
barra_menu = tk.Menu(app)
app.config(menu=barra_menu)
menu_archivo = tk.Menu(barra_menu)
barra_menu.add_cascade(label='Archivo', menu=menu_archivo)
menu_archivo.add_command(label='Salir', command=app.quit)

# Crear título
titulo = tk.Label(app, text='Ingresa tus datos', font=('Arial', 12), bg='black', fg='white')
titulo.pack(pady=10)

# Crear etiquetas y campos de entrada
tk.Label(app, text='Ingresa tus nombres:', bg='black', fg='white').pack()
entrada_nombre = tk.Entry(app)
entrada_nombre.pack()

tk.Label(app, text='Ingresa tus apellidos:', bg='black', fg='white').pack()
entrada_apellido = tk.Entry(app)
entrada_apellido.pack()

tk.Label(app, text='Ingresa tu correo:', bg='black', fg='white').pack()
entrada_correo = tk.Entry(app)
entrada_correo.pack()






tabla = (ttk.Treeview(app, columns=('nombre', 'apellido', 'correo')))
tabla.heading('nombre', text='Nombre ✍️')
tabla.heading('apellido', text='Apellido ✍️')
tabla.heading('correo', text='Correo ✍️')
tabla.column('nombre', width=25, anchor='center')
tabla.column('apellido', width=25, anchor='center')
tabla.column('correo', width=25, anchor='center')








app.mainloop()

