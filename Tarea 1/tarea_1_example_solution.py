"""Tarea 1.

Tarea 1 - Ejemplo de solución para comprobar con Pytest
- Microprocesadores y microcontroladores
Sergio Andrés García Acuña y Alejandro Zamora Llach

"""


def filtrar_vocales(cadena, bandera):
    """Funcion filtrar_vocales.

    La presente función filtra las vocales o
    consonantes de una cadena de texto que es
    el parámetro cadena, segun
    el parametro bandera True o False.

    Parametros:
        cadena (str): cadena de texto a filtrar
        bandera (bool): True para filtrar vocales, False para
        filtrar consonantes

    Retorna:
        estado (int): codigo de error
        string_filtrado (str): cadena filtrada con las vocales o consonantes

        Estado:
        -100: El parámetro cadena no es string.
        -200: La cadena posee valores no alfabéticos.
        -300: La cadena es un string vacío.
        -400: La cadena tiene mas de 30 caracteres.
        -500: La bandera no es un booleano.
        0: Ejecución exitosa.
    """
    if not isinstance(cadena, str):
        # Isinstance es una función que comprueba
        # si la variable es str
        return -100, None
    else:
        print('Es un string')
    if len(cadena) == 0:
        # Si el string es vacio, su longitud es 0
        # y len comprueba efectivamente si es 0S
        return -300, None
    else:
        print('No es un string vacio')
    if not cadena.isalpha():
        # isalpha es un metodo para strings que comprueba
        # si el string contiene solo letras alfabeticas
        return -200, None
    else:
        print('Solo tiene letras del abecedario')
    if (len(cadena) > 30):
        # len permite comprobar la longitud de la cadena,
        # si es mayor a 30 devuelve el error
        return -400, None
    else:
        print('El string tiene menos de 30 caracteres')
    if not isinstance(bandera, bool):
        # se usa isinstance al igual que anteriormente
        # pero para comprobar si la variable es booleana
        # si no lo es devuelve el error
        return -500, None
    else:
        print('Bandera es del tipo booleano')
    # Se inicializa una variable para guardar el string filtrado
    string_filtrado = ''
    if bandera:
        # Si la bandera es verdadera se filtran las vocales
        for letra in cadena:
            for vocal in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
                # Se recorre la cadena y se compara con las vocales
                if letra == vocal:
                    # Si se encuentra una vocal se concatena
                    string_filtrado = string_filtrado + letra
                else:
                    # Si no se encuentra una vocal se pasa
                    pass
    else:
        # Si la bandera es falsa se filtran las consonantes
        for letra in cadena:
            if letra not in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
                # Se recorre la cadena y se busca en este
                # caso que no este en las vocales
                string_filtrado = string_filtrado + letra
            # Si se encuentra una consonante se concatena
            else:
                pass
            # Si no se encuentra una consonante se pasa
    return 0, string_filtrado
    # Si no hubo ningun error se devuelve el string filtrado y el codigo 0
    # que es el codigo de exito


def encontrar_extremos(lista_numeros):
    """Función encontrar_extremos.

    Esta función encuentra el valor mínimo
    y máximo de una lista de números ingresada
    como parámetro y los retorna.

    Parámetro:
        lista_numeros: lista que debe contener únicamente valores
        de tipo int o float.

    Retorna:
        Tres valores en el siguiente orden:
        estado, minimo, maximo.

        Estado:
        -600: El parámetro ingresado no es una lista.
        -700: La lista contiene un elemento no numérico.
        -800: La lista está vacía.
        -900: La lista contiene más de 15 elementos.
        0: Ejecución exitosa.

        Cuando ocurre un error, minimo y maximo son None.
    """
    # Verificar que el parámetro ingresado sea una lista.
    if not isinstance(lista_numeros, list):
        return -600, None, None

    # Verificar que todos los elementos sean números.
    # Se excluyen los booleanos porque Python considera
    # un booleano como un entero
    for numero in lista_numeros:
        if isinstance(numero, bool):
            # Comprueba que la variable sea
            # de la clase deseada
            return -700, None, None

        if not isinstance(numero, (int, float)):
            # Comprueba que la variable sea de la clase
            # deseada pero esta negada por el not
            return -700, None, None

    # Verificar que la lista no esté vacía.
    if len(lista_numeros) == 0:
        return -800, None, None

    # Verificar que la lista no tenga más de 15 elementos.
    if len(lista_numeros) > 15:
        return -900, None, None

    # Obtener el valor mínimo y máximo de la lista.
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    # Retornar código de estado, mínimo y máximo.
    return 0, minimo, maximo
