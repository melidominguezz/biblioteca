import books_data as bd


def busqueda_libros(clave, valor):
    """Búsqueda de libros segun: título, autor, género, ISBN, editorial, año de publicación, serie.
    :param clave: Str, nombre del campo por el cual se quiere realizar la búsqueda.
    :param valor: Str, valor del campo por el cual se quiere realizar la búsqueda.
    :return libros: List, lista de titulos de libros que coinciden con la clave-valor enviados anteriormente y su status. """
    libros = []
    clave_posicion = [["autor", 0], ["titulo", 1], ["genero", 2], ["ISBN", 3], ["editorial", 4],
                      ["año de publicacion", 5],
                      ["serie", 6], ["nro de paginas", 7], ["ejemplares", 8]]

    indice = [caracteristica[1] for caracteristica in clave_posicion if clave == caracteristica[0]][0]

    for libro in bd.libros:
        if libro[indice] == valor:
            titulo = libro[1]
            disponibilidad = libro[9]
            libros.append([titulo, disponibilidad])

    return libros


def cargar_libros(titulo, autor, genero, ISBN, editorial, anio_publicacion, serie_libros, nro_paginas, cant_ejemplares):
    """Cargar libro en stock de biblioteca. Se pueden cargar varios ejemplares del mismo.
    :param titulo: Str, título del libro.
    :param autor: List, nombre del autor/es del libro.
    :param genero: List, género/s del libro.
    :param ISBN: Int, International Standard Book Number del libro.
    :param editorial: Str, editorial del libro.
    :param anio_publicacion: Int, año de publicacion del libro.
    :param serie_libros: Str opcional, si el libro pertenece a una serie, escribirla. Caso contrario escribir None.
    :param nro_paginas: Int, número de páginas del libro.
    :param cant_ejemplares: Int, cantidad de ejemplares del mismo libro que se está cargando.
    :return libros_cargados: List, lista de libros cargados a la biblioteca. """

    nuevo_libro = []
    # chequear si el libro ya existe en la biblioteca

    libros = sum(fila.count(ISBN) for fila in bd.libros)
    if libros > 0:
        for i, libro in enumerate(bd.libros):
            if libro[3] == ISBN:
                bd.libros[i][8] += cant_ejemplares

    else:
        nuevo_libro = [autor, titulo, genero, ISBN, editorial, anio_publicacion, serie_libros, nro_paginas,
                       cant_ejemplares, True]
        bd.libros.append(nuevo_libro)

    return bd.libros


def obtener_libro(ISBN):
    """ Obtener un libro y su detalle segun su id interno o ISBN.
        :param ISBN: Int, International Standard Book Number del libro.
        :return libro: Dict, informacion detallada del libro buscado.
        """
    libro_encontrado = None
    for libro in bd.libros:
        if libro[3] == ISBN:
            libro_encontrado = libro

    return libro_encontrado


# Tenemos la lista con todos los libros disponibles
# La lista con todos los libros alquilados
# La función compara el libro que se consulta con todos los libros presentes en ambas listas. Si lo encuentra en alguna
# Devuelve el estado pertinente, si no lo encuentra en ninguna de las dos es porque no está en la biblioteca

def estatus_libros(n):
    disponible = ["emma"]
    en_espera = ["orgullo y prejuicio"]
    final = ""

    if n in disponible:
        return "disponible"
    elif n in en_espera:
        return "en_espera"


# Codigo principal

libro = input("Ingrese el libro de su consulta")
libro_buscado = estatus_libros(libro)

if libro_buscado == "disponible":
    print("lo tenemos")
elif libro_buscado == "en_espera":
    print("Ahora está reservado, pero vuelve")
else:
    print("No contamos con ese libro en nuestra biblioteca")
