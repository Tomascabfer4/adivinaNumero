#########################################################################################################
###ANALISIS###
#########################################################################################################
#Para empezar el juego hay que generar un número aleatorio del 1 al 200.
#Para ello importaremos random.
#También queremos un contador para los 10 intentos del usuario.
#Si no a acertado el número y quedan intentos:
#Lee un número.
#Veo si ese número coincide con el número que ha generado random y digo si es mayor o menor.
#Vuelvo a pedir un número.
#El bucle termina:
#1º: Si ha ganado, muestra mensaje de enhorabuena y los intentos gastados.
#2ª: De lo contrario si no lo ha adivinado y a gastado los 10 intentos, mostrar el número que
#era y un mensaje indicando que no a conseguido resolver el número.
#########################################################################################################
###DISEÑO###
#########################################################################################################
#Generar un número aleatorio del 1 al 200 <--- num_aleatorio.
#El usuario que está ejecutando el programa tiene 10 intentos.
#Leer num_seleccion.
#Mientras num_seleccion sea distinto a num_aleatorio e intentos sea mayor que 1.
#Si num_aleatorio es mayor a num_seleccion ---> Escribir "El número es mas bajo".
#Si num_aleatorio es menor a num_seleccion ---> Escribir "El número es mas alto".
#intentos <--- intentos - 1.
#Escriibir intentos.
#Leer num_seleccion.
#Si num_secreto es igual a num_seleccion ---> Escribir "¡Ehnorabuena! Has adivinado el número en ",11-intentos," intentos."
#Sino ---> Escribir "Lo siento no lo has adivinado, el numero era: ",num_aleatorio.
#########################################################################################################
import random
intentos = 10
num_aleatorio = random.randint(1,200)
num_seleccion = int(input("Adivina el número del 1 al 100:\n"))
while num_aleatorio != num_seleccion and intentos > 1:
    if num_aleatorio>num_seleccion:
        print ("El número es mas alto")
    else:
        print ("El número es mas bajo")
    intentos = intentos -1
    print("Le quedan ",intentos," intentos")
    num_seleccion = int(input("Adivina el numero del 1 al 100:\n"))
if num_aleatorio == num_seleccion:
    print("¡Ehnorabuena! Has adivinado el número en ",11-intentos," intentos.")
else:
    print("Lo siento no lo has adivinado, el numero era: ",num_aleatorio)
