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
#------------------------------------------------------------------
# MODULOS A SEREM UTILIZADOS NO PROGRAMA
import random # para random.choice(lista) na função gere_frase()

#------------------------------------------------------------------
# CONSTANTES

# ponto final, ponto de interrogação, ponto de exclamação
# não consideraremos reticências "..."
PONTUACAO_FINAL = ".?!"

# vírgula, ponto e vírgula, dois pontos, fecha parênteses
# não devem ser precedidos de espaço na frase gerada
PONTUACAO_SEM_ESPACO = ',;:)' + PONTUACAO_FINAL

# travesão, aspas, abre chaves
# devem ser precedidos de espaço na frase gerada
PONTUACAO_COM_ESPACO = '—"('

# todas juntas (reticências foram desconsideradas)
PONTUACAO = PONTUACAO_SEM_ESPACO + PONTUACAO_COM_ESPACO

# usado na função insira espacos
ESPACO = ' '

# semente para o gerador aleatório com o objetivo de reprodutibilidade
SEED = 1234

#------------------------------------------------------------------
#
def main():
    '''(None) -> None

    Para testar as funções juntas. Esta função não será avaliada, entretanto
    ela __não__ deve gerar erro de execução ou sintático. 
    Modifique-a se desejar.
    '''
    # Para efeitos de reprodutibilidade
    random.seed(SEED)

    print('ESCREVENDO "como" MACHADO DE ASSIS!\n')

    # 1 leia nome do arquivo 
    nome = input("Digite o nome do arquivo com o texto: ")

    # 2 leia o corpus
    try:
        with open(nome, "r", encoding="utf-8") as arq:
            texto = arq.read()
    except:
        print(f"main(): Erro na leitura do arquivo '{nome}'")
        return None
    
    # 3 insira espaços antes de pontuações
    texto = insira_espacos(texto)

    # 4 obtenha lista com itens léxicos
    lst_itens = texto.split()
    
    # 5 construa dicionario de sucessores
    dicio = dicio_sucessores(lst_itens)

    # 6 quantidade de frases que devem ser geradas
    n = int(input("Digite o numero de frases que devem ser geradas: "))

    # 7 gere as frase
    for i in range(n):
        # gere i-ésima frase
        print("---")

        # 7.1 pegue palavra inicial da frase a ser gerada
        palavra_inicial = input(f"Digite a palavra inicial da frase {i+1}: ")

        # 7.2 gere uma frase começando com palavra_inicial 
        frase = gere_frase(palavra_inicial, dicio)
        print("Frase gerada:", frase)

    print("\nFIM")

#------------------------------------------------------------------
def insira_espacos(txt):
    '''(str) -> str

    RECEBE uma string `txt`.
    RETORNA a string resultante da inserção de um ESPACO antes e depois de 
    __cada sinal__ em PONTUACAO que estiver em texto.
    
    '''
    ns = len(txt)
    
    lst = []
    
    for j in range(ns):
        lst += txt[j]
    
    n = len(lst)
    
    nova_str = ''
    
    for i in range (n):
        
        if lst[i] in PONTUACAO:
            nova_str += ESPACO + lst[i] + ESPACO
        
        else:
            nova_str += lst[i]
    
    return nova_str
    
    # modifique o código abaixo para conter a sua solução.
    # print("Vixe! Ainda não fiz a função insira_espacos()!")
    # return ""
    
#------------------------------------------------------------------
def dicio_sucessores(lst):
    '''(list) -> dict

    RECEBE uma lista `lst`.
    RETORNA um dicionário em que 

        - as __chaves__ são os itens que ocorrem em lst e 
        - o  __valor__ associado a cada chave é a lista dos 
          itens que ocorrem imediatamente após a chave na lista lst.

    Por convenção a lista correspondente ao valor do último item 
    na lst (=lst[-1]) contém o primeiro item da lista (=lst[0]).

    Se a `lst` é a lista vazia a função deve retornar o dicionário vazio.
    '''
    dicio = {}
    
    n = len(lst)
    
    if n == 0:
        return dicio

    for i in range (-1, n-1):
        
        if lst[i] in dicio:
            lista = dicio[lst[i]]
            lista += [lst[i+1]]
            dicio[lst[i]] = lista
            
        else:
            lista = [lst[i+1]]
            dicio[lst[i]] = lista
    
    return dicio
    
    # modifique o código abaixo para conter a sua solução.
    # print("Vixe! Ainda não fiz a função dicio_sucessores()!")
    # return {}

#------------------------------------------------------------------
def gere_frase(p_inicial, dicio):
    '''(str, dict) -> str

    RECEBE uma palavra `p_inicial` e um dicionário `dicio`.

    O dicionário foi criado a partir de um texto com uma ou 
    mais frase; como nos textos de Machado de Assis.

    Cada chave do dicionário é um item (str). O valor no dicionário 
    correspondente a uma chave é uma lista (list) de itens (str). 

    RETORNA uma string representando uma frase.

    A frase retornada deve começar com a string p_inicial e ser gerada 
    segundo o __processo aleatório__ descrito no enunciado.
    
    Os itens na frase devem ser precedidos de um ESPACO, exceto:

        - a palavra inicial e
        - e os sinais de pontuação na string PONTUACAO_SEM_ESPACO.

    Se p_inicial não está no dicionário a função deve retornar a string vazia.
    '''
    str_final = ''
    
    if p_inicial not in dicio:
        return str_final
    
    str_final += p_inicial
    
    palavra = p_inicial
    
    while palavra not in PONTUACAO_FINAL:
        lista = dicio[palavra]
        palavra = random.choice(lista)
        
        if palavra in PONTUACAO_SEM_ESPACO:
            str_final += palavra
            
        else:
            str_final += ESPACO + palavra
    
    return str_final
    
    # modifique o código abaixo para conter a sua solução.
    # print("Vixe! Ainda não fiz a função gere_frase()!")
    # return ""

#######################################################
###                 FIM                             ###
#######################################################
#
# Não modifique as linhas abaixo
#
# Esse if serve para rodar a main() dentro do Spyder
# e não atrapalhar o corretor automático
# COMENTE as linhas a seguir durante os testes das suas
# funções no Python Shell

if __name__ == '__main__':
    main()
