def main ():
    lista = leia_seq()
    print ("lista = ", lista)
    inicio, fim, soma_maxima = fatia_max(lista)
    print ("fatia de soma máxima= ", fatia(lista,inicio,fim))
    print ("soma=", soma_maxima)
    print ("ini =", inicio)
    print ("fim =", fim)
    
def fatia(lst, inicio, fim):
    clone = []
    for i in range(inicio, fim, 1):
        clone += [lst[i]]
    return clone
 
def soma(lst):
    soma = 0
    n = len(lst)
    for i in range (0, n, 1):
        soma += lst[i]
    return soma

def fatia_max(lst):
    soma_max = lst[0]
    inicio = 0
    fim = 1
    n = len(lst)
    for i in range(0, n, 1):
        for j in range(i+1, n+1, 1):
            sublista = fatia(lst, i, j)
            s = soma(sublista)
            if s > soma_max:
                soma_max = s
                inicio = i
                fim = j
    return inicio, fim, soma_max

def leia_seq():
    n = int(input("Digite n: "))
    lst = []
    for i in range(1, n+1, 1):
        n1 = int(input("Digite o %do. número: " %(i)))
        lst += [n1]
    return lst

main()