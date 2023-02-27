
#Crie um programa em Python que tenha o seguinte comportamento:
#Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
#Prepare o programa para ler o texto do canal de entrada: stdin;
#Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
#Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
#Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

import sys

accum = 0
state = True

for line in sys.stdin:
        line = line.strip()
        if line.lower() == 'off':
            state = False
        elif line.lower() == 'on':
            state = True
        elif '=' in line:
            print(accum)
        elif state:
            curr_num = ''
            for char in line:
                if char.isdigit():
                    curr_num += char
                elif curr_num:
                    accum += int(curr_num)
                    curr_num = ''

            if curr_num:
                accum += int(curr_num)



