#Funciones con parametros finitos y keywords
x = 1

def saludar(nombre, edad):
    print("Hola " + nombre + "Edad: " + str(edad))


saludar("LEYDI", 20 )
saludar("LUIZ", 20)
saludar("VICTOR", 20)
saludar("ROLEX", 21)
saludar("FICACHI", 22)
saludar("VILLANUEVA", 21)
saludar("KEVIN", 26)

#-------Funciones con N parametros-------------

def asistencia(*alumnos):
    print(alumnos[0])

asistencia("LAURA", "ANGEL", "OCTAVIO", "EMIR")
asistencia("AXEL", "ROLEX")
asistencia("CJ")
#------------------------------
def asistencia(*alumnos):
    for alumno in alumnos:
        print("ASISTIO: " + alumno)


asistencia("LAURA", "ANGEL", "OCTAVIO", "EMIR")
asistencia("AXEL", "ROLEX")
asistencia("CJ")

#----------Funciones  con Parametros con defecto---------------


#----------Funciones que Retornan valores----------------------

