def busqueda_libros(clave, valor):
    """Búsqueda de libros segun: título, autor, género, ISBN, editorial, año de publicación, serie.
    :param clave: Str, nombre del campo por el cual se quiere realizar la búsqueda.
    :param valor: Str, valor del campo por el cual se quiere realizar la búsqueda.
    :return libros: List, lista de titulos de libros que coinciden con la clave-valor enviados anteriormente y su status. """


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


def obtener_libro(id_libro, ISBN):
    """ Obtener un libro y su detalle segun su id interno o ISBN.
        :param id_libro: Str, titulo del libro.
        :param ISBN: Int, International Standard Book Number del libro.
        :return libro: Dict, informacion detallada del libro buscado.
        """


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
