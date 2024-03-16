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
        
        Para a realização desta EP utilizei-me somente de conhecimentos
        adiquiridos no próprio curso, sem a ajuda de terceiros.

'''
# escreva seu programa a seguir

s = input('Digite uma string s: ')
i = input('Digite um inteiro i: ')
i = int(i)

f = input('Digite um float f: ')
f = float(f)

ss = s + s
ii = i + i
ff = f + f
ixs = i * s
ixi = i * i
ixf = i * f
fi = f / i
i2i = (2 * i) / i
ii2 = (i / i) * 2

print('')
print('s+s = ',ss)
print('i+i = ',ii)
print('f+f = ',ff)
print('i*s = ',ixs)
print('i*i = ',ixi)
print('i*f = ',ixf)
print('f/i = ',fi)
print('2*i/i = ',i2i)
print('i/i*2 = ',ii2)
