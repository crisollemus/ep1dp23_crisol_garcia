from sa import SociedadAnonima

def ingresar_datos():
    codigo= input("Ingrese código del centro educativo:")
    nombre= input("Ingrese nombre del centro educativo:")
    direccion= input("Ingrese direccion del centro educativo:")
    telefono= input("Ingrese telefono del centro educativo:")
    director= input("Ingrese nombre del director del centro educativo:")
    url= input("Ingrese URL del centro educativo:")
    cantidad_hombres= input("Ingrese cantidad de hombres del centro educativo:")
    cantidad_mujeres= input("Ingrese cantidad de mujeres del centro educativo:")
    nombre_sa=input("Ingrese  nombre de sociedad anonima:")
    representante=input("Ingrese  nombre del representante")
    correo_representante=input("Ingrese correo del representante:")

    sa=SociedadAnonima(codigo,nombre,direccion,telefono,director,url,cantidad_hombres,cantidad_mujeres,nombre_sa,representante,correo_representante)
    return sa



def ingresar_datos():
    codigo = input("Ingrese código del centro: ")
    nombre = input("Ingrese nombre del centro: ")
    direccion = input("Ingrese dirección del centro: ")
    telefono = input("Ingrese teléfono del centro: ")
    director = input("Ingrese director del centro: ")
    url = input("Ingrese URL del centro: ")
    cantidad_hombres = int(input("Ingrese cantidad de hombres: "))
    cantidad_mujeres = int(input("Ingrese cantidad de mujeres: "))
    nombre_sa = input("Ingrese nombre de la Sociedad Anónima: ")
    representante = input("Ingrese nombre del representante: ")
    representante_correo = input("Ingrese correo del representante: ")
    
    sa = SociedadAnonima(codigo, nombre, direccion, telefono, director, url, cantidad_hombres, cantidad_mujeres, nombre_sa, representante, representante_correo)
    return sa

def mostrar_datos(lista): 
    print("\nDatos de los Centros Ingresados:")
    print("{:<10} {:<20} {:<20} {:<15} {:<20} {:<30} {:<10} {:<10} {:<20} {:<20} {:<30}".format(
        "Código", "Nombre", "Dirección", "Teléfono", "Director", "URL", "Hombres", "Mujeres", "Nombre SA", "Representante", "Correo Rep."))
    for sa in lista:
        print("{:<10} {:<20} {:<20} {:<15} {:<20} {:<30} {:<10} {:<10} {:<20} {:<20} {:<30}".format(
            sa.codigo, sa.nombre, sa.direccion, sa.telefono, sa.director, sa.url, sa.cantidad_hombres, sa.cantidad_mujeres, sa.nombre_sa, sa.representante, sa.representante_correo))

def main():
    lista_centros = []
    for _ in range(5):
        print("\nIngreso de datos para el centro #{}".format(_ + 1))
        centro = ingresar_datos()
        lista_centros.append(centro)

    mostrar_datos(lista_centros)

if __name__ == "__main__": 
    main()