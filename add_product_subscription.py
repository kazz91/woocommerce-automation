#Deletar produtos em massa no Wordpress


!pip install woocommerce

from woocommerce import API
import time


wcapi = API(
      url = 'sua_url',
      consumer_key='sua_consumer_key',
      consumer_secret='sua_consumer_secret',
      version="wc/v3",
      timeout=400
)

ids = []

for c in range(1,21):
      variavel = "products?per_page=100&status=draft&page="+str(c)
     
      x = wcapi.get(variavel).json()
      
      for i in range(len(x)):

          valores = x[i] 

          id = list(valores.items())[0][1]

          ids.append(id)
print()        
print("==========================================================")
print('Ao todo encontramos:',len(ids),' produtos')
print('Maravilha! Agora vamos começar a remover esses produtos!')
print("==========================================================")
print()

for d in ids:
      xis= str(d)
      z = 'products/'+xis
      deletar = wcapi.delete(z, params={"force": True}).json()
      print('O produto',xis,'foi deletado')
print()    
print('Todos os produtos foram deletados!')
