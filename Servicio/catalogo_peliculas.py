import os 

class CatalogoPeliculas:
    
    ruta_archivo = "peliculas.txt"
    
    @staticmethod           
    
    def agregar_pelicula(pelicula):
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            archivo.write(pelicula)
        except Exception as e:
            print("Ocurrio una excepcion al agregar: ", e)
        finally:
            archivo.close()
            
    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print ("Catalogo de peliculas")
            print(archivo.read())
        except Exception as e: 
            print("Ocurrio un error al momento de listar peliculas: ", e)
        finally:
            archivo.close()
    
    @staticmethod
    def eliminar():
        try: 
            os.remove(CatalogoPeliculas.ruta_archivo)
            print("Archivo eliminado: ",CatalogoPeliculas.ruta_archivo)
        except Exception as e:
             print("Ocurrio un error al eliminar peliculas: ", e)