import preguntas as p
from print_preguntas import print_pregunta


def verificar(alternativas, choice):
    correct_alt = [alt for alt in alternativas if alt[1] == 1][0] 
    if choice == correct_alt[0]:
        print('Correcto.')
        return True
    else:
        print(f'Incorrecto.')
        return False



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)






