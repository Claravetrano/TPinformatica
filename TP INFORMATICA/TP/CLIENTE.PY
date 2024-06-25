import database
import sqlite3
from api import obtener_foto
from database import ver_profesionales

class Usuario:
    def __init__(self, id_usuario, contraseña, nombre, apellido, localidad):
         self.user_id = id_usuario
         self.__password = contraseña
         self.nombre = nombre
         self.apellido = apellido
         self.localidad = localidad

    def set_password(self, new_password):
         self.__password = new_password

    def get_password(self):
         return self.__password


class Profesional(Usuario):
    def __init__(self, id_usuario, contraseña, nombre, apellido, localidad, habilidades):
        super().__init__(id_usuario, contraseña, nombre, apellido, localidad)
        self.habilidades = habilidades


class Contratista(Usuario):
    def __init__(self, id_usuario, contraseña, nombre, apellido, localidad, empresa):
        super().__init__(id_usuario, contraseña, nombre, apellido, localidad)
        self.empresa = empresa



def registrar_usuario(usuario):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    if isinstance(usuario, Profesional):
        tipo = "profesional"
        valores = (tipo, usuario.user_id, usuario.get_password(), usuario.nombre, usuario.apellido, usuario.localidad, ",".join(usuario.habilidades), "")
    elif isinstance(usuario, Contratista):
        tipo = "contratista"
        valores = (tipo, usuario.user_id, usuario.get_password(), usuario.nombre, usuario.apellido, usuario.localidad, "", usuario.empresa)
    cursor.execute("INSERT INTO usuarios (tipo, user_id, contraseña, nombre, apellido, localidad, habilidades, empresa) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", valores)
    conn.commit()
    conn.close()

def login(categoria,userid, contrasenia):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {categoria} WHERE userid=? AND contraseña=?", (userid, contrasenia))
    user_data = cursor.fetchone()
    if user_data:
        return user_data
    conn.close()

def esProf(userid):
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profesionales WHERE userid=?", (userid,))
    rows = cursor.fetchone()
    if rows:
        return "profesionales"
    else:
        cursor.execute("SELECT * FROM contratistas WHERE userid=?", (userid,))
        rows = cursor.fetchone()
        if rows:
            return "contratistas"
        else:
            return False
        
def verProfesionales():
    i=False
    conn = sqlite3.connect("base1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profesionales")
    rows = cursor.fetchall()
    servicio = input("Que tipo de servicio estas buscando? ")
    for profesional in rows:
        if servicio == profesional[3]:
            foto = obtener_foto()
            direccion = profesional[5].replace(' ','+')
            print(f"\nNombre:{profesional[0]} \nServicio: {profesional[3]}\nPrecio: {profesional[4]}\nDireccion: https://www.google.com.ar/maps/place/{direccion}\nImagen: {foto}\nMandarle Mensaje: https://api.whatsapp.com/send/?phone={profesional[6]}&text&type=phone_number&app_absent=0\n")
            i=True
        
    if i==False:
        print("No se han encontrado ningun profesional")


def init_database():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                       id INTEGER PRIMARY KEY,
                       tipo TEXT,
                       user_id TEXT,
                       contraseña TEXT,
                       nombre TEXT,
                       apellido TEXT,
                       localidad TEXT,
                       habilidades TEXT,
                       empresa TEXT)''')
    conn.commit()
    conn.close()
    
def main():
    init_database()
    while True:
        usuario = None
        if not usuario:
            userid = input("Ingresa tu email: ")
            categoria = esProf(userid)
            if categoria:
                contrasenia = input("Ingresa tu contraseña: ")
                usuario = login(categoria, userid, contrasenia)
                if usuario:
                    if categoria == "contratistas":
                        print(f"BIENVENIDO AL SISTEMA DE BUSQUEDA DE PROFESIONALES")
                        verProfesionales()
                else:
                    print("Usuario y/o contraseña incorrectos")
        else:
              if isinstance(usuario, Profesional):
                  print("Los profesionales no pueden realizar acciones en esta versión de la aplicación.")
              elif isinstance(usuario, Contratista):
                  
                  pass

main()

print(main)
