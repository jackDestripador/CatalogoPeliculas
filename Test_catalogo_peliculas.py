# importamos nuestra clase
from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas

opcion = None
while opcion != "4":
    print("Opciones:")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catálogo de películas")
    print("4. Salir")
    opcion = input("Escribe tu opción (1-4): ")
    if opcion == "1":
        nombre_pelicula = input("Proporciona el Nombre de la pelicula: ")
        genero_pelicula = input("Proporciona el Genero de la pelicula: ")
        idioma_pelicula = input("Proporciona el Idioma de la pelicula: ")
        actores_pelicula = input(
            "Proporciona el actor o lo autores  de la pelicula: ")
        pelicula = Pelicula(nombre_pelicula, genero_pelicula,
                            idioma_pelicula, actores_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == "2":
        CatalogoPeliculas.listar_peliculas()
    elif opcion == "3":
        CatalogoPeliculas.eliminar()
else:
    print("Salimos del programa...")
