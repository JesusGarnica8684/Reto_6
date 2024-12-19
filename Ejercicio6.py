# Implementar el algoritmo que muestre los números primos del 1 al 100. 
def divisores (num : int) -> bool: 
    bandera = False 
    # un primo es un numero que solo es divisble entre el mismo y 1, puesto que todo numero ya es divisible 
    # sobre uno y el mismo los dos casos se deprecían y se busca los números que tengan más de un divisor.
    den = 2 # se inicializa el denominador en 2, de esta manera se evita la divison sobre uno
    while den < num: # el denominador debe ser menor estricto al numerador, no se puede dividir sobre si mismo
        if num % den == 0: # se evalua si es un divisor de numeros diferentes
            bandera = True # si lo es, se asigna valor verdadero a un booleano
        den += 1 
    return bandera # regresa el booleano (el numero no es primo)

if __name__=="__main__":
    zahl : int = 2
    while zahl <= 100: # se genera un bucle para evaluar los divisores de 2 a 100
        flag = divisores(zahl) # se llama la funcion y se toma el valor booleano
        if flag != True: # si el valor booleano no es verdadero, o sea (no es primo), 
        # el numero no-no es primo, por doble negacion la logica es verdadera, es primo
            print (zahl, " es primo.") 
        zahl += 1 