import sys

#idade,sexo,tensão,colesterol,batimento,temDoença
f = open("myheart.csv","rt")



next(f)

bigList = []
nList = []
def to_list(f):
    
    
    
    for linha in f:
        
        lista = linha.split(",")
        lista[5]= lista[5][0]
        bigList.append(lista)
       

    return bigList

    

def to_tuples(bigList):
    
    for thing in bigList:
        elem = tuple(thing)
        nList.append(elem)
    print(nList)
    return nList

def testage(nList):
    idades=[]
    for coisa in nList:
        age =coisa[0]
        idades.append(age)
    idades.sort()
    idades.reverse()
    print(idades)
    

    
testage(to_tuples(to_list(f)))
    
           

#distribution sick : M & F
#* Crie uma função que lê a informação do ficheiro para um modelo, previamente pensado em memória;
#* Pense num modelo para guardar uma distribuição;
# Crie uma função que calcula a distribuição da doença por sexo;
#* Crie uma função que calcula a distribuição da doença por escalões etários. Considere os seguintes escalões: [30-34], [35-39], [40-44], ...
#* Crie uma função que calcula a distribuição da doença por níveis de colesterol. Considere um nível igual a um intervalo de 10 unidades, comece no limite inferior e crie os níveis necessários até abranger o limite superior;
#* Crie uma função que imprime na forma de uma tabela uma distribuição;
#* Especifique um programa que ao executar apresenta as tabelas correspondentes às distribuições pedidas;
#* Extra: explore o módulo matplotlib e crie gráficos para as suas distribuições.