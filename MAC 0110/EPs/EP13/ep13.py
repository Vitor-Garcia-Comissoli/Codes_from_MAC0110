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

# módulo ep12: ep12.gera_gaps(), ep12.pontuacao()
import ep12

# Constantes
# use essas constantes caso desejar
DNA = 'ATCG'
GAP = '_'

#------------------------------------------------------------------
def main():
    '''
        Modifique essa função, escrevendo os seus testes.
    '''

    ## exemplos de chamada da função do módulo ep12
    print('Testes das funções do módulo ep12:')
    print(ep12.gera_gaps('T'))
    print(ep12.gera_gaps( 'CA' ))
    print(ep12.gera_gaps( 'AT_G' ))

    print(ep12.pontuacao(5, 5, 3, 'T_CGTAC', 'ATCG___'))
    print(ep12.pontuacao(1, 5, 3, 'T_CGTAC', 'ATCG___'))
    print(ep12.pontuacao(5, 5, 3,  'T_CGTA',  'ATCG__'))
    print()

    ## Escreva aqui os testes para a função gera_n_gaps()
    #
    
    print(gera_n_gaps( 'T', 2 ))
    print(gera_n_gaps( 'CA', 2 ))
    print(gera_n_gaps( 'C_A', 2))
    
    ## Escreva aqui os testes para a função pontuacao_max()
    #
    print()
    print(pontuacao_max(5, 5, 3, 'T_CG', 'ATCG'))
    print(pontuacao_max(1, 5, 3, 'T_CGTAC', 'ATCG___', 2))
    print(pontuacao_max(5, 1, 0, 'AT_', 'A_T', 2))
    
    print("Fim dos meus testes.")

#------------------------------------------------------------------
#
def gera_n_gaps( dna, n = 1 ):
    '''( str, int ) -> list

    RECEBE uma string `dna` representando uma fita de DNA com os
    símbolos 'A', 'T', 'C', 'G' e '_' (gap), e um número inteiro positivo `n`.
 
    RETORNA uma lista sem repetições com todas as variações de `dna` 
    com até `n` gaps extras.


    EXEMPLOS:
 
    In [1]: gera_n_gaps( 'T', 2 )
    Out[1]: ['T', '_T', 'T_', '__T', '_T_', 'T__']
    
    In [2]: gera_n_gaps( 'CA', 2 )
    Out[2]: ['CA', '_CA', 'C_A', 'CA_', '__CA', '_C_A', '_CA_', 'C__A', 'C_A_', 'CA__']
    
    In [3]: gera_n_gaps( 'C_A', 2)
    Out[3]: ['C_A', '_C_A', 'C__A', 'C_A_', '__C_A', '_C__A', '_C_A_', 'C___A', 'C__A_', 'C_A__']
    '''
    # modifique o código abaixo para conter a sua solução.
    
    aminoacidos = [dna]
    
    lst_gaps = []
    
    combinacoes = [dna]
    combinacoes += ep12.gera_gaps(dna)
    
    for i in range (1, n):
        lst_gaps = []
        for g in range(len(aminoacidos)):
            lst_gaps += ep12.gera_gaps(aminoacidos[g])
            aminoacidos += lst_gaps
            for j in range (len(lst_gaps)):
                h = ep12.gera_gaps(lst_gaps[j])
                for z in range(len(h)):
                    if h[z] not in combinacoes:
                        combinacoes += [h[z]]
    
    return combinacoes
    
    
    '''
    aminoacidos = dna
    
    combinacoes = [dna]
    combinacoes += ep12.gera_gaps(dna)
    
    lst_aminoacidos = []
    lst = []
    a = 0
    lst_gaps = []
    
    x = (len(lst_aminoacidos)+1)
    
    for j in range(len(aminoacidos)):
        lst_aminoacidos += aminoacidos[j]
        
    lst_gaps += [lst_aminoacidos]
    
    for i in range (0, n-1):
        x = (len(lst_aminoacidos)+(i+1))
        lst_str = []
        
        for k in range (0, x, 1):
            lst = x * ['0']
            lst[k] = GAP
            w = 0
            y = 0
            while w < x:
                if lst[w] == '0':
                    lst[w] = lst_gaps[a][y]
                    w += 1
                    y += 1
                else:
                    w += 1
            
            string = ''
            for z in range(x):
                string += lst[z]
            
            if string not in lst_str: 
                lst_str += [string]
        
            if lst not in lst_gaps: 
                lst_gaps += [lst]
        
        a += 1
            
        for q in range (len(lst_str)):
            b = ep12.gera_gaps(lst_str[q])
            for z in range(len(b)):
                if b[z] not in combinacoes:
                    combinacoes += [b[z]]
    
    return combinacoes
    '''
    
    """
    print("Vixe! Ainda não fiz a função gera_n_gaps()...")
    return []
    """
#------------------------------------------------------------------
#
def pontuacao_max(m, d, g, s, t, n = 1):
    '''(int, int, int, str, str, int) -> int, list de list

    RECEBE:

        - três números inteiros não negativos `m`, `d`, e `g` como no EP12;
        - duas strings `s` e `t` de mesmo comprimento representando fitas de DNA 
          com os símbolos 'A', 'T', 'C', 'G' e '_' (gap); e
        - um número inteiro positivo `n`.

    RETORNA 

        - a maior pontuação entre pares de variações de s e t que têm:

              * o mesmo comprimento; 
              * até `n` gaps extras.

        - uma lista com todos os pares de variações de s e t que têm 
          esta maior pontuação; cada par é uma lista com duas variações.

    Exemplos:

    In [1]: pontuacao_max(5, 5, 3, 'T_CG', 'ATCG')
    Out[1]: (9, [['_T_CG', 'AT_CG']])

    In [2]: pontuacao_max(1, 5, 3, 'T_CGTAC', 'ATCG___', 2)
    Out[2]: (-12, [['_T_CGTAC', 'AT_CG___']])
   
    In [3]: pontuacao_max(5, 1, 0, 'AT_', 'A_T', 2)
    Out[3]: ((10,
              [['A_T_', 'A_T_'],
               ['_A_T_', '_A_T_'],
               ['A__T_', 'A__T_'],
               ['A_T__', 'A_T__']])
    '''
    # modifique o código abaixo para conter a sua solução.
    
    """
    iguais = m
    diferentes = d
    gaps = g
    """
    ate_n_gaps = n
    
    lst1 = s
    lst2 = t
    
    resultado = 0
    maior_resultado = 0
    
    lst_resultado = []
    
    lst_lst1 = gera_n_gaps(lst1, ate_n_gaps)
    lst_lst2 = gera_n_gaps(lst2, ate_n_gaps)
    
    for i in range (0, len(lst_lst1)):
        lst_1 = lst_lst1[i]
        for j in range(0, len(lst_lst2)):
            lst_2 = lst_lst2[j]
            
            if len(lst_1) == len(lst_2):
        
                resultado = ep12.pontuacao(m,d,g,lst_1,lst_2)
                
                if i == 0:
                    maior_resultado = resultado
                    lst_resultado = []
                    lst = []
                    lst += [lst_1]
                    lst += [lst_2]
                    lst_resultado = [lst]
        
                elif maior_resultado < resultado:
                    maior_resultado = resultado
                    lst_resultado = []
                    lst = []
                    lst += [lst_1]
                    lst += [lst_2]
                    lst_resultado = [lst]
                    
                elif maior_resultado == resultado:
                    lst = []
                    lst += [lst_1]
                    lst += [lst_2]
                    lst_resultado += [lst]
    
    return maior_resultado, lst_resultado
    
    """
    print("Vixe! Ainda não fiz a função pontuacao_max()...")
    return 0, []
    """

#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.

if __name__ == '__main__':
    main()
