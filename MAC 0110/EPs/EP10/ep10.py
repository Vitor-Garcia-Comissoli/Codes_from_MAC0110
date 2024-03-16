# -*- coding: utf-8 -*-
#------------------------------------------------------------------
# LEIA E PREENCHA O CABEÇALHO
# NÃO ALTERE OS NOMES DAS FUNÇÕES, MÉTODOS E ATRIBUTOS
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

        Utilizei-me somente do que foi disponibilizado no guia do EP, além
        dos conhecimentos adiquiridos durante as aulas.
        
'''
#####################################################################
# MÓDULOS A SEREM UTILIZADOS NO PROGRAMA
import random

#####################################################################
# CONSTANTES

# enquanto estiver testando o seu programa deixe True
TESTANDO = True

# nunca se sabe ...
SOCORRO  =  False

# indica o volume do som, 512 parece ok.
# qualquer coisa, ajuste o volume do seu computador
VOLUME = 512 # 256

#-------------------------------------------------------------------------
# NOSSO ALBUM DE MÚSICAS, mais ou menos
# MUSICA, o mais perto que consegui, faltam notas musicais...,
# Hmm, vocês podem expandir..., mas não entregue a versão expandida.
STAR_WAY_TO_HEAVEN = [
    'C', 'E', 'A', 'B', 'E', 'C',
    'B', 'C+', 'F', 'C', 'C+', 'F#', 'D',
    'A', 'F', 'E', 'C', 'A', 'C', 'E', 'C', 'A'
]

FRERE_JACQUES = [
    'C', 'D', 'E', 'C',
    'C', 'D', 'E', 'C',
    'E',  'F', 'G',
    'E',  'F', 'G',
    'G',  'A', 'G', 'F', 'E', 'C',
    'G',  'A', 'G', 'F', 'E', 'C',
    'C',  'G', 'C',  # hmm, esse sol devia ser uma oitava abaixo, fui mal...
    'C',  'G', 'C' 
]

AQUARELA = [
    'G',   'G', 'C+', 'C+', 'B', 'A', 'G', 'G',
    'C+', 'C+', 'B',   'A', 'G', 'G', 'A', 'A',
    'G',   'G', 'C+', 'C+', 'B', 'A', 'G', 'G',
    'C+', 'C+', 'B',   'A', 'G', 'G', 'A', 'G', 'F'
]    

# ---------------------------------------------------------------
# ESCALA MAIOR
# Tabela mostrando a correspondência entre teclas do computador, notas musicais e frequencias:
# a TECLA[i] corresponde a nota musical NOTA[i] que tem frequencia (aprx) FREQUENCIA[i]
# Hmm, vocês podem expandir as notas,..., mas não entregue a versão expandida.
if TESTANDO:
    # 44100 é a taxa de amostragem "padrão" de som digital
    TAXA_DE_AMOSTRAGEM = 12
    #     
    NO_AMOSTRAS = 10 
    # não tem nada a ver com som, apenas para testes numéricos
    TECLAS      = [  'a',  'w',  's']
    NOTAS       = [  'C', 'C#',  'D']
    FREQUENCIAS = [    2,    2,    2]
else:
    # 44100 é a taxa de amostragem "padrão" de som digital
    TAXA_DE_AMOSTRAGEM = 44100

    # Hmm, esse 20000 é chutado...
    # Quanto maior, mais 'longo' é o som, quanto menor, mais 'curto'
    # Hmm, quanto maior, maiores são as listas e mais tempo para carregar no browser
    NO_AMOSTRAS = 20000 # 30000 
    # para executar server.py e sintetizar som, TESTANDO deve ser False
    # notas musicais, C+ é invensão para C "um oitava acima"
    #            dó   dó#   ré    ré#    mi    fá    fá#   sol  sol#    lá   lá#    si    dó  (uma oitava acima)
    NOTAS  = [  'C', 'C#',  'D', 'D#',  'E',  'F',  'F#',  'G', 'G#',  'A', 'A#',  'B',  'C+']
    #            dó   dó#   ré    ré#    mi    fá   fá#   sol  sol#   lá    lá#    si    dó  (uma oitava acima)
    TECLAS = [  'a',  'w',  's',  'e',  'd',  'f',  't',  'g',  'y',  'h',  'u',  'j',   'k']
    # frequencias
    FREQUENCIAS = [
        523.25,  # dó, 
        554.36,  # dó sustenido,
        587.33,  # ré, 
        622.25,  # ré sustenido, 
        659.26,  # mi, 
        698.46,  # fá, 
        739.99,  # fá sustenido, 
        783.99,  # sol, 
        830.61,  # sol sustenido, 
        880.00,  # lá 
        932.33,  # lá sustenido
        987.77,  # si 
        1046.50  # dó uma oitava acima, sol maior
    ]

# indices da tabela que representa a guitarra
IND_TECLA = 0  # guitarra[i][0] representa uma tecla (str)
IND_NOTA  = 1  # guitarra[i][1] representa uma nota musica (str)
IND_SOM   = 2  # guitarra[i][2] representa o som da nota (list)

#####################################################################
#
# Funções a serem escritas ou consertadas.
#
#-------------------------------------------------------------------
def indice(item, lst):
    '''(obj, list) -> int ou None

    RECEBE um objeto  `item` e uma lista de `lst`.
    RETORNA o índice da posição de `lst` em que é igual a `item`.

    Se nenhuma posição de `lst` é igual a item a função IMPRIME uma 
    mensagem "SOCORRO! Não achei item" e RETORNA None.

    Se mais de uma posição de `lst` é igual a item a função RETORNA o
    maior índice.
    '''
    # modifique o código abaixo para conter a sua solução.
    
    a = item
    lista = lst[:]
    indice = None
    
    n = len(lista)
    
    for i in range(0, n, 1):
        if lista[i] == a:
            indice = i
    
    if indice == None:
        print("SOCORRO! Não achei", a)
        return None
    
    return indice
    
    """
    print("Vixe! Ainda não fiz a função indice()")
    return None
    """  
#-------------------------------------------------------------------
def crie_ruido(n):
    '''(int) -> list

    RECEBE um inteiro n.
    RETORNA uma lista com n valores aleatórios entre -0,5 e 0,5. 

    Para criar a lista use a chamada da função random.uniform(-0.5, 0.5) 
    que retorna um número aleatório em ponto flutuante entre -0.5 e 0.5.
    '''
    # modifique o código abaixo para conter a sua solução.
    
    lista = n * [0]
    
    for i in range(0, n, 1):
        lista[i] = random.uniform(-0.5, 0.5)
      
    return lista

    """
    print("Vixe!! ainda não fiz a função crie_ruido()")
    return []
    """
#-------------------------------------------------------------------
def superposicao(som1, som2):
    '''(list, list) -> list

    RECEBE duas lista de números `som1` e `som2` de  MESMO comprimento.
    A função CRIA e RETORNA a lista resultante da adição
    dos componentes das duas listas, componente a componente.
    '''
    # modifique o código abaixo para conter a sua solução.
    lista1 = som1[:]
    lista2 = som2[:]
    
    n = len(lista1)
    
    soma = n * [0]
    
    for i in range(0, n, 1):
        soma[i] = lista1[i] + lista2[i]
    
    return soma
    
    """
    print("Vixe!! ainda não fiz a função superposicao()")
    return []
    """ 
#--------------------------------------------------------------------
def aplique_ks(ruido, n):
    '''(list, int) -> list

    RECEBE uma lista `ruido` e um inteiro `n`.
    A função CRIA e RETORNA uma lista `som` que respeita as seguintes condições:

      * se `p` é o comprimento da lista `ruido`, então o comprimento da lista 
        `som` é `p+n`.
      * os primeiros `p` componentes de `som` são iguais a `ruido`
      * cada um dos demais componentes da lista `som` deve ser obtido através da 
        equação do algoritmo de Karplus-Strong.
        
    PRÉ-CONDIÇÃO: a função supõe que p é pelo menos 2.    
    '''
    #modifique o código abaixo para conter a sua solução.
    
    lista = ruido[:]
    p = len(lista)
    num = n
    cont = 0
    som = lista + num*[0]
    
    if num != 0:
        for i in range(p, p+n, 1):
            som[i] = 0.996 * ((som[0 + cont] + som[1 + cont])/2)
            cont += 1
    
    return som
    
    """
    print("Vixe!! ainda não fiz a função aplique_ks()")
    return []
    """

####################################################################
#
# As funções crie_guitarra() e crie_musica() devem ser consertadas
#    
####################################################################

#--------------------------------------------------------------------    
def crie_guitarra(teclas=TECLAS, notas=NOTAS):
    '''(list, list) -> list[3]

    RECEBE uma lista `teclas` e uma lista `notas` de mesmo comprimento.
    Cada posição da lista `teclas` contém uma string associada a uma posição do 
    teclado do computador.
    Cada posição da lista `notas` contém uma string associada a uma nota musical.

    A função CRIA e RETORNA uma lista `guitarra` represetando uma guitarra.
    Cada posição `guitarra[i]` é uma lista de 3 posições 
 
       * `guitarra[i][0] é `teclas[i]
       * `guitarra[i][1] é `notas[i]`
       * `guitarra[i][2] é  uma lista `som` com os números que sintetizam o 
                         som associado a `notas[i]`

    DEPENDE da função crie_som_nota() que está TOTALMENTE feita.
    '''
    guitarra = []
    n = len(teclas)
    
    for i in range(n):
        nota      = notas[i]
        tecla     = teclas[i]
        som_nota  = crie_som_nota(nota)
        guitarra += [[tecla, nota, som_nota]]
        
    return guitarra

#--------------------------------------------------------------------
def crie_musica(guitarra, partitura):
    ''' (list[3], list) -> list

    RECEBE uma lista `guitarra` criada pela função `crie_guitarra()` e que
    representa uma guitarra.
    RECEBE ainda uma lista `partitura` em que cada componete é:

        * uma string representado uma nota musical, como por exemplo, 'A','C#',...
        * uma lista de strings representado um acorde, como por exemplo ['A', 'C#', 'E']

    A função CRIA e RETORNA uma lista `musica`.
    Cada posição `musica[i]` corresponde ao som (lista de números) associada a 
    nota ou acorde em partitura[i]. Portanto, o comprimento da lista `musica`
    é igual ao da lista `partitura`.

    DEPENDE da função crie_som_acorde() que está TOTALMENTE feita.
    ''' 
    
    n = len(partitura) 
    musica = [0]*n
    
    for i in range(n):
        acorde = partitura[i] # srt para nota ou list para acorde
        som_acorde = crie_som_acorde(guitarra, acorde) # list de números
        musica[i] = som_acorde
        
    return musica

####################################################################
#
# A função produza_musica() é apenas para você se divertir
#    
####################################################################

#-------------------------------------------------------------------
def produza_musica():
    '''(None) -> list

    RETORNA uma lista `musica` criada pela função `crie_musica()` e 
    correspondente a música na lista `partitura` que é uma
    variável local.

    Cada posição da lista `partitura` é uma string correspondente 
    a uma nota musical como `A`, `A#`, `D`,... ou uma lista de
    strings correspondente a uma acorde como ['A', 'C#', 'E'].

    Essa você é apenas para você se divertir criando suas próprias músicas
    e escutando-as através do programa `server.py`.

    Este exemplo começa com a canção "Brilha, brilha".

    DEPENDE das função crie_guitarra() e crie_musica() que você consertou
    '''
    # 1 crie uma guitarra
    guitarra  = crie_guitarra()
    
    # exemplo que toca apenas uma nota
    # musica = [crie_som_nota('A')] 
    # return musica

    # 2 crie uma partitura
    # partitura = ['F', 'G', 'A', 'F', 'G',  'A', ['B', 'D', 'F']]
    # partitura = ['A', 'B','C#', 'A', 'B', 'C#', ['B', 'D', 'F']]
    partitura = FRERE_JACQUES
    # partitura = STAR_WAY_TO_HEAVEN
    # partitura = AQUARELA
    
    # 3. crie a música associada partitura 
    musica = crie_musica(guitarra, partitura)
    
    # 4. retorne a música
    return musica 


####################################################################
#
# Não altere nada deste ponto em diante
#    
####################################################################

#-------------------------------------------------------------------
def crie_som_nota(nota, n=NO_AMOSTRAS, taxa_de_amostragem=TAXA_DE_AMOSTRAGEM, volume=VOLUME):
    '''(str, int, int, int) -> list

    RECEBE:

       - uma string `nota` reprentando uma no musical
       - um inteiro `n` que será o número de amostras e tamanho da lista que será criada e 
         retornada
       - a taxa_de_amostragem que é o número de amostras por segundo, tiicamente 44110
       - um inteiro que indica o volume do som que será criado

    RETORNA uma lista `som` de com `n` números que será usado para sintetizar o 
    som correspondente a `nota` dada.

    DEPENDE das funções crie_ruido() e aplique_ks().
    '''
    # 1. pegue a frequência da nota
    ind_nota   = indice(nota, NOTAS)
    frequencia = FREQUENCIAS[ind_nota]
    if SOCORRO:
        print("---------------------------------------")
        print("crie_som_nota(): frequencia de '%s'= %f"%(nota, frequencia))
        
    # 2. calcule a atraso, aqui é o UNICO LUGAR que usa a frequência da nota
    atraso   = int(taxa_de_amostragem / frequencia)
    if SOCORRO:
        print("---------------------------------------")
        print("crie_som_nota(): atraso=", atraso)
        
    # 3. crie o ruido: o comprimento `atraso` do ruído é função da frequência da nota
    ruido = crie_ruido(atraso)
    if SOCORRO:
        print("---------------------------------------")
        # print("ruido=", ruido) # lista longa de valores entre -0.5 e 0.5
        print("crie_som_nota(): len(ruido)=", len(ruido))

    # obtenha o som da corda estendendo o ruído com o algoritmo de Karplus-Strong
    amostras = aplique_ks(ruido, n - atraso)
    if SOCORRO:
        print("---------------------------------------")
        # print("amostras depois de ks=", amostras) # lista muito longa de floats
        print("crie_som_nota(): len(amostras)=", len(amostras))

    # ajuste o volume e do som para ser apresentado por server.py
    som = []
    for i in range(len(amostras)):
        som += [int(volume*amostras[i])]
    if SOCORRO:    
        print("---------------------------------------")
        # print("som =", som) # lista muito longa de inteiros
        print("crie_som_nota(): len(som) =", len(som))
        
    return som

#-----------------------------------------------------------------------------
def crie_som_acorde(guitarra, notas):
    ''' (list[3], str ou list) -> list

    RECEBE uma lista `guitarra` criada pela função `crie_guitarra()` e que representa
    uma guitarra.
    RECEBE ainda uma string ou lista `notas`. Se `notas` é uma string então corresponde
    a uma nota musical. Se `notas` é uma lista então é uma lista de strings que
    representam um acorde.

    A função CRIA e RETORNA uma lista `som_acorde` que representa o som da nota ou do 
    acorde musical `notas`, dependendo do caso. O som de um acorde é obtido através
    da superposição das notas que o compoem,

    DEPENDE das funções crie_som_nota() e superposicao().
    '''
    if type(notas) == str:
        # na verdade é apenas uma nota e não um acorde
        som_acorde = crie_som_nota(notas)
    else:
        # notas é uma lista de notas
        # crie uma lista para o som do acorde
        som_acorde = [0]*NO_AMOSTRAS
        # pegue o número de notas
        n = len(notas)
        for i in range(n):
            # pegue o indice nota
            k = indice(notas[i], NOTAS)
            # pegue o som da nota na guitarra: é uma lista
            som_nota = guitarra[k][IND_SOM]
            # superponha o _som da nota_ com o som do _acorde atual_,
            # essencialmente 'som_acorde = som_acorde + som_nota
            som_acorde = superposicao(som_acorde, som_nota)
    return som_acorde  

   
