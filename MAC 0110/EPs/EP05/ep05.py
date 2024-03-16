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
        
        Para a realização desde EP utilizei-me somente das propriedades aprendidas em sala
        de aula, consultando a internet somente para reforçar o conceito de Trios Pitagoreanos.

"""

# Escreva seu programa aqui

def Main():
    
    n = int(input("Digite o valor de n: "))
    
    if n % 12 == 0:
        a = 3
        b = 4
        c = 5
    #else:
        #a = n+1
        #b = n+1
        #c = n+1
    
    elif n % 30 == 0:
        a = 5
        b = 12
        c = 13
    elif n % 56 == 0:
        a = 7
        b = 24
        c = 25
    elif n % 40 == 0:
        a = 8
        b = 15
        c = 17
    elif n % 90 == 0:
        a = 9
        b = 40
        c = 41
    elif n % 132 == 0:
        a = 11
        b = 60
        c = 61
    elif n % 84 == 0:
        a = 12
        b = 35
        c = 37
    elif n % 182 == 0:
        a = 13
        b = 84
        c = 85
    elif n % 144 == 0:
        a = 16
        b = 63
        c = 65
    elif n % 70 == 0:
        a = 20
        b = 21
        c = 29
    elif n % 126 == 0:
        a = 28
        b = 45
        c = 53
    elif n % 154 == 0:
        a = 33
        b = 56
        c = 65
    elif n % 198 == 0:
        a = 36
        b = 77
        c = 85
    elif n % 208 == 0:
        a = 39
        b = 80
        c = 89
    elif n % 176 == 0:
        a = 48
        b = 55
        c = 73
    elif n % 234 == 0:
        a = 65
        b = 72
        c = 97
    else:
        a = n+1
        b = n+1
        c = n+1
    
    a1 = a
    b1 = b
    c1 = c
    
    pit = False
    cont = 2
    
    #if n == a + b + c:
        #pit = Pitagórico(a,b,c)
    
    while n >= a1 + b1 + c1 and not pit:
    
        if a1**2 + b1**2 == c1**2 and a1 + b1 + c1 == n and a1 < b1 < c1:
            pit = True
        
        else:
            a1 = a * cont
            b1 = b * cont
            c1 = c * cont
            cont += 1
 
    
    if pit:
        print("%d é soma do trio (%d, %d, %d)" % (n, a1, b1, c1))
    else:
        print("%d não é soma de trio Pitagoreano" % (n)) 

          
def Pitagórico(a,b,c):
    if a**2 + b**2 == c**2 and a < b < c:
        return True
    else:
        return False

Main()