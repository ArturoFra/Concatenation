#!/usr/bin/env python
# coding: utf-8

# # Concatenar y apendizar datas sets

# In[1]:


import pandas as pd


# In[4]:


red_wine = pd.read_csv("C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/datasets/wine/winequality-red.csv", sep=";")


# In[5]:


red_wine.head()


# In[7]:


red_wine.columns.values


# In[8]:


red_wine.shape


# In[9]:


white_wine = pd.read_csv("C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/datasets/wine/winequality-white.csv", sep=";")


# In[12]:


white_wine.head()


# In[13]:


white_wine.columns.values


# In[15]:


white_wine.shape


# Recordar que el axis=0 denota el eje horizontal y axis=1 denota el eje vertical

# In[17]:


wine_data =pd.concat([red_wine, white_wine], axis=0)
wine_data


# In[21]:


data1 = wine_data.head(10)
data2 = wine_data[300:310]
data3 = wine_data.tail()


# In[22]:


wine_scramble = pd.concat([data1, data2, data3], axis=0)


# In[23]:


wine_scramble


# # Datos distribuidos

# In[25]:


data = pd.read_csv("C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/datasets/distributed-data/001.csv")


# In[27]:


data


# Bucle para recorrer y abrir cada uno de los ficheros

# In[28]:


filepath="C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/datasets/distributed-data/"


# In[31]:


for i in range(2, 333):
    if i < 10:
        filename="00" + str(i)
    elif 10 <= i < 100:
        filename="0" + str(i)
    elif i>=100:
        filename=str(i) 
    file = filepath + filename + ".csv"
    temp_data = pd.read_csv(file)
    
    data= pd.concat([data, temp_data], axis=0)
    


# In[32]:


data.shape


# # Joins de dataset

# In[33]:


filepath="C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/datasets/athletes/"


# In[34]:


data_main= pd.read_csv(filepath + "Medals.csv")


# In[35]:


data_main


# In[36]:


a =data_main["Athlete"].unique().tolist()


# In[37]:


len(a)


# In[39]:


data_country = pd.read_csv(filepath + "Athelete_Country_Map.csv")


# In[40]:


data_country.head()


# In[41]:


len(data_country)


# In[43]:


data_country[data_country["Athlete"] == "Aleksandar Ciric"]


# In[54]:


data_sports = pd.read_csv(filepath + "Athelete_Sports_Map.csv")


# In[55]:


data_sports.head()


# In[56]:


len(data_sports)


# In[57]:


data_sports[(data_sports["Athlete"]=="Chen Jing") | 
               (data_sports["Athlete"]=="Richard Thompson") | 
               (data_sports["Athlete"]=="Matt Ryan")]


# In[ ]:


d


# In[ ]:





# In[52]:


data_sports


# In[113]:


data_country_dp= data_country.drop_duplicates(subset="Athlete")


# In[114]:


len(data_country_dp)


# In[115]:


data_main_country = pd.merge(left = data_main, right = data_country_dp,
                            left_on="Athlete", right_on="Athlete")


# In[63]:


data_main_country.head(10)


# In[64]:


data_main_country[data_main_country["Athlete"] == "Aleksandar Ciric"]


# In[69]:


data_sports_dp = data_sports.drop_duplicates(subset="Athlete")


# In[71]:


data_final = pd.merge(left = data_main_country, right = data_sports_dp,
                            left_on="Athlete", right_on="Athlete")


# In[72]:


data_final.head(10)


# # Tipos de Joins

# ### Inner Join 

# In[74]:


Image(filename="C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/notebooks/resources/inner-join.png")


# In[73]:


from IPython.display import Image


# In[79]:


import numpy as np


# In[85]:


out_athletes = np.random.choice(data_main["Athlete"], size=6, replace = False)


# In[96]:



data_country_dlt = data_country_dp[(~data_country_dp["Athlete"].isin(out_athletes)) &
                                  (data_country_dp["Athlete"] != "Michael Phelps")]
data_sports_dlt= data_sports_dp[(~data_sports_dp["Athlete"].isin(out_athletes)) &
                                  (data_sports_dp["Athlete"] != "Michael Phelps")] 
data_main_dlt = data_main[(~data_main["Athlete"].isin(out_athletes)) &
                                  (data_main["Athlete"] != "Michael Phelps")]


# In[97]:


len(data_country_dlt)


# In[98]:


len(data_sports_dlt)


# In[99]:


len(data_main_dlt)


# In[ ]:





# In[116]:


data_sports_dlt


# In[ ]:





# In[117]:


data_main_dlt


# In[ ]:





# In[ ]:





# In[ ]:





# In[91]:


data_country_dlt.head()


# In[ ]:





# In[ ]:





# Si el conjunto A tiene 60 filas y el cojunto B tiene 40 pero solo hay 30 filas coincidentes entre ellos, entonces el nuevo dataframe solo tendra 30 filas. 

# In[103]:


merged_inner = pd.merge(left = data_main, right = data_country_dlt, how = "inner", 
                       left_on = "Athlete", right_on="Athlete")


# In[107]:



merged_inner.head()


# In[ ]:





# ### Left Join 

# In[75]:


Image(filename="C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/notebooks/resources/left-join.png")


# Solo devuelve los datos del conjunto Izquierdo en este caso del conjunto A, si el conjunto A tiene 60 filas y el B 40, el dataframe resuktate sería de 60 filas dado que tambien cuenta con la intersección B, estos datos serán rellenados con NA en caso de que no tengan información.

# In[109]:


merged_left = pd.merge(left = data_main, right = data_country_dlt, how = "left", 
                       left_on = "Athlete", right_on="Athlete")
len(merged_left)


# In[110]:


merged_left.head()


# In[ ]:





# In[ ]:





# ### Right Join 

# In[76]:


Image(filename="C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/notebooks/resources/right-join.png")


# Es el caso contrario a left-join, y en ejemplo solo se toman en cuenta los valores del conjunto B.

# In[118]:


merged_right = pd.merge(left = data_main_dlt, right = data_country_dp, how = "right", 
                       left_on = "Athlete", right_on="Athlete")
len(merged_right)


# In[121]:


merged_right.tail()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Outer Join 

# In[77]:


Image(filename="C:/Users/A Emiliano Fragoso/Desktop/MLcourse/python-ml-course-master/notebooks/resources/outer-join.png")


# Considera la información de ambos conjuntos, si el conjunto A tiene 60 filas , el conjunto B tiene 40 filas y entre estos la unión es dde 20 filas, el dataframe resultante queda de 80 filas. 

# In[125]:


data_country_jb = data_country_dlt.append(
    {
        "Athlete": "Emiliano Fragoso",
        "Country": "México"
        
        
        
        
    },ignore_index = True


)


# In[126]:


merged_outer = pd.merge(left = data_main, right=data_country_jb, how = "outer",
                       left_on = "Athlete", right_on="Athlete")
len(merged_outer)


# In[127]:


merged_outer.tail()


# In[128]:


merged_outer.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




