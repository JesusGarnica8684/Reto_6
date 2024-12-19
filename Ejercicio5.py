# Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores
def divisores (num : int) -> int: # la funcion calcula los divisores del numero por medio de dividirlo sobre un denominador
    den = 1 # se inicializa el denominador en 1
    print ("Los divisores de ", num, " son: ")
    while den < num: # el denominador debe ser menor estricto al numerador
        if num % den == 0 : # se evalua si es un divisor (tiene residuo 0)
            print (den) # conforme se confirma el divisor se imprime
        den += 1 # incremento de 1
    return num # regresa la variable de ingreso puesto todo numero es divisor de si mismo

if __name__=="__main__":
    zahl : int = 2
    while zahl <= 50: # se genera un bucle para evaluar los divisores de 2 a 50 
        print (divisores(zahl))
        zahl += 1 