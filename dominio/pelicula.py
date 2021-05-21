class Pelicula:
    # iniciamos la variable de contador en el valor 0
    contador_pelicula = 0
    # recivimos el parametro del self y el del nombre de la pelicula

    def __init__(self, nombre, genero, idioma, actores):
        # suma un 1 por cada pelicula que lleguen
        Pelicula.contador_pelicula += 1
        # definimos nustra variable contador
        self.__id_pelicula = Pelicula.contador_pelicula
        # definimos nuestro atributo privado y la asignamos nuestro argumento que es nombre
        self.__nombre = nombre
        self.__genero = genero
        self.__idioma = idioma
        self.__actores = actores

    # Definimos el metodo con el parametro de self
    def __str__(self):
        # Regresamos la cadena con los atributos del objeto
        return "Id Pelicula: " + str(self.__id_pelicula)+" " + " Título de la Pelicula: "+self.__nombre + " " + "Genero: "+self.__genero + " " + " Idioma: " + self.__idioma + " " + " Actores o Autoras: " + " " + self.__actores+" "

    # Definimos el metodo de get para obtener el atributo
    def get_nombre(self):
        # acedemos al atributo de nombre de tipo privado
        return self.__id_pelicula+self.__nombre+self.__genero+self.__idioma+self.__actores
    # Colocamos el atributo de nombre

    def set_nombre(self, nombre, genero, idioma, actores):
        self.__id_pelicula
        # usalmos el parametrp de self y le asignamos un nuevo nombre
        self.__nombre = nombre
        self.__genero = genero
        self.__idioma = idioma
        self.__actores = actores
