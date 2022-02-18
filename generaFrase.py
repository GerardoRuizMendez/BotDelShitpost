from pickle import TRUE
import random, sqlite3

conexion=sqlite3.connect("BBDD/frases")
cursor=conexion.cursor()

def genera():
    tipo=random.randrange(1,3)
    frase=""
    if(tipo==1):
        cursor.execute("SELECT nombre FROM comida")
        tam=len(cursor.fetchall())
        cursor.execute("SELECT nombre FROM comida WHERE id=" +str(random.randrange(1,tam+1)))
        frase+=cursor.fetchall()[0][0] +" "

        cursor.execute("SELECT nombre FROM conector")
        tam=len(cursor.fetchall())
        cursor.execute("SELECT nombre FROM conector WHERE id=" +str(random.randrange(1,tam+1)))
        frase+=cursor.fetchall()[0][0] +" "

        cursor.execute("SELECT nombre FROM extra")
        tam=len(cursor.fetchall())
        cursor.execute("SELECT nombre FROM extra WHERE id=" +str(random.randrange(1,tam+1)))
        frase+=cursor.fetchall()[0][0]

    else:
        cursor.execute("SELECT nombre FROM extra")
        tam=len(cursor.fetchall())
        cursor.execute("SELECT nombre FROM extra WHERE id=" +str(random.randrange(1,tam+1)))
        frase+=cursor.fetchall()[0][0]

    return frase
