def main():
 '''
Programa que lê n notas de provas, calcula a média 
das notas da prova e imprime o número de notas
maiores que a média calculada.
 '''
 # leia o número de notas
 n = int(input("Digite o número de notas: "))
 
 # inicializacões
 soma_notas = 0
 lista_notas = []
  
 # calcule a soma das notas e crie uma lista com as notas
 i = 0
 while i < n:

     nota = float(input("Digite a %da. nota: "%(i+1)))
     soma_notas += nota
     i += 1
     lista_notas += [nota]

 # calcule a média
 media_notas = soma_notas/n
 print("A média das notas é %.1f" %(media_notas))

 # conte quantas notas são acima da média
 cont = 0
 i = 0
 while i < n:
     if lista_notas[i] > media_notas:
        cont += 1
     i += 1 
    
 print("%d nota(s) maiores que %.1f"%(cont, media_notas))
 
#----------------------------------------------------
main()
