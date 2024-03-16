# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
#------------------------------------------------------------------

'''
    Nome: Vítor Garcia Comissoli
    NUSP: 11810411

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que p%ortanto não
    constituem desonestidade acadêmica ou plágio.
    Declaro também que sou responsável por todas as cópias desse
    programa e que não distribui ou facilitei a sua distribuição.
    Estou ciente que os casos de plágio e desonestidade acadêmica
    serão tratados segundo os critérios divulgados na página da
    disciplina.
    Entendo que EPs sem assinatura devem receber nota zero e, ainda
    assim, poderão ser punidos por desonestidade acadêmica.

    Abaixo descreva qualquer ajuda que você recebeu para fazer este
    EP.  Inclua qualquer ajuda recebida por pessoas (inclusive
    monitores e colegas). Com exceção de material de MAC0110, caso
    você tenha utilizado alguma informação, trecho de código,...
    indique esse fato abaixo para que o seu programa não seja
    considerado plágio ou irregular.

    Exemplo:

        A monitora me explicou que eu devia utilizar a função int() quando
        fazemos leitura de números inteiros.

        A minha função quicksort() foi baseada na descrição encontrada na
        página https://www.ime.usp.br/~pf/algoritmos/aulas/quick.html.

    Descrição de ajuda ou indicação de fonte:

        Utilizei-me somente de conhecimentos já adiquiridos, além do texto
        explicativo do próprio EP.
'''
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
# random.shuffle()
import random
# time.time()
import time 
#-----------------------------------------------------------------------
def main():
    '''
(None) -> None

Unidade de teste para as funções pedidas no EP.
Escreva outros testes que desejar.
    '''
    print("Testes para o EP09")

# testes da função no_egoistas
    print()
    print("Teste no_egoistas()")
    amigos1 = [1,2,3,4,0]
    amigos2 = [2,1,0,3,4]
    print("    no_egoistas(%s) = %s"%(amigos1, no_egoistas(amigos1)))
    print("    no_egoistas(%s) = %s"%(amigos2, no_egoistas(amigos2)))

# para efeito de reprodutibilidade dos experimentos
    semente = int(input("Digite o valor da semente do gerador de números pseudo-aleatórios: "))
    random.seed(semente)

# parâmetros para os experimentos
    print() # pula linha
    print("Parâmetros para o experimento ")
    ini    = int(input("Digite o número mínimo de pessoas: "))
    fim    = int(input("Digite o número máximo de pessoas: "))
    passo  = int(input("Digite o passo: "))
    T      = int(input("Digite o número de tentativas em cada experimento: "))
    mostre = input("Deseja ver as listas com índices egoistas [s/n]: ")

    print("Teste experimento()")
# estima q(N) para vários valores de N
    for N in range(ini, fim, passo):
# inicie o cronômetro
        t_ini = time.time()
# execute o experimento
        qN, lst_egoistas = experimento(N, T)
# exiba a estimativa do valor de q(N)
        print("q(%d) = %f"%(N, qN))
        if mostre in ['s', 'S']: 
            print("    lista com índices egoistas para q(%d): "%(N))
            tamanho = len(lst_egoistas)
            if tamanho == 0:
                print("      nenhuma lista possui índice esgoísta")
            else:
# transforme listas com egoistas em listas sem 
                for i in range(0, tamanho, 1):
                    print("    antes : ", lst_egoistas[i])
                    altruistas(lst_egoistas[i])
                    print("    depois: ", lst_egoistas[i])
# pare cronômetro            
        t_fim = time.time()
        print("    tempo decorrido: %7.2f ms"%((t_fim - t_ini)*1000))

    print()    
# teste altruismo() n grande
    print("Teste altruismo() para lista grande")
    muito_grande = 1000000
    amigos3  = sorteie_lista(muito_grande)
    amigos3 += [muito_grande] # garante índice egoísta
    print("    no. de egoístas com lista de %d = %s"%(muito_grande, no_egoistas(amigos3)))
    t_ini = time.time() # inicie o cronômetro
    altruistas(amigos3)
    t_fim = time.time() # pare cronômetro 
    print("    no. de egoístas com lista de %d = %s"%(muito_grande, no_egoistas(amigos3)))
    print("    tempo decorrido: %7.2f ms"%((t_fim - t_ini)*1000))
    
#-----------------------------------------------------------------------
def sorteie_lista(n):
    '''
(int) -> list

RETORNA uma lista de tamanho n, contendo os números de 0 a n em 
ordem aleatória.

ATENÇÃO: a tabulação das linhas foi removida e a ordem de algumas 
linhas alterada. A função deve ser consertada antes de ser utilizada.
    '''
    lista = []

    for i in range(n):
        lista += [i]
    
    random.shuffle(lista)
    return lista
#-----------------------------------------------------------------------
def no_egoistas(amigo_de):
    '''(list) -> int

    RECEBE uma lista `amigo_de`.
    RETORNA o número de indices egoistas na lista.
    '''
    # modifique o código abaixo para conter a sua solução.
    
    cont = 0
    n = len(amigo_de)
    lista = amigo_de
    
    for i in range(0, n, 1):
        if lista[i] == i:
            cont += 1
    
    return cont
    
    """
    print("Vixe!! ainda não fiz a função esgoista()")
    return False
    """   
#-----------------------------------------------------------------------
def experimento(N, T):
    '''(int, int) -> float, list

    RECEBE um inteiros positivos N e T.

    Estima a probabilidade q(N) de uma lista de "amigo secreto" 
    com N participantes NÃO ter um índice esgoista.

    A função realiza T sorteios de listas de tamanho N e utiliza 
    como estimador a razão entre o número de listas sem egoistas e T.

    RETORNA a probabilidade estimada para q(N) e uma lista formada
    por todas as listas com índices egoístas sorteadas durante 
    o experimento.
    '''
    # modifique o código abaixo para conter a sua solução.
    
    # T = num de sorteios
    # N = tamanho das listas
    # S = num de listas egoístas
    # prob = (T - S) / T
    
    S = 0
    cont = 0
    lista_de_listas = []
    
    for i in range(0,T,1):
        lista = sorteie_lista(N)
        S = no_egoistas(lista)
        if S > 0:
            lista_de_listas += [lista]
        if S == 0:
            cont += 1
            
    prob = cont / T
    
    return prob, lista_de_listas
    
    """
    print("Vixe!! ainda não fiz a função experimento()")
    return 0, []  # retorna uma estimativa probabilidade e uma lista de listas
    """
#-----------------------------------------------------------------------
def altruistas(amigo_de):
    ''' (list) -> None

    RECEBE uma lista amigo_de e troca a posição de elementos da lista
    de tal forma a não possuir índices egoístas.
    '''
    # modifique o código abaixo para conter a sua solução.
    
    egoista = True
    n = len(amigo_de)
    
    while egoista:
        a = amigo_de[0]
        for i in range(0,n-1,1):
            amigo_de[i] = amigo_de[i+1]
        amigo_de[n-1] = a
        if no_egoistas(amigo_de) == 0:
            return
    """  
    while i < n and egoista:
        if amigo_de[i] == i and i < n-1:
            a = amigo_de[i]
            amigo_de[i] = amigo_de[i+1]
            amigo_de[i+1] = a
        elif amigo_de[i] == i and i == n-1:
            a = amigo_de[i]
            amigo_de[i] = amigo_de[0]
            amigo_de[0] = a
        if no_egoistas(amigo_de) == 0:
            egoista = False
        else:
            i += 1
    """
    '''
    egoista = True
    n = len(amigo_de)
    a = amigo_de[:]
    
    while egoista:
        random.shuffle(a)
        if no_egoistas(a) == 0:
            egoista = False
            for i in range(0, n, 1):
                amigo_de[i] = a[i]
    '''
    """
    print("Vixe!! ainda não fiz a função altruistas()")
    """
#=====================================================================
# Não modifique as linhas abaixo
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático
if __name__ == '__main__':
    main()
