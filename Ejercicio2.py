# Imprimir un listado con los números impares desde 1 hasta 999 y 
# seguidamente otro listado con los números pares desde 2 hasta 1000.
if __name__=="__main__":
    zahl : int = 1 #variable para inicializar impares
    numb : int = 2 #variable para inicializar pares

    while zahl <= 1000:
        print(zahl)
        zahl += 2 #incremento en impares
    print()
    while numb <= 1000:
        print(numb)
        numb += 2 #incremento en pares