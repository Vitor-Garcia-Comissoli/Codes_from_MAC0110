n = int(input("Digite o tamanho da sequ�ncia: "))

lista_num = []
i = 0
i1 = 0
a = 0
diferente = True
ocorrencia = n * [1]

while i < n:

     num = int(input("Digite o %do. n�mero: "%(i+1)))
     if i == 0:
         diferente = True
     else:
         while i > 0 and a > i1:
             if num == lista_num[i1]:
                 diferente = False
                 ocorrencia[i1] += 1
                 i1 = a + 1
             i1 += 1
             
     if diferente:   
        lista_num += [num]
        
     i += 1
     i1 = 0
     diferente = True
     a = len(lista_num)

print ("Valor :","Ocorr�ncias")
x = 0
while x < a:
        print(" ",lista_num[x],"  :     ",ocorrencia[x])
        x += 1