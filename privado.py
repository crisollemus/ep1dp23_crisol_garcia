from centro_educativo import CentroEducativo

class Privado (CentroEducativo):
 def __init__(self, codigo, nombre, direccion, telefono, director, url, cantidad_hombres, cantidad_mujeres):
  super().__init__(codigo, nombre, direccion, telefono, director, url)
  self.cantidad_hombres=cantidad_hombres
  self.cantidad_mujeres=cantidad_mujeres
  