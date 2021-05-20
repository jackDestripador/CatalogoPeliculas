class Pelicula:
    # recivimos el parametro del self y el del nombre de la pelicula
    def __init__(self, nombre, genero):
        # definimos nuestro atributo privado y la asignamos nuestro argumento que es nombre
        self.__nombre = nombre
        self.__genero = genero

    # Definimos el metodo con el parametro de self
    def __str__(self):
        # Regresamos la cadena con los atributos del objeto
        return "Título de la Pelicula: "+self.__nombre + "Genero: "+self.__genero

    # Definimos el metodo de get para obtener el atributo
    def get_nombre(self):
        # acedemos al atributo de nombre de tipo privado
        return self.__nombre+self.__genero
    # Colocamos el atributo de nombre

    def set_nombre(self, nombre, genero):
        # usalmos el parametrp de self y le asignamos un nuevo nombre
        self.__nombre = nombre
        self.__genero = genero
