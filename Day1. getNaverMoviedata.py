#!/usr/bin/env python
# coding: utf-8

# In[4]:


import urllib.request
from bs4 import BeautifulSoup


# In[5]:


# 영화 평점 가져오기
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20210426'


# In[6]:


request = urllib.request.urlopen(url)


# In[7]:


getNaverMovie = BeautifulSoup(request, 'html.parser')


# In[8]:


Title_of_Movie = getNaverMovie.findAll("td",{"class": "title"})
Title_of_Movie


# In[10]:


Title_of_Movie[1].find('a')


# In[11]:


for item in Title_of_Movie:
    print(item.find('a').text)


# In[21]:


# 별점 데이터 수집하기
stars= getNaverMovie.findAll("td",{"class":"point"})
stars


# In[22]:


for star in stars:
    print(star.text)


# In[23]:


# 제목과 평점 리스트 정리하기
# 각각 개수 확인하기
len(Title_of_Movie)


# In[24]:


len(stars)


# In[51]:


# 영화 타이틀 리스트로 저장 
movie_title = []
for item in Title_of_Movie:
    movie_title.append(item.text.strip())


# In[36]:


movie_star = []
for star in stars:
    movie_star.append(star.text.strip())


# In[67]:


movie_star_lst = list(zip(movie_title,movie_star))
movie_star_lst


# In[66]:


for i in range(len(movie_star_lst)):
    print("영화 제목:", movie_star_lst[i][0])
    print("평점:", movie_star_lst[i][1])
    print(" ")


# In[62]:


movie_star_lst[1][1]


# In[ ]:




