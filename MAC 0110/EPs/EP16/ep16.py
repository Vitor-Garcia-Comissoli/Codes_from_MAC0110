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

'''

import ep15
# contém as seguintes funções do módulo ep15:
#    ep15.crie(),
#    ep15.clone(),
#    ep15.subtraia(),
#    ep15.to_string() e
#    ep15.limiarize()


#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''
    # coloque aqui os seus testes
    
    # return

#------------------------------------------------------------------
#
def erosao ( img, viz = 3 ):
    ''' (matriz, int) -> None

    RECEBE uma matriz `img` representando uma imagem em níveis de cinza e
    um inteiro `viz`.

    MODIFICA `img` de tal forma que, ao final, cada pixel 
    [lin][col] seja o valor mínimo da vizinhança de tamanho `viz`
    centrada no pixel [lin][col] da imagem original.

    Pré-condição: a função supõe que `viz` é um número ímpar 
    positivo.
    '''
    nlin = len(img)
    ncol = len(img[0])
    
    viz_lat = int((viz - 1) / 2)
    
    matriz = nlin * [(ncol * [0])]
    
    for i in range(nlin):
              
        lst = []
        
        for j in range (ncol):
            
            if i > 0 and i < nlin - 1:
                for z in range (i - viz_lat, i + viz_lat):
                    
                    if j > 0 and i < ncol - 1:
                        for w in range (j - viz_lat, j + viz_lat):
                            lst += [img[z][w]]
                            
                    elif j == 0:
                        for w in range (j, j + viz_lat):
                            lst += [img[z][w]]
                        
                    elif j == ncol - 1:
                        for w in range (j - viz_lat, j):
                            lst += [img[z][w]]
            
            elif i == 0:
                for z in range (i, i + viz_lat):
                    
                    if j > 0 and i < ncol - 1:
                        for w in range (j - viz_lat, j + viz_lat):
                            lst += [img[z][w]]
                    
                    elif j == 0:
                        for w in range (j, j + viz_lat):
                            lst += [img[z][w]]
                        
                    elif j == ncol - 1:
                        for w in range (j - viz_lat, j):
                            lst += [img[z][w]]
            
            elif i == nlin - 1:
                 for z in range (i - viz_lat, i):
                     
                    if j > 0 and i < ncol - 1:
                        for w in range (j - viz_lat, j + viz_lat):
                            lst += [img[z][w]]
                        
                    elif j == 0:
                        for w in range (j, j + viz_lat):
                            lst += [img[z][w]]
                        
                    elif j == ncol - 1:
                        for w in range (j - viz_lat, j):
                            lst += [img[z][w]]
        
        matriz[i][z] = min(lst)
    
    for x in range(nlin):
        for y in range(ncol):
            img[x][y] = matriz[x][y]
    
    return None

    '''
    Náo consegui chegar em um resultado satisfatório com a função erosão(img, viz=3)
    
                                Nota final 5/10
    '''
    # print("Vixe! Ainda não fiz a função erosao()...")

#------------------------------------------------------------------
#
def segmentacao_SME( img, viz = 3 ):
    ''' (matriz, int) -> matriz

    RECEBE uma matriz `img`. 
    APLICA o filtro de erosão com vizinhança viz.
    RETORNA a imagem resultado da subtração entre `img` e sua erosão. 
    Veja exemplos no enunciado.
    '''
    
    m_erosao = ep15.clone(img)
    
    erosao(m_erosao, viz)
    
    matriz = ep15.subtraia(img, m_erosao)
    
    return matriz
    
    # print("Vixe! Ainda não fiz a função segmentacao_SME()...")
    # return [[0]]


#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
