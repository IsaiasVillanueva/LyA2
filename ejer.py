nombre= input('Ingrese su nombre: ')
mi_lista= nombre.split('-')
nombre_completo=[]
for palabra in mi_lista:
    nombre_completo.append(palabra.capitalize())

print(' '.join(nombre_completo))