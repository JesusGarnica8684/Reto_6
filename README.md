# Reto_6

1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado
```mermaid
flowchart TD
    A["Inicio"] --> B["Asignar zahl = 1"]
    B --> C["Definir variable de inicio"]
    C --> D{"¿zahl &lt;= 100?"}
    D -- No --> H["Fin"]
    D -- Sí --> E["Calcular cahl = zahl al cuadrado"]
    E --> F["Imprimir zahl y cahl"]
    F --> G["Incrementar zahl en 1"]
    G --> D

    A@{ shape: rounded}
    H@{ shape: rounded}
    F@{ shape: in-out}
    G@{ shape: rect}
```
```python
if __name__=="__main__":
    zahl = 1 #Variable de inicio en 1
    while zahl <= 100: #el ciclo ira hasta 100
        cahl = zahl ** 2 #cuadrado del numero
        print(zahl, ": ", zahl, "^2=", cahl)
        zahl += 1 #asignacion incremento
```
2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```mermaid
flowchart TD
    A["Inicio"] --> B["Inicializar zahl = 1 (indice impares)"]
    B --> C["Inicializar numb = 2 (indice pares)"]
    C --> D{"¿zahl &lt;= 1000?"}
    D -- Sí --> E["Imprimir zahl"]
    E --> F["Incrementar zahl en 2"]
    F --> D
    D -- No --> G{"¿numb &lt;= 1000?"}
    G -- No --> J["Fin"]
    G -- Sí --> H["Imprimir numb"]
    H --> I["Incrementar numb en 2"]
    I --> G

    A@{ shape: event}
    E@{ shape: in-out}
    J@{ shape: event}
    H@{ shape: in-out}
```
```python
if __name__=="__main__":
    zahl : int = 1 #variable para inicializar impares
    numb : int = 2 #variable para inicializar pares
    
    while zahl <= 1000:
        print(zahl)
        zahl += 2#incremento en impares
    print()
    while numb <= 1000:
        print(numb)
        numb += 2#incremento en pares
```
3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```mermaid
flowchart TD
    A["Inicio"] --> B["Solicitar número inicial (zahl)"]
    B --> C{"¿zahl >= 2?"}
    C -- No --> D["Fin"]
    C -- Sí --> E{"¿zahl es impar?"}
    E -- Sí --> F["Hacer zahl par (zahl = zahl - 1)"]
    F --> G["Imprimir zahl"]
    E -- No --> G
    G --> H["Decrementar zahl (zahl = zahl - 2)"]
    H --> C

    A@{ shape: event}
    B@{ shape: out-in}
    D@{ shape: event}
    G@{ shape: in-out}
```
```python
if __name__=="__main__":

    zahl = int(input("Ingrese el numero con el que desea iniciar: "))

    while zahl >= 2:
        if zahl%2 != 0: # se revisa que el indice sea par
            zahl = zahl-1 # se vuelve par si es necesario
        print(zahl)
        zahl -= 2 # asignacion de decremento
```
4. Imprimir el factorial de un número natural n dado.
```python
def factorial (num : int) -> int:
    fact = 1
    while num > 1: # el indice del while debe ser mayor estricto de uno, pues fact ya hará el producto de 1
        fact *= num # conforme el ciclo while corra se multiplicara por los numeros menores al indice
        num -= 1 # decremento de 1
    return fact

if __name__=="__main__":
    zahl = int(input("Ingrese el numero a calcular su factorial: "))
    print ("El factorial de ", zahl, " es ", factorial(zahl))
```
5. Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.
```python
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
```
6. Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones
```python
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
```
