x = 4
nombreMessi = "MESSI"
nombreCristiano = "CRISTIANO"

z = float(3)
y = int(3.2)
k = int("10")
print(z)
print(y)
print(k)
print(type(k))

# Condiciones
if x == 7:
    print(nombreCristiano)
elif x == 10:
    print(nombreMessi)
elif x == 4:
    print("rafa marquez")
else:
    print("No existe")

# Strings
nombre = "Isaias"
print(nombre)

#-------Deletrear el nombre------------------
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])
print(nombre[4])
print(nombre[5])
#----------Segunda forma de deletrear nombre----------------------
for letra in nombre:
    print(letra)

#----Cuantas letras tiene la variable------
print(len(nombre))

#------Imprimir una palabra especifica----------
texto = "alla en la fuente habia un chorrito"
print("chorrito" in texto)
if "chorrito" in texto:
    print("CHORRITO")

#ejercicio
#Del siguiente variable texto =
""" 
Son las 7 de la noche y ya me quiero ir
si encuentra el numero 7 y es menor a 8
imprimir el numero 7 convertido a int
y el texto, 'es hora de irnos son las : '7'
"""


texto = "Son las 7 de la noche y ya me quiero ir"
if '7' in texto:
    n = int("7")
    if n<8:
        print(f"es hora de irnos son las: {n}" )

##Slicing String
##---------------Mostrar palabras por rango de espacios---------
b = "Hola Mundo"
c = b[0:4]
print(c)

#Silce desde el inico
#
print(b[5:10])
print(b[:5])
#Slice
#-----------Mostrar palabra desde una posicion hasta el final----------
print(b[5:])

#Slice con pocisiones negativas
print(b[-5:-2])

#Boleanos

# Mayor que
print(10 > 9)

#igual que
print(10 == 9)

# menor que
print(10 < 9)

#Variables boleanas
enStock = True
isTiendaAbierta = True

if enStock and isTiendaAbierta:
    print("VENDER PRODUCTOS")

tieneEfectivo = False
tieneTarjeta = True
if tieneTarjeta or tieneEfectivo:
    print("PAGO ACEPTADO")

regresasteconEx = False
if not regresasteconEx:
    print("MENTIROSO")

tienesNovie= False
if not tienesNovie:
    print("FALSO")

paseLenguajes = True
if not paseLenguajes:
    print("REPROBASTE")

isUploded = True
if isUploded:
    print("")
else:
    print("REINTENTAR")

if not isUploded:
    print("REINTENTAR")

# OPERADORES ARITMETICOS
# -------Suma------
x = 5
y = 6
print(x + y)

#--------------Resta-------------
print(x - y)

#---------Multiplicacion-------
print(x * y)

#----------Division---------
print(x / y)

#----------Modulo---------
print(x % y)

#-----------Exponentes--------
print(2 ** 2)
print(x ** 2)
print(y ** 2)

#-----floor division------
print(4 // 2)
print(x // y)

#Operadores de asignacion
x = 30
x += 32
x -= 2
x *= 2
x /= 2
x %= 2
print(x)

#Operadores Logicos de Comparacion
a = 3
b = 2

#----Igual---
print(a == b)

#---Diferente----
print(a != b)

#-----Mayor--
print(a > b)

#-----Menor------
print(a < b)

#-----Mayor igual------
print(a >= b)

#-----Mneor igual------
print(a <= b)


#Operadores Logicos
promedio = 100
asistencias = True
aprobado = (promedio > 70) and asistencias
#------and, not, org------------
print(aprobado)

#Operadores de Indentidad
j = "HOLA"
k = "HOLA "



#Operadores de pertenencia
print("A" in "HOLA")
print("A" not in "HOLA")

#Listas
frutas = ["Manzana", "Banana", "Mango"]
frutas2 = ["🍎", "🍌", "🍋"]
print(frutas)
print(frutas2)

lista = [1, 2, 3, 4, 5, 6]
print(lista)

logico = [True, False, True]
print(logico)

Lista1 = ["abc", 34, True, "a", "🍑"]
print(Lista1)

print(type(lista))
print(lista)

#List, Tuple, Set, Dictionary

"List: Es una colección la cual esta ordenada y modificable, la cual permite duplicados"
"Tuple: Es una coleccion la cual esta ordenada y no es modificable. Permite duplicados"
"Set: Es una coleccion la cual NO❌ esta ordenada, no es modificable ni indexada. No pertmite Duplicados"
"Dictionary: Es una coleccion la cual esta ordenada y es modificable. No permite duplicados"

#---------Lista---------
lista1 = ("🐥", "🐵", "🐷")

print(lista1)
#-----------Tupla
Tupla1 = ("🐥", "🐵", "🐷")

#-----------Set----------
set1 = ("🐥", "🐵", "🐷")

print(set1)

#--------Dictionary----------
diccionario1 = {
    "pollo" : "🐥",
    "monito" : "🐵",
    "cerdito" : "🐷"
}
diccionario1["koala"] = "🐨"
diccionario1["tigre"] = ("🐯")
print(diccionario1["monito"])
print(diccionario1)


"#0 Crear una lista: 1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9"
"#1 Convertir la lista en un set para eliminar duplicados"
"#2 Calcular la suma de los numeros usando una lista"
"#3 Calcular la suma de los numeros usando un set"
"#4 Crear un diccionario para almacenar las estadisticas"
"#  Numeros unicos, suma total lista, suma total set"
"#  Maximo valor, minimo valor"
"#5 Imprimir las estadisticas"

numeros = [1, 2, 2, 3, 4, 4]
numerosSet = set(numeros)
sumaLista = sum(numeros)
sumaSet = sum(numerosSet)
len(numerosSet)
max(numeros)
min(numeros)

###---#1----
Listanumero = (1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9)

#---#2----
numeroSet = set(Listanumero)

#----3-----
sumaNumero = sum(Listanumero)
sumaSet = sum(numeroSet)


#----4----
numeroMaximo = max(Listanumero)
numeroMinimo = min(Listanumero)

diccionario2 = {
    "numeros Unicos" : numeroSet,
    "suma total de la lista" : sumaNumero,
    "suma total del set" : sumaSet,
    "Maximo valor" : numeroMaximo,
    "minimo valor" : numeroMinimo
}
print(diccionario2)

buscar = True
if buscar:
    for frutas in frutas2:
        if frutas == "🍌":
            print("Se encontro: " + frutas)
        else:
            print("NO COINCIDE")
else:
    print("NO SE ESTA BUSCANDO")

buscar = False
if buscar:
    for frutas in frutas2:
        if frutas == "🍌":
            print("Se encontro: " + frutas)
        else:
            print("NO COINCIDE")

#----Continue----

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
        print(1)

#-----Breck----

#---Ciclo while----


#----Truek----
quiereVolver = True
vecesRegresaron = 0
while vecesRegresaron < 3:
    vecesRegresaron += 1
    print("Han vuelto " + str(vecesRegresaron) + " Veces")

#----Condiciones----
a = 200
b = 345

if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")


