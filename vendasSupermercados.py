#coding: utf-8
from cmath import sqrt
from numpy import size
import pandas as pd
import numpy as np
import matplotlib.pyplot as grafico

arquivo = pd.read_csv("/home/brunohelghast/PROFISSIONAL/PYTHON/SCIKIT_LEARN/vendasSupermercado/supermarket_sales.csv")
arquivo["indice"] = pd.RangeIndex(0,len(arquivo),1)

#arquivo["Rating"] = arquivo["Rating"]*100

yangon = arquivo[arquivo["Branch"] == "A"]
mandalay = arquivo[arquivo["Branch"] == "B"]
naypyitaw = arquivo[arquivo["Branch"] == "C"]

female = arquivo[arquivo["Gender"] == "Female"]
male = arquivo[arquivo["Gender"] == "Male"]

clienteMembro = arquivo[arquivo["Customer type"] == "Member"]
clienteNormal = arquivo[arquivo["Customer type"] == "Normal"]

fashion = arquivo[arquivo["Product line"] == "Fashion accessories"]
comidaBebida = arquivo[arquivo["Product line"] == "Food and beverages"]
eletronicos = arquivo[arquivo["Product line"] == "Electronic accessories"]
esportesViagens = arquivo[arquivo["Product line"] == "Sports and travel"]
casaEstiloVida = arquivo[arquivo["Product line"] == "Home and lifestyle"]
saudeBeleza = arquivo[arquivo["Product line"] == "Health and beauty"]

dinheiro = arquivo[arquivo["Payment"] == "Cash"]
credito = arquivo[arquivo["Payment"] == "Credit card"]
carteiraEletronica = arquivo[arquivo["Payment"] == "Ewallet"]
"""
grafico.boxplot([yangon["Rating"],mandalay["Rating"],naypyitaw["Rating"]])
grafico.xlabel("Filiais")
grafico.ylabel("Notas")
grafico.grid()
grafico.show()

print(np.mean(yangon["Rating"]))
print(np.mean(mandalay["Rating"]))
print(np.mean(naypyitaw["Rating"]))

amostraYangon = yangon["Rating"].sample(30)
amostraMandalay = mandalay["Rating"].sample(30)
amostraNaypyitaw = naypyitaw["Rating"].sample(30)
mediaNotaYangon = np.mean(amostraYangon)
mediaNotaMandalay = np.mean(amostraMandalay)
mediaNotaNaypyitaw = np.mean(amostraNaypyitaw)
varianciaNotaYangon = np.var(amostraYangon)
varianciaNotaMandalay = np.var(amostraMandalay)
varianciaNotaNaypyitaw = np.var(amostraNaypyitaw)

mediaVariancias = np.mean([varianciaNotaMandalay,varianciaNotaNaypyitaw,varianciaNotaYangon])

varianciaMedias = ((mediaNotaYangon + mediaNotaNaypyitaw + mediaNotaMandalay) / 2.0)

numerador = varianciaMedias*30
razaoF = numerador/mediaVariancias
print(razaoF)
"""
""" 
grafico.boxplot([dinheiro["Total"],credito["Total"],carteiraEletronica["Total"]])
grafico.xlabel("Formas de pagamento",{"size":16})
grafico.ylabel("Total",{"size":16})
grafico.grid()
grafico.show()

amostraDinheiro = dinheiro["Total"].sample(30)
amostraCredito = credito["Total"].sample(30)
amostraCarteira = carteiraEletronica["Total"].sample(30)

mediaDinheiro = np.mean(amostraDinheiro)
mediaCredito = np.mean(amostraCredito)
mediaCarteira = np.mean(amostraCarteira)

varianciaDinheiro = np.var(amostraDinheiro)
varianciaCredito = np.var(amostraCredito)
varianciaCarteira = np.var(amostraCarteira)

mediaVariancias = np.mean([varianciaDinheiro,varianciaCredito,varianciaCarteira])
varianciaMedia = ((mediaDinheiro + mediaCredito + mediaCarteira) / 2.0)

numerador = varianciaMedia*30
razaoF = numerador/mediaVariancias
print(razaoF)
"""

"""
grafico.boxplot([male["Total"],female["Total"]])
grafico.xlabel("Genero",{"size":16})
grafico.ylabel("Total",{"size":16})
grafico.grid()
grafico.show()

amostraMasculino = male["Total"].sample(50)
amostraFeminino = female["Total"].sample(50)

mediaMasculino = np.mean(amostraMasculino)
mediaFeminino = np.mean(amostraFeminino)

varianciaMasculino = np.var(amostraMasculino)
varianciaFeminino = np.var(amostraFeminino)

mediaVariancias = np.mean([varianciaMasculino,varianciaFeminino])
varianciaMedias = (mediaMasculino + mediaFeminino)

numerador = varianciaMedias*50
razaoF = numerador/mediaVariancias
print(razaoF)
"""

"""
grafico.boxplot([yangon["Total"],mandalay["Total"],naypyitaw["Total"]])
grafico.xlabel("Cidades",{"size":16})
grafico.ylabel("Total",{"size":16})
grafico.grid()
grafico.show()

amostraYangon = yangon["Total"].sample(30)
amostraMandalay = mandalay["Total"].sample(30)
amostraNaypyitaw = naypyitaw["Total"].sample(30)
mediaPrecoYangon = np.mean(amostraYangon)
mediaPrecoMandalay = np.mean(amostraMandalay)
mediaPrecoNaypyitaw = np.mean(amostraNaypyitaw)
varianciaPrecoYangon = np.var(amostraYangon)
varianciaPrecoMandalay = np.var(amostraMandalay)
varianciaPrecoNaypyitaw = np.var(amostraNaypyitaw)

mediaVariancias = np.mean([varianciaPrecoYangon,varianciaPrecoMandalay,varianciaPrecoNaypyitaw])

varianciaMedias = ((mediaPrecoYangon + mediaPrecoMandalay + mediaPrecoNaypyitaw)/2.0)

numerador = varianciaMedias*30
razaoF = numerador/mediaVariancias
print(razaoF)
"""

"""
amostraFashion = fashion["Unit price"].sample(20)
amostraComida = comidaBebida["Unit price"].sample(20)
amostraEletronicos = eletronicos["Unit price"].sample(20)
amostraEsportes = esportesViagens["Unit price"].sample(20)
amostraCasaEstilo = casaEstiloVida["Unit price"].sample(20)
amostraSaude = saudeBeleza["Unit price"].sample(20)

mediaFashion = np.mean(amostraFashion)
mediaComida = np.mean(amostraComida)
mediaEletronicos = np.mean(amostraEletronicos)
mediaEsportes = np.mean(amostraEsportes)
mediaCasaEstilo = np.mean(amostraCasaEstilo)
mediaSaude = np.mean(amostraSaude)

varianciaFashion = np.var(amostraFashion)
varianciaComida = np.var(amostraComida)
varianciaEletronicos = np.var(amostraEletronicos)
varianciaEsportes = np.var(amostraEsportes)
varianciaCasaEstilo = np.var(amostraCasaEstilo)
varianciaSaude = np.var(amostraSaude)

mediaVarianciasProdutos = np.var([varianciaFashion,varianciaComida,varianciaEletronicos,varianciaEsportes,varianciaCasaEstilo,varianciaSaude])

varianciaMediaProdutos = ((mediaFashion + mediaComida + mediaEletronicos + mediaEsportes + mediaCasaEstilo + mediaSaude)/5.0)

numeradorProdutos = varianciaMediaProdutos*20
razaoF = numeradorProdutos/mediaVarianciasProdutos
print(razaoF)

grafico.boxplot([fashion["Unit price"],comidaBebida["Unit price"],eletronicos["Unit price"],esportesViagens["Unit price"],casaEstiloVida["Unit price"],saudeBeleza["Unit price"]])
grafico.xlabel("Produtos",{"size":16})
grafico.ylabel("Preco unitario",{"size":16})
grafico.grid()
grafico.show()
"""

"""
grafico.boxplot([yangon["Unit price"],mandalay["Unit price"],naypyitaw["Unit price"]])
grafico.xlabel("Cidade",{"size":16})
grafico.ylabel("Preco unitario",{"size":16})
grafico.grid()
grafico.show()

amostraYangon = yangon["Unit price"].sample(30)
amostraMandalay = mandalay["Unit price"].sample(30)
amostraNaypyitaw = naypyitaw["Unit price"].sample(30)
mediaPrecoYangon = np.mean(amostraYangon)
mediaPrecoMandalay = np.mean(amostraMandalay)
mediaPrecoNaypyitaw = np.mean(amostraNaypyitaw)
varianciaPrecoYangon = np.var(amostraYangon)
varianciaPrecoMandalay = np.var(amostraMandalay)
varianciaPrecoNaypyitaw = np.var(amostraNaypyitaw)

mediaVariancias = np.mean([varianciaPrecoYangon,varianciaPrecoMandalay,varianciaPrecoNaypyitaw])

varianciaMedias = ((mediaPrecoYangon + mediaPrecoMandalay + mediaPrecoNaypyitaw)/2.0)

numerador = varianciaMedias*30
razaoF = numerador/mediaVariancias
print(razaoF)
"""

"""
print(np.mean(yangon["gross income"]))
print(np.mean(mandalay["gross income"]))
print(np.mean(naypyitaw["gross income"]))
-Naypyitaw apresenta a maior renda média por hora: 16.05 dólares.
"""

""" 
print(np.max(arquivo["Quantity"]))
-Nenhuma venda excedeu 10 ítems
"""

""" 
grafico.boxplot([yangon["Total"],mandalay["Total"],naypyitaw["Total"]])
grafico.xlabel("Cidades")
grafico.ylabel("Total")
grafico.grid()
grafico.show()
-75% das vendas tiveram um valor total inferior a 500 dólares.
"""

""" 
print(arquivo["City"].groupby(arquivo["Gender"]).value_counts())

-Yangon tem mais clientes homems e Naypyitaw tem mais clientes mulheres.
-Existe 17,84% por cento de uma compra ter sido feita por um homem em Yangon.
"""

""" 
print(arquivo["Customer type"].groupby(arquivo["Gender"]).value_counts())

-Mais da metade das compras feitas por mulheres são para mulheres membros e mais da metade das compras feitas por homems são para clientes normais.
-Existe 52% de chance de uma vida ser feita por um cliente membro feminino
"""

""" 
print(arquivo["Customer type"].groupby(arquivo["City"]).value_counts())

-Naypyitaw tem mais clientes membros do que normais, levando a conclusão de que a população dessa cidade tem maior poder aquisitivo que as outras.
-Existe 17,82% de chance dessa compra ter sido feita por um cliente normal em Yangon.
"""

"""
print("{:.2f}".format(np.mean(yangon["Rating"])))
print("{:.2f}".format(np.mean(mandalay["Rating"])))
print("{:.2f}".format(np.mean(naypyitaw["Rating"])))

Avaliação média
    yangon = 7.03
    mandalay = 6.82
    naypyitaw = 7.07
"""

""" 
The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data. Predictive data analytics methods are easy to apply with this dataset.

Branch: Branch of supercenter (3 branches are available identified by A, B and C).
City: Location of supercenters
Customer type: Type of customers, recorded by Members for customers using member card and Normal for without member card.
Gender: Gender type of customer
Product line: General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle, Sports and travel
Unit price: Price of each product in $
Quantity: Number of products purchased by customer
Tax: 5% tax fee for customer buying
Total: Total price including tax
Date: Date of purchase (Record available from January 2019 to March 2019)
Time: Purchase time (10am to 9pm)
Payment: Payment used by customer for purchase (3 methods are available – Cash, Credit card and Ewallet)
COGS: Cost of goods sold
Gross margin percentage: Gross margin percentage
Gross income: Gross income
Rating: Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)
"""

# O valor total da compra não influencia na forma de pagamento pelo cliente. Uma Razão F calculada (para amostras de 30 elementos) é menor que a Razão F tabelada (3.101) para intervalo de confiança de 95%.

# Tanto homems como mulheres gastam o mesmo valor total nas compras. Pois a Razão F calculada (para amostras de 50 elementos) é menor que a Razão F tabelada (3.935) para intervalo de confiança de 95%.

# O valor total das compras são os mesmos entre as cidades. Pois a Razão F calculada (para amostras de 30 elementos) é menor que a Razão F tabelada (3.101) para intervalo de confiança de 95%. Isso quer dizer que as pessoas geralmente gastam o mesmo valor nas compras, independente da cidade em que estejam.

# O preço unitário dos produtos são os mesmos entre os setores. Pois a Razão F calculada (para amostras de 20 elementos) é menor que a Razão F tabelada (2.294) para intervalo de confiança de 95%.

# O preço unitário dos produtos são diferentes entre as cidades. Pois a Razão F calculada (para amostras de 30 elementos) é maior que a Razão F tabelada (3.101) para intervalo de confiança de 95%.

# As filiais apresentaram avaliações diferentes sobre a experiência dos usuários. Uma Razão F calculada (para amostras de 30 elementos) é maior que a Razão F tabelada (3.101) considerando intervalo de confiança de 95%.