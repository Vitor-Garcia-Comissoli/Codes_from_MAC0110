def leia_notas():
    
    # leia o número de notas
    n = int(input("Digite o número de notas: "))
    lista_notas = []
    i = 0
    while i < n:
        nota = float(input("Digite a %da. nota: "%(i+1)))
        i += 1
        lista_notas += [nota]
        
    return lista_notas

def media_notas(list):
    soma_notas = 0
    i = 0
    n = len(list)
    while i < n:
        soma_notas += list[i]
        i += 1
    # calcule a média
    media_notas = soma_notas/n
    
    return media_notas
   
def maiores_notas(list, m):
    n = len(list)
    i = 0
    maiores = []
    while i < n:
        if list[i] > m:
            a = list[i]
            maiores += [a]
        i += 1 
    
    return maiores
    
def main():

    notas = leia_notas()
    # print (notas)
    media = media_notas(notas)
    print("A média das notas é %.1f" %(media))
    maiores = maiores_notas(notas, media)
    cont = len(maiores)
    print("%d nota(s) maior(es) que %.1f"%(cont, media))
    # print (maiores)
    print("Notas maiores que %.1f:"%(media))
    i = 0
    while i < cont:
        print(maiores[i])
        i += 1
        
main()   