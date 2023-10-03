#CLASES Y OBJETOS


#Creando la clase
class Alumno:
    def __int__(self, nombre, numControl, edad):
        self.nombre = nombre
        self.numControl = numControl
        self.edad = edad

#Creando el objeto
alumnoEmir = Alumno
alumnoRoxel = Alumno
alumnoVictor = Alumno

print(alumnoEmir.nombre)
print(alumnoRoxel.nombre)
print(alumnoVictor.nombre)