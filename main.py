import matplotlib.pyplot as graph

global anos
global pib
paises = []
anos = [2013,2014,2015,2016,2017,2018,2019,2020]
pib = []


arquivo = open("arq_planilha.csv", "r")
conteudo = arquivo.read()
linhas=conteudo.split("\n")
linhas.pop(0)


for linha in linhas:
  dados = linha.split(",")
  paises.append(dados[0])
  pib.append([float(dados[i]) for i in range(1, len(dados))])

pais_escolhido = input("Informe um país: ")
ano = int(input("Informe um ano entre 2013 e 2020: "))


def solicitar_pib():

  if ano != anos:
    print("\nAno não disponível.")
    

  localizou = 1
  for i in range(len(paises)):
    

    if pais_escolhido == paises[i]:
      print(f'\nPIB {paises[i]} em {ano}: US${pib[i][ano-2013]} trilhões.\n\n')

      global pais_escolhido_pib_anos 
      pais_escolhido_pib_anos = pib[i]

      localizou = 1
      break

    else:
      localizou = -1
      

  if localizou == -1:
    print("\nPaís não disponível.")
    exit()
    


solicitar_pib()


def listar_estimativa():
  
    for a in range(len(pib)):
      estimativa_variacao_pib = (pib[a][7]/pib[a][0] -1 )*100

      estimativa_variacao_pib_round ="%2.2f" % round(estimativa_variacao_pib,2)
  
      print(f'{paises[a]} ------------  Variação de {estimativa_variacao_pib_round}% entre 2013 e 2020.')
  

listar_estimativa()


def grafico():

  x = anos
  y = pais_escolhido_pib_anos 

  graph.title("Gráfico da evolução do PIB ao longo dos anos")
  graph.xlabel('Anos ( 2013 - 2020)')
  graph.ylabel('PIB - Produto Interno Bruto')

  graph.plot(x,y)
  graph.show()


grafico()