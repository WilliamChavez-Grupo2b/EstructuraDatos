#listaunidimensional
lista = [1, 2, "Estructura de datos", 4, 5]
print(lista[1]) 
# Bidimensional 3x3 
lista2= [[1,2,"Estructura de datos"], 
         [4,5,6], 
         [7,8,9]]
print(lista2[2][2]) #7
"Busqueda de un elemento en una lista"

elemento = "Estructura de datos"
if elemento in lista:
    print("Elemento encontrado en la lista unidimensional")
if elemento in lista2[0]:
    print("Elemento encontrado en la lista bidimensional")