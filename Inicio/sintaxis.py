#Práctica 2: Sintaxis Python

#1. Comentarios
#Cometario de una línea
'''
Soy un
comentario
de
varias líneas
'''
#2. Cadenas
print('Soy una cadena')
print("Soy otra cadena")

a = 'Mi banda favorita\nes:'
b = "Imagine Dragons"

print(a+b)
print (a,b)

#Funciones para cadenas
print(len(a))

print(b)
print(b[2:5])
print(b[:5])
print(b[2:])

#3. Variables
x = 5
y = "john"

z = int(3)
w = str("mike")
v = float(3.5)

print(x)
print(y)

print(z)
print(w)
print(v)

print(type(x))
print(type(y))
print(type(z))
print(type(w))
print(type(v))

import random
numero = random.randrange(1,15)
print(numero)

#4. Solicitud de datos
var1 = input("Introduce cualquier dato: ")
var2 = str(input("Introduce una cadena: "))
var3 = int(input("Introduce un número entero: "))
var4 = float(input("Introduce un número decimal: "))
print(var1, var2, var3, var4)

#5. Booleans y Operadores de Comparación y Lógicos
print(10 > 9)
print(10 == 9)
print(10 < 9)
print(10 >= 9)
print(10 != 9)
print(10 <= 9)

x = 1
print(x < 5 and x < 10)
print(x < 5 or x < 10)
print(not(x < 5 and x < 10))

#Operaciones Binarias
print(x < 5 & x < 10)
print(x < 5 | x < 10)
print(not(x < 5 & x < 10))