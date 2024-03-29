"""Se genera validador para saber si opcion ingresada esta dentro de mi rango

"""

def validate(opciones, eleccion):
    # Ciclo while con not in para revisar si el elemento no esta en mi lista
    while eleccion not in opciones:
        print(f'La opcion no es valida, ingrese una opcion valida: {', '.join(opciones)}')
        eleccion = input('Ingrese una opcion: ').lower()
        
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    opciones = ['0','1']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    validate(opciones, eleccion)
    
    
    
