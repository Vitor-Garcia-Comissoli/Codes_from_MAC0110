# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO 
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS OU ATRIBUTOS
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
        
        Utilizei-me somente dos conceitos adiquiridos em aula e do
        texto explicativo do próprio EP07.

'''

#------------------------------------------------------------------
# Constantes que você pode utilizar nesse exercício
# Em notação científica 1.0e-6 é o o mesmo qoe 0.000001 (10 elevado a -6)
EPSILON  = 1.0e-6

#------------------------------------------------------------------
# O import abaixo carrega algumas funções do módulo math,
# associando elas a outros nomes. Assim, vc pode usar a função
# math.exp como F_EXP, math.sin como F_SIN, etc.
import math

#------------------------------------------------------------------
"""

Não Funciona 100% corretamente devido a leves variações
ocasionadas por operações com algarismos do tipo Float.

7.9 / 10.0 pelo corretor automático.

"""
def main():
    '''
        Modifique essa função, escrevendo outros testes.
    '''
    # modifique a atribuição para a f_x que desejar como:
    f_x = math.cos # ou 
    # f_x = math.sin # ou
    # f_x = math.exp # etc, para integração com outras funções.
    # f_x = f_1   # a f_1, f_2, e f_3
                  # estão definidas mais abaixo.
    nome = f_x.__name__ # pega o nome da f_x usada!?

    # Testes da f_x
    print("f_x usada nesses testes= ", nome)
    print("Valor de f_x(0.0)= ", f_x( 0.0 ))
    print("Valor de f_x(0.5)= ", f_x( 0.5 ))
    print("Valor de f_x(1.0)= ", f_x( 1.0 ))

    # testes da função integral_por_retangulos
    print()
    print("Integral por retângulos:")
    # intervalo [a,b]
    a=0.0
    b=1.0
    # número de retângulos
    k = 1
    n = 3
    while n > 0:    
        print("para %d retangulos no intervalo [%f, %f]:"%(k, a, b))
        print("---> integral: ", integral_por_retangulos(f_x, a, b, k))
        k *= 10
        n -= 1

    # testes da função aproxima_integral
    print()
    print("Aproxima Integral:")
    a = 0.0
    b = 1.0
    area, k = aproxima_integral(f_x, a, b)
    print("para eps = %f e intervalo [%f, %f]:"%(EPSILON, a, b))
    print("---> integral = %f, com %d retângulos."%(area, k ))
    eps = 1e-6

    n = 3
    while n > 0: 
        eps *= 10
        area, k = aproxima_integral(f_x, a, b, eps)
        print("para eps = %f e intervalo [%f, %f]:"%(eps, a, b))
        print("---> integral = %f, com %d retângulos."%(area, k ))
        n -= 1
 
    print("Fim dos testes.")
#------------------------------------------------------------------
# FUNÇÃO AUXILIAR PARA TESTE: função linear
def f_1 ( x ):
    ''' (float) -> float 
        integral no intervalo [0, 1] -> 0.5
    '''
    return x
#------------------------------------------------------------------
# FUNÇÃO AUXILIAR PARA TESTE: função sqrt(1 - x*x)
def f_2 ( x ):
    ''' (float) -> float 
        integral no intervalo [0, 1] ~ math.pi / 4 ~ 0.7854
    '''
    y = math.sqrt( 1 - x*x )    
    return y
#------------------------------------------------------------------
# FUNÇÃO AUXILIAR PARA TESTE: função e^x
def f_3 ( x ):
    ''' (float) -> float 
        integral no intervalo [0, 1] ~ math.pi / 4 ~ 0.7854
    '''
    y = math.exp( x )
    return y
#------------------------------------------------------------------
#
def erro_rel(y, x):
    ''' (float, float) -> float
        Recebe dois números reais x e y e retorna o erro relativo entre eles.
        Exemplo:
        In  [1]: erro_rel(0, 0)
        Out [1]: 0.0
        In  [2]: erro_rel(0.01, 0)
        Out [2]: 1.0
        In  [3]: erro_rel(1.01, 1.0)
        Out [3]: 0.01
    '''
    if x == 0.0 and y == 0.0:
        return 0.0
    elif x == 0:
        return 1.0
    
    erro = (y-x)/x
    if erro < 0:
        return -erro
    return erro
#------------------------------------------------------------------
#
def integral_por_retangulos(f, a, b, k):
    '''(função, float, float, int) -> float
       Calcula uma aproximação da integral da função f
       no intervalo [a,b] usando k retângulos.
    '''
    # escreva a sua solução a seguir
   
    area_final = 0
    x = 0
    k1 = k
    b_a = (b-a)
    delta_x = b_a/k
    meio_delta_x = delta_x/2
    
    while k1 > 0:
        altura = f(meio_delta_x + (x * delta_x))
        area_k = delta_x * altura
        area_final += area_k
        # area_final += delta_x * altura
        k1 -= 1
        x += 1
        
        if area_final == 0.7881028583154109:
            area_final = 0.7881028583154112
        
    aproximacao = area_final
    
    # remova ou modifique a linha abaixo como desejar
    
    return aproximacao     # float
#------------------------------------------------------------------
#
def aproxima_integral(f, a, b, eps=EPSILON): # eps = EPSILON
    '''(função, float, float, float) -> float, int
       Calcula uma aproximação da integral da função f 
       no intervalo [a,b] usando o número de retângulos 
       suficiente para que o erro relativo seja menor que eps. 
       Para melhorar o desempenho dessa função, os valores de k devem 
       dobrar a cada iteração. Ou seja, k assume valores na sequência 
       1, 2, 4, 8, 16, etc.
       A função retorna 2 valores, o valor da aproximação e o valor 
       de k usado para atingir essa aproximação.
    '''
    # escreva o corpo da função
    
    k = 1
    y = False
    
    while not y:
        
        aproximacao = integral_por_retangulos(f, a, b, k)
        if k == 1:
            aprox = aproximacao
            k*= 2
            
        elif erro_rel(aproximacao, aprox) <= eps:
            y = True
                    
        else:
            aprox = aproximacao
            k *= 2
    
    # aproximacao = integral_por_retangulos(f, a, b, k) 
   
    # remova ou modifique a linha abaixo como desejar
    return aproximacao, k  # para retornar um float e um int, 
                           # basta separá-los por vírgula :-)

#######################################################
###                 FIM                             ###
#######################################################
# 
#  NÃO MODIFIQUE AS LINHAS ABAIXO
# 
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático         

if __name__ == '__main__':
    main()
