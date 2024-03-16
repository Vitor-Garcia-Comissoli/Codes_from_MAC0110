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

# CONSTANTES
ESPACO = ' '
BRANCO = ' \n\t\v\r\f'

#------------------------------------------------------------------
def main():
    '''
    Modifique essa função, escrevendo outros testes.
    '''
# 1. leia o limite de caracteres por linha    
    k = int(input("Digite o no. de colunas por linha (> 0): "))

# 2. leia o texto de um arquivo
# 2.1 leia o nome do arquivo
    nome = input("Digite o nome do arquivo: ")
# 2.2 "abra" o arquivo
    arquivo = open(nome, 'r', encoding='utf-8')
# 2.3 leia o conteudo do arquivo e chame de txt 
    txt = arquivo.read()
# 2.4 feche o arquivo
    arquivo.close()

# 3. faça uma reguinha
# reguinha = s[:k]
    reguinha = " " + ((k//5 + 1) * '....*')[:k] # reguinha

# 4. exiba o texto original    
    print("Texto original: ")
    print(reguinha)
    print(txt + '\n') # '\n' para mudar de linha

# 5. ajuste o limite da coluna
# de txt para uma lista de strings k-ajustadas à esquerda
    print(f"Texto com linhas {k}-ajustadas à esquerda: ")
    lst_str_esq = ajuste_esquerda(txt, k)
    print(reguinha)
    for linha in lst_str_esq:
        print('|'+linha+'|')
    print()

# 6. ajuste o limite da coluna
# de lista de strings k-ajustadas à esquerda para k-ajustadas completas
    print(f"Texto linhas {k}-ajustadas completamente: ")    
    lst_str_comp = ajuste_completo(lst_str_esq, k)
    print(reguinha)
    for linha in lst_str_comp:
        print("|"+linha+"|")
        
#--------------------------------------------------------
def ajuste_esquerda(txt, k):
    '''(str, int) -> list de str

    RECEBE  uma string `txt` e um inteiro `k`.
    RETORNA uma lista de strings k-ajustadas à esquerda que representa `txt`.
    '''
    texto = txt.strip()
    lst_txt = texto.split()
    print(lst_txt)
    
    linhas_ajt = []
    linha = ''
    i = 0
    cont = 0
    x = len(lst_txt)
    
    while i < x:
        tamanho = len(lst_txt[i])
        if i == x-1:
            if cont + tamanho + 1 <= k:
                linha += (ESPACO + lst_txt[i])
                linha = linha.strip()
                linhas_ajt += [linha]
                cont += tamanho + 1
                i += 1
            else:
                linha = linha.strip()
                linhas_ajt += [linha]
                linha = ''
                linha += lst_txt[i]
                linha = linha.strip()
                linhas_ajt += [linha]
                i += 1
        elif linha == '':
            linha += lst_txt[i]
            cont += tamanho
            i += 1
        elif cont + tamanho + 1 <= k:
            linha += (ESPACO + lst_txt[i])
            cont += tamanho + 1
            i += 1
        else:
            linha = linha.strip()
            linhas_ajt += [linha]
            cont = 0
            linha = ''
    
    # print(linhas_ajt)
    if linhas_ajt[0] == '' and linhas_ajt[1] != '':
        linhas_ajt = [linhas_ajt[1]]   
    # print(linhas_ajt)
    
    return linhas_ajt
    
    # print("Vixe! Ainda não fiz a função ajuste_esquerda()!")

#--------------------------------------------------------
def ajuste_completo(lst_str, k):
    '''(list de str, int) -> list de str

    RECEBE  uma lista de strings `lst_str` e um inteiro `k` tais que cada string na 
       lista é `k`-ajustada à esquerda.
    CRIA e RETORNA uma lista com as strings em `lst_str` k-ajustadas completamente.
    '''
    # print(lst_str)
    
    i = 0
    x = len(lst_str)
    # print(lst_str)
    lst_comp = x * ['']
    
    while i < x:
        string = lst_str[i]
        
        if len(string) >= k:
            lst_comp[i] = string
            i += 1
            
        elif len(string) < k:
            sobra = k - len(string)
            palavras = string.split()
            for y in range (0, len(palavras) - 1, 1):
                str_palavra = palavras[y]
                palavras[y] = str_palavra + ESPACO
            
            # print(sobra)
            
            add_espacos = ''
            j = 0
            if len(palavras) != 1:
                while j < len(palavras) and sobra > 0:
                    add_espacos = (palavras[j] + ESPACO)
                    sobra -= 1
                    palavras[j] = add_espacos
                    j += 1
                    if j == len(palavras) - 1:
                        j = 0
                        
            elif len(palavras) == 1:
                add_espacos = (palavras[j] + (sobra * ESPACO))
                palavras[j] = add_espacos
                
            z = len(palavras)
            linha = ''
            for w in range (0, z, 1):
                linha += palavras[w]
            
            lst_comp[i] = linha
            i += 1
            
    return lst_comp
    
    # print("Vixe! Ainda não fiz a função ajuste_completo()!")
    
    
#######################################################
###                 FIM                             ###
#######################################################
# 
# Esse if serve para rodar a main() dentro do Spyder.
if __name__ == '__main__':
    main()
