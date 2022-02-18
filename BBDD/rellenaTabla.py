import sqlite3

conexion=sqlite3.connect("BBDD/frases")
cursor=conexion.cursor()

cursor.execute("INSERT INTO comida VALUES(NULL, 'tacos')")
cursor.execute("INSERT INTO comida VALUES(NULL, 'mole')")
cursor.execute("INSERT INTO comida VALUES(NULL, 'empanada')")
cursor.execute("INSERT INTO comida VALUES(NULL, 'chile')")
cursor.execute("INSERT INTO comida VALUES(NULL, 'sopa')")


cursor.execute("INSERT INTO conector VALUES(NULL, 'con')")
cursor.execute("INSERT INTO conector VALUES(NULL, 'de')")

cursor.execute("INSERT INTO extra VALUES(NULL, 'aceituna')")
cursor.execute("INSERT INTO extra VALUES(NULL, 'arroz')")
cursor.execute("INSERT INTO extra VALUES(NULL, 'pito')")

conexion.commit()
conexion.close()