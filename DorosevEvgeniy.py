#!/usr/bin/env python
# coding: utf-8

# <center style="font-size: 26px"> <b>Проверка уровня знаний Python</b></center>

# In[29]:


# обеспечиваем совместимость с Python 2 и 3
from __future__ import (absolute_import, division, print_function, unicode_literals)

# отключаем предупреждения дистрибутива Anaconda
import warnings
warnings.simplefilter('ignore')


# ### Практические задания:

# #### Загрузите датасет, который вы использовали в блоке задания Power BI как dataframe
# 
# [Датасет с платформы ИНИД](https://www.data-in.ru/data-catalog/datasets/133/#dataset-overview)

# In[30]:


# ВАШ КОД ЗДЕСЬ


import pandas as pd

df=pd.read_excel("C:\\Users\\Jeka\\Desktop\\biocad\\data\\data.xlsx", sheet_name='Data')
data.head()


# #### 1. Выведете типы данных столбцов

# In[31]:


clmn_types = df.dtypes
print(clmn_types)


# #### 3. Уберите из названий столбцов знаки переносов ('\n')

# In[43]:


df=df.rename(columns={"Дата \nпоставки/\nновости":"Дата поставки/новости", 
                      "Карточка помощи \n(описание, текст)":"Карточка помощи (описание, текст)", 
                      "Международные \nорганизации":"Международные организации"})
print(df.columns)


# #### 4. Выведите таблицу, которая позволит просмотреть первую дату поставки и общее количество поставленной вакцины в рамках Марки вакцины и страны.

# In[78]:


table1=pd.DataFrame(df.groupby(['Марка вакцины', 'Страна']).apply(lambda df: int(df['Вакцина (кол-во)'].sum())))
table2=pd.DataFrame(df.groupby(['Марка вакцины', 'Страна']).apply(lambda df: df['Дата поставки/новости'].min()))
res=table1.join(table2, on=['Марка вакцины', 'Страна'], lsuffix='', rsuffix=' ')
res


# #### 5. Напишите код для выгрузки полученной таблицы из задания 4 в xlsx так, чтобы лист Excel-файла назывался "Выгрузка" и были сохранены заголовки таблицы

# In[92]:


res.to_excel("output.xlsx", sheet_name="Выгрузка")

data2=pd.read_excel("output.xlsx")
data2=data2.rename(columns={'0':'Количество вакцин', '0 ':'Первая поставка'})
data2.to_excel("output.xlsx", sheet_name="Выгрузка", index=False)
data3=pd.read_excel("output.xlsx")


# #### 6. Достать домены источников 1, 2, 3
# Для столбцов Источников создать столбцы Доменов, где будет извлечен только домен (источник: https://sputnik-abkhazia.ru/Abkhazia/20200320/..., домен: sputnik-abkhazia.ru). В исходном датасете 3 столбца источника и соответственно должно быть создана 3 столбца с доменами.

# In[118]:


import math

def func(ind):
    temp=df[f"Источник {ind}"]
    domens=[]
    for el in temp:
        if type(el)==float and math.isnan(el):
            domens.append(None)
        else:
            domens.append(el[8:el.find('/', 9)])
    df[f"Домен {ind}"]=domens

func(1)
func(2)
func(3)
df.head()


# In[ ]:




