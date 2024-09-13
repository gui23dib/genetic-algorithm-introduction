
###
# Guilherme Dib da Silva
# Kadish Bernardo Ribeiro da Silva
# Larissa Sena Pereira
# Murilo Mendes Santo Sardão
# Thiago de Andrade Prado
# Victor Eduardo Rodrigues de Abreu e Silva
###
import random

class populacao:
  cromossomos = []
  pontuacao = -1

  def __init__(self, cromossomos, pontuacao):
    self.cromossomos = cromossomos
    self.pontuacao = pontuacao
    

def popular(pop, numpop, word_length):
    if pop == None or len(pop) == 0:
        lista = []
        for _ in range(numpop):
            temp = []
            for __ in range(word_length):
                temp.append(random.randint(65, 90))
            lista.append(populacao(temp, -1))

        return lista    
    else:
        return pop

def avaliar(pop , obj):

    for individuo in pop:
        pontuacao = 0
        count = 0
        for gene in individuo.cromossomos:
            pontuacao += pow((obj[count] - gene), 2)
            count += 1

        if pontuacao == 0: individuo.pontuacao == 0
        elif pontuacao == 1: individuo.pontuacao = 0.1
        else: individuo.pontuacao = (1 / pontuacao) 
    
    return pop

def reproduzir(A, B):
    length = len(A.cromossomos)
    result = ([], [])

    point = random.randint(0, length - 1)
    for i in range(length):
        result[0 if i < point else 1].append(A.cromossomos[i])
        result[1 if i < point else 0].append(B.cromossomos[i])
    
    return (mutacao(result[0]), mutacao(result[1]))


def mutacao(X):
    for i in range(len(X)):
        if random.randint(0, 999) <= 4: # 0.05 chance
            atual = X[i]
            X[i] = random.randint(65, 90)
            while(X[i] == atual):
                X[i] = random.randint(65, 90)
    return X


def selecionar_torneio(pop, pop_len):
    idx_A = random.randint(0, pop_len - 1)
    idx_B = random.randint(0, pop_len - 1)
    while idx_A == idx_B:
        idx_B = random.randint(0, pop_len - 1)
        
    return reproduzir(pop[idx_A], pop[idx_B])


def print_populacao(pop):
    for i in range(len(pop)):
        print_individuo(pop[i])
        
def print_individuo(c):
    for p in c.cromossomos:
        print(chr(p), end=" ")
    print(" = ", c.pontuacao)


def elitismo(pop, populacao_nova, n_surv):
    for i in range(n_surv):
        populacao_nova.append(pop[i])
    
    return populacao_nova
        


palavra_obj = 'ARTIFICIAL' #str(input())
obj = [ord(e) for e in palavra_obj]

pop_length = len(palavra_obj) * 10
pop_sample = popular(None, pop_length, len(obj))
count = 0
while pop_sample[0].pontuacao != 0.0:
    pop_sample = avaliar(pop_sample, obj)
    pop_sample = sorted(pop_sample, key=lambda x: x.pontuacao, reverse=True)

    print(count)
    print_individuo(pop_sample[0])
    print_individuo(pop_sample[99])
    count += 1

    # print_populacao(pop_sample)

    populacao_nova = elitismo(pop_sample, [], 2)
    while len(populacao_nova) < pop_length:
        filhos_novos = selecionar_torneio(pop_sample, pop_length)
        populacao_nova.append(populacao(filhos_novos[0], -1))
        populacao_nova.append(populacao(filhos_novos[1], -1))

    # print_populacao(populacao_nova)
    pop_sample = populacao_nova

print_individuo(pop_sample[0])