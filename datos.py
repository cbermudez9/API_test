import llamado



def alives():
    cadena = llamado.api_llamado()
    nombre = " 'name'"
    siguiente_caracter = ","
    i = 0

    while True:
        x = cadena.find(nombre, i) #encontrar la posicion de " 'name'"

        if x == -1: #si es -1 se finaliza
            break

        y = x + len(nombre)  #posicion posterior a name
        f = cadena.find(siguiente_caracter, y) #encontrar la poscion del siguiente_caracter despues del nombre

        if f == -1:
            continuidad = cadena[y:]  # continuar en la cadena, posicion despues de name
        else:
            continuidad = cadena[y:f] #obtener la subcadena

        print("Personaje vivo" + continuidad) #imprimir subcadena

        i = f + 1 #actualizar posicion en la cadena