import sqlite3 

ruta_base='base1.db' 

def crear_tablas(ruta_b): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    tabla1='CREATE TABLE profesionales (nombre VARCHAR(100),userid VARCHAR(100), contraseña VARCHAR(100),servicios VARCHAR(100),precio INTEGER, direccion VARCHAR(100), telefono INTEGER)' 
    cursor.execute(tabla1) 
    tabla2='CREATE TABLE contratistas (userid VARCHAR(100), contraseña VARCHAR(100), direccion VARCHAR(100))' 
    cursor.execute(tabla2) 
    conexion.close() 
 
crear_tablas(ruta_base) 

def agregar_profesional(ruta_b,nombre,userid,contraseña,servicios,precio,direccion,telefono): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    sentenciasql= "INSERT INTO profesionales VALUES('"+nombre+"','"+userid+"','"+contraseña+"','"+servicios+"',"+str(precio)+",'"+direccion+"',"+str(telefono)+")" 
    cursor.execute(sentenciasql) #aca ve si hay error 
    conexion.commit()   #si hay error no llena la tabla. 
    conexion.close() 
 
def agregar_contratista(ruta_b,userid,contraseña,direccion): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    sentenciasql= "INSERT INTO contratistas VALUES('"+userid+"','"+contraseña+"','"+direccion+"')" 
    cursor.execute(sentenciasql)  
    conexion.commit()    
    conexion.close() 
    

agregar_profesional(ruta_base,"Lucila Katz","lkatz","hola123","Maquillaje",1000,"2374 Cuenca, CABA, Buenos Aires",1132598325) #esto despues lo hacemos con inputs 
agregar_contratista(ruta_base,"wanda","perro123","2344 Arregui, CABA, Buenos Aires ") 
 
def insertar_lista_profesionales(ruta_b,lista): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    sentenciasql= "INSERT INTO profesionales VALUES(?,?,?,?,?,?,?)" 
    cursor.executemany(sentenciasql,lista) 
    conexion.commit()   
    conexion.close() 
 
def insertar_lista_contratista(ruta_b,lista): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    sentenciasql= "INSERT INTO contratistas VALUES(?,?,?)" 
    cursor.executemany(sentenciasql,lista) 
    conexion.commit()   
    conexion.close() 
    
profesionales = [
    ("Silvia Gonzalez", "silvigonzalez","hola","peluqueria",1000,"Navarro 2887,CABA,Buenos Aires",1132598326),
    ("Ernesto Rodriguez", "ert","234","maquillaje",100,"Pedernera 3215,CABA,Buenos Aires",1132598327),
    ("Clara Villalba", "clara","vet","peluqueria",1050,"Pastor Obligado 70,Villa Sarmiento,Buenos Aires",1132598526),
    ("Nahuel Melero", "nahi","mel","maquillaje",180,"Maestro Santana 451,San Isidro,Buenos Aires",1132598336),
    ("Marcela Gonzalez", "marcela89", "324", "barberia", 800, "Av. Corrientes 1234, Buenos Aires, Buenos Aires",1132598396),
    ("Martin Fernandez", "martin2023", "martin123", "manicura", 1500, "Av. Libertador 5678, Vicente López, Buenos Aires",1132598320),
    ("Ana Gomez", "ana_belleza", "anabella2023", "manicura", 500, "Av. San Martín 4321, San Miguel, Buenos Aires",1132596326),
    ("Juan Perez", "juan_peluquero", "juanpelu", "peluqueria", 600, "Calle Lavalle 987, Ramos Mejía, Buenos Aires",1132598376),
    ("Sofia Carlos", "sofia_estilista", "sofia123", "maquillaje", 1200, "Av. Rivadavia 6543, Morón, Buenos Aires",1132598336),
    ("Diego Mecina", "diego_medico", "diegom", "estetica", 900, "Av. Cabildo 2101, Belgrano, Buenos Aires",1132598726),
    ("Lucia Pedemonte", "lucia_ped", "lucia", "estetica", 1200, "Calle Ituzaingó 345, Olivos, Buenos Aires",1132598026),
    ("Carlos Fanga", "carlos_fotografia", "carlitosfotos", "peluqueria", 1800, "Av. Santa Fe 7890, Martínez, Buenos Aires",1132598520),
    ("Ana Flores", "ana_estetica", "anita2023", "estetica", 1100, "Av. Cabildo 4321, Nuñez, Buenos Aires",1132598586),
    ("Juan Martinez", "juan_cocinero", "juan_cocina", "maquillaje", 2000, "Av. Scalabrini Ortiz 876, Palermo, Buenos Aires",1132592326),
    ("Luis Fraga", "luis_pintor", "luisarte", "estetica", 1500, "Dorrego 123, Vicente López, Buenos Aires",1132597626),
    ("Claudia Susic", "claudia_eventos", "clau_organiza", "pedicura", 2500, "Av. Santa Fe 5678, Recoleta, Buenos Aires",1132598456),
    ("Diego Carrera", "diego_entrenador", "diegofit", "pedicura", 800, "Av. Belgrano 321, Caballito, Buenos Aires",1132598323),
    ("Laura Frigo", "laura_limpieza", "lau321", "manicura", 600, "Monroe 789, Villa Urquiza, Buenos Aires",1132598344),
    ("Carlos Tech", "carlos_tech", "carlotech", "barberia", 1200, "Av. Corrientes 9876, Almagro, Buenos Aires",1132596626),
    ("Rosa Mauric", "rosa_costura", "rosasews", "barberia", 1300, "Billinghurst 2345, Chacarita, Buenos Aires",1132598387)]

insertar_lista_profesionales(ruta_base,profesionales) 
 
contratistas=[("nmeler","12345","2322 Navarro, CABA, Buenos Aires"),
              ("martu122","simona321","6425 Arregui,CABA,Buenos Aires"),
              ("nico","123","3742 Campana, CABA, Buenos Aires"),
              ("julieta95", "clave123", "500 Av. Cabildo, Belgrano, Buenos Aires"),
              ("roberto_gym", "gym1234", "1200 Av. Rivadavia, Flores, Buenos Aires"),
              ("luciana_p", "luciana456", "700 Av. Santa Fe, Recoleta, Buenos Aires"),
              ("marcos_viajes", "viajero321", "3400 Av. Corrientes, Almagro, Buenos Aires"),
              ("valentina_tech", "valen_tech", "900 Calle Tucumán, Centro, Buenos Aires"),
              ("lucas_figue", "lucasfi333", "250 Av. Córdoba, Palermo, Buenos Aires"),
              ("carolina_t", "carovet", "1500 Av. Libertador, Vicente López, Buenos Aires"),
              ("leo_fit", "leo123", "1800 Calle Dorrego, Chacarita, Buenos Aires")] 
insertar_lista_contratista(ruta_base,contratistas) 
 
#LEER LA BASE DE DATOS 

def ver_profesionales(ruta_b): 
    conexion=sqlite3.connect(ruta_b) 
    cursor=conexion.cursor() 
    sentenciasql= "SELECT * FROM profesionales" 
    cursor.execute(sentenciasql) #aca ve si hay error 
    conexion.commit()   #si hay error no llena la tabla. 
    conexion.close() 

conexion=sqlite3.connect(ruta_base) 
cursor=conexion.cursor() 
articulo=cursor.fetchone() 
print(articulo) 
conexion.close() 