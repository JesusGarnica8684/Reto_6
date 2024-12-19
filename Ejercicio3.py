# Imprimir los números pares en forma 
# descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
if __name__=="__main__":

    zahl = int(input("Ingrese el numero con el que desea iniciar: "))

    while zahl >= 2:
        if zahl%2 != 0: # se revisa que el indice sea par
            zahl = zahl-1 # se vuelve par si es necesario
        print(zahl)
        zahl -= 2 # asignacion de decremento