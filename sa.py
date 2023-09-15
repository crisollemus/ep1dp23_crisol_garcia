from privado import Privado

class SociedadAnonima(Privado):
    def __init__(self, codigo, nombre, direccion, telefono, director, url, cantidad_hombres, cantidad_mujeres,nombre_sa,representate,representante_correo):
        super().__init__(codigo, nombre, direccion, telefono, director, url, cantidad_hombres, cantidad_mujeres)
        self.nombre_sa=nombre_sa
        self.representante=representate
        self.representante_correo=representante_correo
        