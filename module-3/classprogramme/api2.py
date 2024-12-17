import requests
import pandas as p 

url="https://fakestoreapi.com/products"

req=requests.get(url)

data=req.json()

# user=p.read_csv('https://fakestoreapi.com/products',sep='|',index_col='id')

for i in data:
  
    d = {'id':i['id'],'title':i['title'],'price':i['price'],'rating':i['rating']['rate']}
    df = p.DataFrame(d,index=[i['id']])
    print(df.to_string())
   

