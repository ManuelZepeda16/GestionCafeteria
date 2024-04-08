def validFormat(array):
    #Separar la entrada por comas
    splitArray = array.split(",")
    
    #Eliminar los espacios en blanco alrededor de los elementos
    for i in range(0, len(splitArray)):
        splitArray[i] = splitArray[i].strip()
    
    #Verificar el largo mínimo y máximo
    if len(splitArray) == 0 or len(splitArray) == 1 or len(splitArray) > 6:
        return False
    
    #Verificar que el primer valor sea un alpha y que los demás sean números
    for i in range(1, len(splitArray)):
        if not splitArray[0].isalpha() or not splitArray[i].isnumeric():
            return False

    #Verificar el largo del nombre
    if len(splitArray[0]) < 2 or len(splitArray[0]) > 15:
        return False

    #Quitar el nombre de la lista
    splitArray.pop(0)

    #Pasar a valores enteros la lista resultante
    intList = [int(x) for x in splitArray]

    #Comprobar el rango de los números 
    for i in range(0, len(intList)):
        if intList[i] < 1 or intList[i] > 48:
            return False
    
    #Verificar que los valores sean ingresados en orden y que estos no se repitan
    if intList != sorted(set(intList)):
        return False
    
    return True



