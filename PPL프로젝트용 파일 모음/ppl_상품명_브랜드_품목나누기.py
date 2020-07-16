#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[24]:


# ppl.csv 파일 불러오기
ppl1 = pd.read_csv('ppl1.csv')
ppl2 = pd.read_csv('ppl2.csv')
ppl3 = pd.read_csv('ppl3.csv')


# In[63]:


# ppl1 상품명
a = range(2,len(ppl1.columns),2)
ppl1_brand_category = ppl1.iloc[:,a]
ppl1_brand_category


# In[64]:


# ppl2 상품명
a = range(2,len(ppl2.columns),2)
ppl2_brand_category = ppl2.iloc[:,a]
ppl2_brand_category


# In[65]:


# ppl3 상품명
a = range(2,len(ppl3.columns),2)
ppl3_brand_category = ppl3.iloc[:,a]
ppl3_brand_category


# In[ ]:





# In[66]:


#  ppl1 브랜드 + 품목
b = range(1,len(ppl1.columns),2)
ppl1_product = ppl1.iloc[:,b]
ppl1_product


# In[67]:


# ppl2 브랜드 + 품목
b = range(1,len(ppl2.columns),2)
ppl2_product = ppl2.iloc[:,b]
ppl2_product


# In[68]:


# ppl3 브랜드 + 품목
b = range(1,len(ppl3.columns),2)
ppl3_product = ppl3.iloc[:,b]
ppl3_product


# In[69]:


ppl_all_product = pd.concat([ppl1_product, ppl2_product, ppl3_product], axis=1)


# In[70]:


ppl_all_brand_category = pd.concat([ppl1_brand_category, ppl2_brand_category, ppl3_brand_category], axis=1)


# In[ ]:





# In[ ]:





# In[73]:


# ppl 브랜드 + 품목 내보내기
ew = pd.ExcelWriter('ppl_all_brand_category.xlsx', engine='xlsxwriter')
ppl_all_product.to_excel(ew, index=False)
ew.save()


# In[74]:


# ppl 상품명 내보내기
ew = pd.ExcelWriter('ppl_all_product.xlsx', engine='xlsxwriter')
ppl_all_brand_category.to_excel(ew, index=False)
ew.save()


# In[ ]:




