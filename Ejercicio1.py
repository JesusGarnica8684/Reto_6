#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado
if __name__=="__main__":
    zahl : int = 1 #Variable de inicio en 1
    while zahl <= 100: #el ciclo ira hasta 100
        cahl = zahl ** 2 #cuadrado del numero
        print(zahl, ": ", zahl, "^2=", cahl)
        zahl += 1 #asignacion incremento