def primo(n):
    '''(int) -> bool

       Recebe um número inteiro n e retorna True se n é primo.
       Em caso contrário a função retorna False.
    '''
    n1 = n - 1
    Primo = False
    
    if n == 1:
        return False
    if n <= 0:
        return False
    
    while Primo == False:
        if n % n1 == 0 and n1 != 1:
            return False
        elif n % n1 == 0 and n1 == 1:
            return True
        else:
            n1 = n1 - 1
            
def main ():
    
    print("Programa que imprime todos os primos menores que ou igual a n")
    
    num = int(input("Digite n: "))
    primos = []
    
    for i in range(0,num+1,1):
        if primo(i) == True:
            primos += [i]
    
    if primos == []:
        print("Não há Primos")
    else:
        print("Primos:",primos)

main()