import sqlite3

conexion=sqlite3.connect("BBDD/frases")
cursor=conexion.cursor()


cursor.execute('''CREATE TABLE comida(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(20))''')

cursor.execute('''CREATE TABLE conector(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(10))''')

cursor.execute('''CREATE TABLE extra(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(10))''')

conexion.commit()
conexion.close()