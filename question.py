import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.

opciones = {'basicas': [1,2,3],
            'intermedias': [1,2,3],
            'avanzadas': [1,2,3]}
###############################################


def choose_q(dificultad):
    # Escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]
    
    global opciones
    # Selecciona pregunta al azar
    seleccion = random.choice(opciones[dificultad])
    # Elimina del ambiente global para no escogerla de nuevo   
    opciones[dificultad].remove(seleccion)

    # Escoger enunciado y alternativas mezcladas
    pregunta = preguntas[f'pregunta_{seleccion}']
    alternativas = shuffle_alt(pregunta)
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')