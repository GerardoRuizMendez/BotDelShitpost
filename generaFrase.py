import random, sqlite3

conexion=sqlite3.connect("BBDD/frases")
cursor=conexion.cursor()

def genera():
    cursor.execute("SELECT nombre FROM comida")
    print(cursor.fetchall()[1][0])

""""
frase=""
    if(random.randrange(1,3)==1):
        cursor.execute("SELECT nombre FROM comida")
        print(cursor.fetchall())
        #cursor.execute("SELECT nombre FROM comida WHERE id=" +random.randrange(1,))
        frase+=frase
"""


genera()