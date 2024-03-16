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
        
        Para a realização deste EP utilizei-me dos conhecimentos adiquiridos em sala de aula, em conjunto
        com uma breve pesquisa no google com o intuito de relembrar a fórmula utilizada para a definição de
        áreas circulares em um plano cartesiano, sendo tal fórmula: (x-x0)^2 + (y-y0)^2 = r^2
        
"""

##################################################################

# leitura da coordenada em x, y
x = float(input("Digite x: "))
y = float(input("Digite y: "))

## ESCREVA O RESTO DO SEU PROGRAMA ABAIXO USANDO x, y

fora = True

raio_maior = 1.0
raio_menor = 0.5

x0 = 0
y0 = 2

if -3.0 <= x <= 3.0 and 0 <= y <= 4.0:                            # Retânglo Geral
    fora = False
    
    if 1.5 <= x <= 2.5 and 1.5 <= y <= 2.5:
        fora = True                                               # Cubo dentro de outro Cubo
        if 1.75 <= x <= 2.25 and 1.75 <= y <= 2.25:
            fora = False
            
    if 2.0 < x <= 3 and 0 <= y < 1.0:
        fora = True                                               # Tirando cantos do Retângulo Geral
    elif 2.0 < x <= 3 and 3.0 < y <= 4.0:
        fora = True

    if -2.5 <= x <= -1.5 and 0.5 <= y <= 1.5:
        fora = True                                               # 2 Quadrados um em cima do outro
    elif -2.5 <= x <= -1.5 and 2.5 <= y <= 3.5:
        fora = True

    if ((x - x0)**2 + (y-y0)**2) < raio_maior**2:
        fora = True                                               # Áreas Circulares
        if ((x - x0)**2 + (y-y0)**2) < raio_menor**2:
            fora = False

if fora:
    print("False")
else:
    print("True")



