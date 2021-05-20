# libreria o Blivlioteca que nos permite modificar los archivos del sistema
import os


class CatalogoPeliculas:

    ruta_archivo = "peliculas.txt"

    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            # "a" - modo append
            # Abrimos el archivo
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            # Escribimos en el archivo
            archivo.write(pelicula.__str__()+"\n")
        except Exception as e:
            # En caso de que no exista el archivo mandamos un mensaje de error
            print("Ocurrió una excepción al agregar: ", e)
        finally:
            # Cerramos el archivo
            archivo.close()
    # metodo para acceder a los metodos de la clase

    @staticmethod
    def listar_peliculas():
        try:
            # Abrimos el archivo
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print("Catálogo de Películas:")
            print(archivo.read())
        except Exception as e:
            print("Ocurrió un error al listar películas: ", e)
        finally:
            archivo.close()

    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print("Archivo eliminado: ", CatalogoPeliculas.ruta_archivo)
        except Exception as e:
            print("Ocurrió un error al eliminar películas:", e)
