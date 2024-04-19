import os

os.system

#Ejercicio 1

# for x in range (5):
#   print (x)

#Ejercicio 2

# for x in "hola":
#   print (x)

#Ejercicio 3

# for x in range (5):
#   x= x +2
#   print (x)

#Ejercicio 4

# n = 5
# fact = 1

# for x in range (1, n+1):
#   fact = fact * x

# print ("el factorial de 5 es : ", end="")
# print(fact)

#Ejercicio 5

# while True:
#   num = int(input("ingrese un numero"))
#   if (num%2==0):
#     continue
#   else:
#     result = num * 4
#     print(f"el numero {num} multiplicado por 4 es: {result}")
#     break

#Ejercicio 6

# base = int(input("ingrese valor de base"))

#Ejercicio 7

num = int(input("ingrese numero"))
list_residuo = []
zeros = []

if num==2:
  print (f"{num} es numero primo")
elif num%2==0:
  print(f"{num} No es numero primo")
else:
  for x in range(3,num+1,2):
    residuo = num%x
    list_residuo.append(residuo)
  for j in list_residuo:
    if j == 0:
      zeros.append(j)
  if len(zeros) > 1:
    print(f"{num} No es numero primo")
  else:
    print(f"{num} Es un numero primo")  

#Ejercicio 8


