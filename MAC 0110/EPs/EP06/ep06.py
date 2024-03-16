# -*- coding: utf-8 -*-
# ------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
# ------------------------------------------------------------------

"""
    Nome: Vítor Garcia Comissoli
    NUSP: 11810411

    Ao preencher esse cabeçalho com o meu nome e o meu número USP,
    declaro que todas as partes originais desse exercício programa (EP)
    foram desenvolvidas e implementadas por mim e que portanto não
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
        
        Não utilizei-me de nada fora do aprendido em sala de aula e/ou nos
        Fóruns da disciplina.
        
"""
#----------------------------------------------------    
def primo(n):
    '''(int) -> bool

       Recebe um número inteiro n e retorna True se n é primo.
       Em caso contrário a função retorna False.
    '''
    n1 = n - 1
    Primo = False
    
    if n == 1:
        return False
    if n < 0:
        return False
    
    while Primo == False:
        if n % n1 == 0 and n1 != 1:
            return False
        elif n % n1 == 0 and n1 == 1:
            return True
        else:
            n1 = n1 - 1
        
#----------------------------------------------------        
def goldbach(n):
    '''(int) -> bool, int, int 

       Recebe um número inteiro n e retorna True se n pode
       ser escrito como a soma de dois nḿeros primos. 
       Nesse caso a função deve retornar dois números primos
       p e q tais que p + q == n.

       Em caso contrário a função retorna False, 0, 0.
    '''
    p = 1
    q = n - 1
    gold = False
    
    while not gold and p < n and q > 0:
        if primo(p) and primo(q) == True:
            gold = True
        else:
            p += 1
            q -= 1
    
    if gold:
        return True, p, q
    else:
        return False, 0, 0
    
#----------------------------------------------------    
def exponencial(n0, e, p, d):
    '''(int, int, float, int) -> int 

       Recebe 

         * o número `n0` de indivíduos infectados em um dia 0;
         * o número diário médio `e` de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade `p` de uma exposição resultar em uma infecção;
         * um inteiro `d`,  d >=  0. 

      Retorna o número total de indivíduos infectados até o dia d 
      determinado por (n0, e, p).
    '''
    num_inf = n0
    
    num_inf = int(((1 + e * p)**d)*n0)
    
    return num_inf
    
#--------------------------------------------------
def logistica(n0, e, p, n, d):
    '''(int, int, float, int, int) -> int
 
       Recebe 

         * o número `n0` de indivíduos infectados em um dia 0;
         * o número diário médio `e` de indivíduos com quem alguém 
           infectado é exposto;
         * a probabilidade `p` de uma exposição resultar em uma infecção;
         * o número `n` de indivíduos na população; e
         * um inteiro `d`, d >= 0. 

       Retorna o número total de indivíduos infectados até o dia `d` 
       determinado por (n0, e, p, n).

    '''
    num = n0
    if d == 0:
        return n0
    dia = 1
    
    while dia <= d:
        num_inf = (1 + e * p * (1 - num/n))* num
        dia += 1
        num = num_inf
    
    num_inf = int(num_inf)
    return num_inf
    