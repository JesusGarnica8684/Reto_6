# Imprimir el factorial de un número natural n dado
def factorial (num : int) -> int:
    fact = 1
    while num > 1: # el indice del while debe ser mayor estricto de uno, pues fact ya hará el producto de 1
        fact *= num # conforme el ciclo while corra se multiplicara por los numeros menores al indice
        num -= 1 # decremento de 1
    return fact

if __name__=="__main__":
    zahl = int(input("Ingrese el numero a calcular su factorial: "))
    print ("El factorial de ", zahl, " es ", factorial(zahl))
