#!/usr/bin/env python
# coding: utf-8

# In[40]:


from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
import re

def kyochon_store(result):
    for page in range(1, 17+1):
        for region in range(1, 50):
            kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' %(page, region)
            print(kyochon_url)
            
            try:
                html = urllib.request.urlopen(kyochon_url)
            except:
                break
                
            soupkyochon = BeautifulSoup(html,'html.parser')
            tag_ul = soupkyochon.find(class_='list')
            
            if tag_ul == None:  # 탐색 결과 없으면
                break
            
            for store in tag_ul.find_all(class_='store_item'):
                
                if store == None:  # 탐색 결과 없으면
                    continue
                
                store_name = store.find('strong').string
                store_em = store.find('em').text.replace('\t', '').strip().split('\n')
                store_sido = store_em[0]
                store_address = store_em[1]
                store_phone = store_em[2]
                result.append([store_name]+[store_sido]+[store_address]+[store_phone])

    return result

def main():
    result = []
    print('kyochon store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    kyochon_store(result) #[CODE 1] 호출
    kyochon_tbl = pd.DataFrame(result, columns = ('store', 'sido-gu','address','phone'))
    kyochon_tbl.to_csv("C:\My_Python/6장_data/kyochon.csv",encoding = 'cp949', mode = 'w', index = True)
    del result[:]
          
if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:




