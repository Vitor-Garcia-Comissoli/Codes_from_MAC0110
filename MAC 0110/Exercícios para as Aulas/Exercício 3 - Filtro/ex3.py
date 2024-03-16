n = int(input("Digite n: "))
lista_num = []
i = 0
i1 = 0
a = 0
diferente = True
while i < n:

     num = int(input("Digite o %do. número: "%(i+1)))
     if i == 0:
         diferente = True
     else:
         while i > 0 and a > i1:
             if num == lista_num[i1]:
                 diferente = False
                 i1 = a + 1
             #else:
                 #i1 = i1 + 1
             i1 += 1
             
     if diferente:   
        lista_num += [num]
     #else:
        #lista_num = lista_num
        
     i += 1
     i1 = 0
     diferente = True
     a = len(lista_num)
   
print ("Lista de números sem repeticões:")
x = 0
while x < a:
        print(lista_num[x]," ", end="")
        x += 1