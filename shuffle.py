"""Se genera modulo para mezclar las distintas alternativas
    
 """

import preguntas
import random

def shuffle_alt(preguntas):
    random.shuffle(preguntas['alternativas'])
    return preguntas['alternativas']


if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    print(shuffle_alt(preguntas.pool_preguntas['basicas']['pregunta_1'])) 
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]