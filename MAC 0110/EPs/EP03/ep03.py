# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
# NÃO APAGUE OS DOCSTRINGS
#------------------------------------------------------------------
     
'''
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
        
        Para a realização deste EP, utilizei-me somente das ferramentas
        fornecidas em sala de aula.
'''

# escreva seu programa a seguir

n = int(input('Digite n: ' ))

# dv1 -->  1 x d1 + 2 x d2 ... + n x dn, dv1 = somadv1 % 11
# dv2 -->  0 x d1 + 1 x d2 ... + (n-1) x dn + n x dv1, dv2 = somadv2 % 11
somadv1 = 0

n1 = n
n2 = n
cont = 0
while n1 > 0:
    n1 = n1 // 10
    cont = cont + 1

freq = cont       # número de algarismos em n

while n2 > 0 :
    somadv1 = somadv1 + (freq * (n2 % 10))
    n2 = n2 // 10
    freq = freq - 1
    
dv1 = somadv1 % 11
if dv1 == 10:
    dv1 = 0
    
somadv2 = cont * dv1
cont = cont - 1

while n > 0:
    somadv2 = somadv2 + (cont * (n % 10))
    n = n // 10
    cont = cont -1
    
dv2 = somadv2 % 11
if dv2 == 10:
    dv2 = 0
    
print('DV=', dv1, dv2)