#!/usr/bin/env python
# coding: utf-8

# # Visualización

# In[26]:


get_ipython().system('pip install pandoc')


# ## 1. Dependencias

# In[29]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import pandoc as pdc


# ## 2. Importar data

# In[49]:


#Se define la ruta en la que guardamos la data que usaremos
ruta = "D:/Users/Camilo 323/Desktop/Universidad/Python Repositorio/Corredores_Davivienda/"


# In[50]:


students = pd.read_csv(ruta+'StudentsPerformance.csv')


# In[51]:


#Cambiamos el nombre de la columna para evitar problemas con el "/"
students.rename(columns = {'race/ethnicity':'ethnicity'},inplace=True)


# In[52]:


students.isna().sum()
#No hay Na's


# In[43]:


students.info()


# In[53]:


students.head()


# ## 3. Estadística descrptiva y visualización

# In[54]:


#Tabla de estadística descriptiva
#Unicamente para variables cuantitativas
students.describe()


# In[55]:


students.columns


# In[60]:


#Porcentaje de estudiantes por etnicidad
plt.figure(figsize = (6,6))
plt.pie(students.ethnicity.value_counts().values, labels = students.ethnicity.value_counts().index, autopct = '%2.1f%%', textprops={'fontsize': 14})
plt.title('Porcentaje de estudiantes por etnicidad')


# 
