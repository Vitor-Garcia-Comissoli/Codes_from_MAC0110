# -*- coding: utf-8 -*-

# True para exibir a construÃ§Ã£o da matriz
MOSTRE = False

# PALETA
# selecione um cÃ³digo de cores
# ver https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
COLOR_MAP = "prism"

# DIMENSÃ•ES
DPI = 1   # para leitura do teclado de matrizes pequenas


#-----------------------------------------------------
def main():
    '''
    Programa que lÃª n e uma matriz de inteiros n x n
    e verifica se a matriz Ã© simÃ©trica.
    '''
    # 1 leia matriz
    mat = leia_matriz()
    
    # 2 exiba matriz
    exiba_matriz(mat)
    
    # 3 verifique se a matriz Ã© simÃ©trica
    b = simetrica(mat)
    if b: # b == True
        print("Matriz é simétrica")
    else:
        print("Não é simétrica")
        
    # 4 exiba matriz imagem associada Ã  matriz
    exiba_imagem(mat)
    
#------------------------------------------------
def simetrica(mat):
    '''(matriz) -> bool
    RETORNA True se matriz Ã© simÃ©tria e False em
    caso contrÃ¡rio.
    
    HÃ¡ vÃ¡rias soluÃ§Ãµes possÃ­veis: 
      
        - usar indicado de passagem
        - evitar comparaÃ§Ãµes supÃ©rfluas
        
     FaÃ§a a sua preferida   
    '''
    # pegue a dimensÃ£o da matriz
    nlin = len(mat)
    ncol = len(mat[0]) 
    
    # se matriz nÃ£o Ã© quadrada, nÃ£o Ã© simÃ©trica
    if nlin != ncol: 
        return False
    
    # percorrer matriz linha por linha 
    for i in range(nlin):     # for i in range(1, nlin):
        for j in range(ncol): #     for j in range(i): 
            if mat[i][j] != mat[j][i]:
                print(f"{mat[i][j]} = mat[{i}][{j}] != mat[{j}][{i}] = {mat[j][i]}")
                return False # acaba aqui
    return True             
    
            
        
#---------------------------------------------------
def leia_matriz():
    '''(None) -> matriz (list de list)
    LÃª uma matriz atravÃ©s do teclado e retorna uma 
    lista de lista representando a matriz
    '''
    if MOSTRE:
        print("leia_matriz(): entrando")
        pause()
        
    # 1 leia as dimensÃµes
    nlin = int(input("Digite o no. de linha: "))
    ncol = int(input("Digite o no. de colunas: "))
    
    print(f"dimensÃ£o {nlin} x {ncol}")
    
    # crie a matriz 
    mat = crie_matriz(nlin, ncol) #!!!!!!!! <3
    if MOSTRE:
        print(f"Matriz: {mat}")
    
    # preencha a matriz
    for i in range(nlin):
        # leia linha i
        for j in range(ncol):
            valor = int(input(f"Digite elem [{i}][{j}]: ")) 
            mat[i][j] = valor
            if MOSTRE:
               print(mat)
               pause()
            
    if MOSTRE:
       print("leia_matriz(): saindo")
       pause()        
    return mat

#--------------------------------------------------
def crie_matriz(nlin, ncol, val=0):
    '''(int, int, obj) -> matriz (list de list)
    RECEBE inteiros `nlin` e `ncol` e um valor `val`.
    RETORNA uma matriz de dimensÃ£o `nlin` x `ncol` com 
    `val` em cada posiÃ§Ã£o.
    Exemplo:
    In [1]: mat = crie_matriz(2,3)
    In [2]: mat
    Out[2]: [[0, 0, 0], [0, 0, 0]]
    '''
    if MOSTRE: 
        print("crie_matriz(): entrando")
        pause()
    matriz = []
    if MOSTRE:
        print(f"matriz inicial: {matriz}")
        pause()
    # crie a matriz
    for i in range(nlin):
        # crie uma linha com ncol caras
        linha = ncol*[val] # [val] + [val] +...+[val]
        # coloque na matriz
        matriz += [linha]
        if MOSTRE:
           print(f"matriz com linha {i}: {matriz}")
           pause()
    if MOSTRE:
        print("crie_matriz(): saindo")
        pause()
    return matriz

    
#--------------------------------------------------
def exiba_matriz(matriz):
    '''(matriz) -> None
    RECEBE uma matriz `mat`.
    EXIBE essa matriz ...
    AINDA PRECISA SER FEITA
    '''
    
    print("Matriz: ")
    for linha in matriz:
        print(linha)
    
    """
    nlin = len(matriz)
    ncol = len(matriz[0])
    
    # max_len = max_len_valor(matriz) + 1 # exercício
    
    print(f'Matriz: {nlin} x {ncol}')
    for i in range (nlin):
        for j in range(ncol):
            print(f'{matriz[i][j]:{max_len}}')
        print()
    """
#----------------------------------------------------------------    
def exiba_imagem(img):
    # ver https://matplotlib.org/
    from matplotlib import pyplot as plt

    # pegue a dimensÃ£o/forma da imagem
    nlin = len(img)
    ncol = len(img[-1])

    # pontos por polegada (dpi)
    fig = plt.figure(figsize=(ncol/DPI, nlin/DPI))

    # coloque um tÃ­tulo
    plt.title(f"MAC0110: matriz {nlin} x {ncol}")
    
    # desenhe usando o cÃ³digo de cores
    pcolor = plt.pcolor(img, cmap = COLOR_MAP)
    
    # mostre o desenho
    plt.show()
        
#------------------------------------------------------
def pause():
    '''(None) -> None
    PARA a execuÃ§Ã£o atÃ© que seja teclado ENTER
    '''
    input("Tecle ENTER para continuar. ")
    
#------------------------------------------------------
# inÃ­cio da execuÃ§Ã£o do programa
if __name__ == "__main__":
    main()