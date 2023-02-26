#do me a function that parses a file
#Crie um programa em Python que tenha o seguinte comportamento:
#Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
#Prepare o programa para ler o texto do canal de entrada: stdin;
#Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
#Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
#Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.


import sys

print("TPC2")
print("Insira textto:")

state = 1
lines = []


accum = 0
for line in sys.stdin:
    lines.append(line.strip())
    if state:
        if "Off" or "off" or "oFF" or "OFF" or "oFf" or "OfF" in line :
            state = 0 
        
        for thing in lines:
            if "=" in thing:
                print(accum)
                break
            for coisa in thing:
                
                if coisa.isdigit():
                    accum+= int(coisa)
    else:
        if "On" or "on" or "oN" in line:
            state = 1
                

