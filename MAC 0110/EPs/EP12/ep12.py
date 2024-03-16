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
# Constantes
# use essas constantes caso desejar
DNA = 'ATCG'
GAP = '_'


#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''
    print("main(): início dos teste")
    ## Escreva aqui os testes para a função gera_gaps
    # 
    
    DNA = input('Digite uma sequência de DNA: ')
    dna = DNA.strip()
    lst = gera_gaps(dna)
    
    print('')
    print('As combinações possíveis são: ',lst)
    
    ## Escreva aqui os testes para a função pontuação
    #
    
    lst1 = input('Digite a 1a sequência de DNA: ')
    lst2 = input('Digite a 2a sequência de DNA: ')
    
    iguais = int(input('Digite o valor de M: '))
    diferentes = int(input('Digite o valor de D: '))
    gaps = int(input('Digite o valor de G: '))
    
    resultado = pontuacao(iguais, diferentes, gaps, lst1, lst2)
    
    print('')
    print('O valor do resultado é de', resultado)
    print('')
    
    print("main(): fim dos testes")


#------------------------------------------------------------------
#
def gera_gaps( dna ):
    ''' ( str ) -> list

    RECEBE uma string `dna` representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (GAP).

    RETORNA uma lista com todas as variações de dna com um símbolo GAP 
    a mais e sem repetições.

    exemplos: 
    In  [1]: gera_gaps( 'T' )
    Out [1]: ['_T', 'T_']
    
    In  [2]: gera_gaps( 'CA' )
    Out [2]: ['_CA', 'C_A', 'CA_']
    
    In  [3]: gera_gaps( 'AT_G')
    Out [3]: ['_AT_G', 'A_T_G', 'AT__G', 'AT_G_'] 
    '''
    # modifique o código abaixo para conter a sua solução.
    
    aminoacidos = []
    
    for i in range(len(dna)):
        a = dna[i]
        aminoacidos += [a]
    
    x = len(dna) + 1
    
    lst_dna = []
    
    for i in range(0, x, 1):
        lst = x * [0]
        lst[i] = GAP
        w = 0
        j = 0
        while w < x:
            if lst[w] == 0:
                lst[w] = aminoacidos[j]
                w += 1
                j += 1
            else:
                w += 1
        
        string = ''
        for y in range(x):
            string += lst[y]
        
        if string not in lst_dna:
            lst_dna += [string]
    
    return lst_dna

    '''
    print("Vixe!! ainda não fiz a função gera_gaps()...")
    return []
    '''
#------------------------------------------------------------------
#
def pontuacao(m, d, g, s, t):
    ''' (int, int, int str, str) -> int

    RECEBE 3 inteiros não negativos `m`, `d`, e `g` e duas strings `s` e `t` 
    de mesmo tamanho com zero ou mais gaps representando fitas de DNA.
 
    RETORNA a pontuação do alinhamento entre `s` e `t` calculada da seguinte 
    forma:
 
       * duas letras iguais alinhadas contam `m` pontos, 
       * duas letras diferentes alinhadas contam `-d` pontos (subtrai d pontos) e 
       * uma letra alinhada com um gap ou dois gaps alinhados contam `-g` pontos.

    Exemplos:

    In  [1]: pontuacao(5, 5, 3, 'T_CGTAC', 'ATCG___')
    Out [1]: -7 
    
    In  [2]: pontuacao(1, 5, 3, 'T_CGTAC', 'ATCG___')
    Out [2]: -15
    
    In  [3]: pontuacao(5, 5, 3, 'T_CGTA', 'ATCG__')
    Out [3]: -4
    '''
    # modifique o código abaixo para conter a sua solução.
    
    iguais = m
    diferentes = d
    gaps = g
    
    lst1 = s
    lst2 = t
    
    resultado = 0
    
    x = len(lst1)
    
    for i in range(x):
        if lst1[i] == lst2[i] and lst1[i] != GAP and lst2[i] != GAP:
            resultado += iguais
        elif lst1[i] == lst2[i] and lst1[i] == GAP and lst2[i] == GAP:
            resultado -= gaps
        elif lst1[i] != lst2[i]:
            if lst1[i] == GAP or lst2[i] == GAP:
                resultado -= gaps
            elif lst1[i] != GAP and lst2[i] != GAP:
                resultado -= diferentes
    
    return resultado
    
    '''
    print("Vixe!! ainda não fiz a função pontuacao()...")
    return 0
    '''

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
