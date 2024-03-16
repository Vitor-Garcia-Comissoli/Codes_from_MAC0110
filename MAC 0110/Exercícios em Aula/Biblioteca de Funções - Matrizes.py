# -*- coding: utf-8 -*-
'''
   Nossa biblioteca de funções para manipular matrizes.

   API:

   * crie_matriz(nlin, ncol, val=0)
   * exiba_matriz(matriz)
   * to_string(matriz)
   * leia_matriz(None)
   * leia_matriz_arquivo(nome_arq)
   * simetrica(matriz)
   * rode_dir(matriz)
   * rode_esq(matriz)
   * gire_horizontal(matriz)
   * give_vertical(matriz)
'''
# constante usada para testar as funÃ§Ãµes
MOSTRE = False

# IMAGENS
MAT_3x3  = "mat_3x3.txt"
MAT_4x4  = "mat_4x4.txt"
RUIDO_100x100 = "ruido_100x100.txt"
BLACK_PANTHER = "black-panther.txt"
RELOGIOS = "relogios.txt"
STINKBUG = "stinkbug.txt"
ARVORES = "arvores.txt"
DR_KING  = "dr_king.txt"

# CÃ“DIGOS DE CORES
# ver https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
PRISM = "prism"
GRAY  = "gray"
HSV   = "hsv"

# ponto por polegada
DPI_1   = 1   # bom para mat_3x3 mat_4x4
DPI_10  = 10  # bom para ruido_100x100
DPI_100 = 100 # bom para resoluÃ§Ãµes maiores

#--------------------------------------------------
def mult_matriz(matrizA, matrizB):
    
    m = len(matrizA)
    n = len(matrizB)
    p = len(matrizB[0])
    
    matrizC = crie_matriz(m, p, 0)
    
    for i in range (m):
        for j in range (p):
            for k in range (n):
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
    
    return matrizC
#--------------------------------------------------
def grave_matriz(matriz, nome_arq = 'matriz.txt'):
    
    nlin = len(matriz)
    ncol = len(matriz[0])
    
    arq = open(nome_arq, 'w', encoding = 'utf-8')
    
    arq.write(f'{nlin} x {ncol}')
    arq.write('\n')
    
    for i in range(nlin):
        for j in range (ncol):
            arq.write(f'{matriz[i][j]}')
        arq.write('\n')
    
    arq.close()

#--------------------------------------------------
def crie_matriz(nlin, ncol, val=0):
    ''' (int, int, obj) -> matriz (list de list)

    RECEBE dois inteiros `nlin`, `ncol` e um valor `val`.
    RETORNA uma matriz de dimensÃ£o `nlin` x `ncol` em que 
    todas as posiÃ§Ãµes tem `val`
    Exemplo:
    In [1]: mat = crie_matriz(2,3)
    In [2]: mat
    Out[2]: [[0, 0, 0], [0, 0, 0]]
    '''
    matriz = []
    # crie a matriz
    for i in range(nlin):
        # crie uma linha com ncol itens
        linha = ncol*[val] # [val] + [val] +...+[val]
        # coloque na matriz
        matriz += [linha]
    return matriz

#-------------------------------------------------------
def exiba_matriz(matriz):
    '''(matriz) -> None

    RECEBE e exibe uma matriz de inteiros.
    '''
    print(to_string(matriz)) # IDEIA NOVA

#-------------------------------------------------------
def to_string(matriz):
    '''(matriz) -> str

    RECEBE uma matriz `matriz`
    RETORNA uma string que representa a matriz.

    A string retornado Ã© usada para exibir a matriz atravÃ©s de print().
    '''
    s = "" 
    nlin = len(matriz)
    ncol = len(matriz[0])

    # pegue o maior nÃºmero caracteres para escreve um valor
    max_len = max_len_valor(matriz) + 1 # EXERCÃCIO

    s += "Matriz: %d x %d\n" %(nlin, ncol)
    for i in range(0, nlin, +1):
        for j in range(0, ncol, +1):
             s +=  f"{matriz[i][j]:{max_len}}"  # NOVO 
        # pule uma linha    
        s += "\n"

    return s
            
#-------------------------------------------------------------------        
def leia_matriz():
    '''(None) -> matriz

    LÃª do teclado os elementos de uma matriz .
    RETORNA uma lista de listas representando a matriz.
    '''
    # 1 leia as dimensÃµes
    nlin = int(input("Digite o no. de linha: "))
    ncol = int(input("Digite o no. de colunas: "))
    
    # crie a matriz 
    matriz = crie_matriz(nlin, ncol)
    
    # preencha a matriz
    for i in range(nlin):
        # leia linha i
        for j in range(ncol):
            valor = int(input(f"Digite elem [{i}][{j}]: ")) 
            matriz[i][j] = valor
    return matriz

#-------------------------------------------------------
def leia_matriz_arquivo(nome_arq):
    '''(str) -> matriz (list de list)

    RETORNA uma matriz lida de um arquivo.

    A funÃ§Ã£o supÃµe que os dois primeiros valores do arquivo 
    sÃ£o nÃºmero inteiros representando a dimensÃ£o da matriz:

        nÃºmero de linha nlin e nÃºmero de coluna ncol.

    Em seguida devem estar dispostos o nlin por ncol 
    elementos da matriz.

    Todos os valores devem estar separados por pelo menos
    um branco.
    '''
    arq = open(nome_arq, 'r', encoding= 'utf-8')
    arq_txt = arq.read()
    arq.close()
    
    lst = arq_txt.split()
    nlin = int(lst[0])
    ncol = int(lst[1])
    
    matriz = crie_matriz (nlin,ncol)
    
    k = 2
    for i in range(nlin):
        for j in range(ncol):
            matriz[i][j] = int(lst[k])
            k += 1
            
    return matriz

#------------------------------------------------
def simetrica(matriz):
    '''(matriz) -> bool

    RETORNA True se matriz Ã© simÃ©tria e False em
    caso contrÃ¡rio.
    
    HÃ¡ vÃ¡rias soluÃ§Ãµes possÃ­veis: 
      
        - usar indicado de passagem
        - evitar comparaÃ§Ãµes supÃ©rfluas
        
    FaÃ§a a sua preferida   

    PrÃ©-condiÃ§Ã£o: a funÃ§Ã£o supÃµes que a matriz e quadrada

    In [1]: a = [[1,2,3],[2,1,4],[3,4,1]]
    In [2]: a
    Out[2]: [[1, 2, 3], [2, 1, 4], [3, 4, 1]]
    In [3]: imprima_matriz(a)
    Matriz: 3 x 3
         1     2     3
         2     1     4
         3     4     1
    In [4]: simetrica(a)
    Out[4]: True
    '''
    # pegue a dimensÃ£o da matriz
    nlin = len(matriz)
    ncol = len(matriz[0]) 
    
    # percorrer matriz linha por linha 
    for i in range(1, nlin):
        for j in range(i): 
            if matriz[i][j] != matriz[j][i]:
                print(f"{matriz[i][j]}=matriz[{i}][{j}] != matriz[{j}][{i}]={matriz[j][i]}")
                return False # acaba aqui
    return True             

#----------------------------------------------------------------
def rode_dir(matriz):
    '''(matriz) -> matriz

    RECEBE uma matriz `matriz`.
    RETORNA a `matriz` rotacionada para a direita (horÃ¡rio)
    '''
    nlin = len(matriz)
    ncol = len(matriz[0])
    d = crie_matriz(ncol, nlin)
    #exiba_matriz(d)
    #pause()
    
    for j in range(ncol):
        for i in range(nlin):
            d[i][j] = matriz[nlin - j - 1][i]
        #exiba_matriz(d)
        #pause()
    
    return d

#----------------------------------------------------------------
def rode_esq(matriz):
    '''(matriz) -> matriz

    RECEBE uma matriz `matriz`.
    RETORNA a `matriz` rotacionada para a esquerda (horÃ¡rio).
    '''
    return []

#----------------------------------------------------------------
def gire_horizontal(matriz):
    '''(matriz) -> matriz

    RECEBE uma matriz `matriz`.
    RETORNA a `matriz` refletida horizontalmente (cima-baixo).
    '''
    #exiba_matriz(matriz)
    #pause()
    nlin = len(matriz)
    ncol = len(matriz[0])
    h = crie_matriz(nlin, ncol)
    #exiba_matriz(h)
    #pause()
    
    for i in range(nlin):
        for j in range(ncol):
            h[i][j] = matriz[nlin - i - 1][j]
        #exiba_matriz(h)
        #pause()
    
    return h

#----------------------------------------------------------------
def gire_vertical(matriz):
    '''(matriz) -> matriz

    RECEBE uma matriz `matriz`.
    RETORNA a `matriz` refletida verticalmente (esquerda-direita).
    '''
    #exiba_matriz(matriz)
    #pause()
    nlin = len(matriz)
    ncol = len(matriz[0])
    v = crie_matriz(nlin, ncol)
    #exiba_matriz(v)
    #pause()
    
    for j in range(ncol):
        for i in range(nlin):
            v[i][j] = matriz[i][ncol - j - 1]
        #exiba_matriz(v)
        #pause()
    
    return v

#----------------------------------------------------------------    
def exiba_imagem(img, color_map = GRAY, dpi = None):
    '''(matriz) -> None

    RECEBE uma matriz de inteiros `img` e exibe a matriz como 
    uma imagem
    '''
    # ver https://matplotlib.org/
    from matplotlib import pyplot as plt

    # pegue a dimensÃ£o/forma da imagem
    nlin = len(img)
    ncol = len(img[-1])

    # determine o nÃºmero de pontos por polegada (= dots per inch)
    if dpi == None:
        dpi = max(nlin, ncol)/10 # o 10 Ã© chute
        
    # pontos por polegada (dpi)
    fig = plt.figure(figsize=(ncol/dpi, nlin/dpi))

    # coloque um tÃ­tulo
    plt.title(f"MAC0110: matriz {nlin} x {ncol}")
    
    # desenhe usando o cÃ³digo de cores
    pcolor = plt.pcolor(img, cmap = color_map)
    
    # mostre o desenho
    plt.show()

#------------------------------------------------------
#
# FUNÇÕES AUXILIARES
#
#-----------------------------------------------------

#------------------------------------------------------
def pause():
    '''(None) -> None
    PARA a execuÃ§Ã£o atÃ© que seja teclado ENTER
    '''
    input("Tecle ENTER para continuar. ")

#-----------------------------------------------------    
def max_len_valor(matriz):
    '''(matriz) -> int 

    RECEBE uma matriz.
    RETORNA o maior nÃºmero de caracteres necessÃ¡rios para exibir
    qualquer valor da matriz.
    '''
    # EXERCÃCIO
    # escreva a sua funÃ§Ã£o a seguir
    print("Vixe! Ainda nÃ£o fiz a funÃ§Ã£o max_len_valor()... :-(")
    return 4 # deve ser ok para matrizes bem comportadas      
    max_len = 0
    return max_len
