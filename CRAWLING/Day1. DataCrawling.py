#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# pip install beautifulsoup4 : HTML 원하는 정보 추출 


# In[1]:


# 데이터 추출 패키지
import urllib.request


# In[2]:


url = "http://www.naver.com"
html = urllib.request.urlopen(url)
print(html.read())


# In[3]:


#고양이 이미지 가져오기
# url 확장자와 저장 이름 확장자 맞추기
url = "https://blog.kakaocdn.net/dn/bhc7n0/btqEsgp1iD8/XcRKmzBB3qxQNrfEhjgzPK/img.png"
save_name = "고양이처럼살자.png"


# In[ ]:


# 주피터 노트북이 실행되는 곳에서 실행됨
urllib.request.urlretrieve(url, save_name)


# #### HTML만들어 데이터 추출하기

# In[1]:


from bs4 import BeautifulSoup


# In[5]:


# 가짜 html 만들기
html = """
        <html>
            <body>
                <h1>스크래핑 이란?</h1>
                <p>웹 페이지를 분석하는 것</p>
                <p>원하는 부분을 추출하는 것</p>
                </body>
            </html>
"""


# In[6]:


# html을 추출하는 객체
soup = BeautifulSoup(html, 'html.parser')


# In[7]:


soup


# In[8]:


soup.html.body


# In[9]:


soup.html.body.h1


# In[10]:


soup.html.body.h1.string


# In[ ]:


# 첫번째가 나옴
soup.html.body.p


# In[ ]:


# 두번째 p
#공백이 있어서 next_sibling 두번
soup.html.body.p.next_sibling.next_sibling


# In[6]:


# 가짜 html 만들기
collect_webpage = """
        <html>
            <body>
                <h1 id ="title1">스크래핑 이란?</h1>
                <p id = "body1">웹 페이지를 분석하는 것</p>
                <p>원하는 부분을 추출하는 것</p>
                <h1 id = "title2">스크래핑!!!</h1>
                <p id ="body2">웹페이지 분석!!!</p>
                <p>힘내자~:)!</p>
                </body>
            </html>
"""


# In[7]:


#find활용해서 id 속성이 일치하는 태그 리턴

# html 원하는 놈을 만드는 객체
soup = BeautifulSoup(collect_webpage, 'html.parser')


# In[8]:


soup


# In[9]:


soup.find(id = "title2")#.string: 내용만 뽑기


# In[10]:


soup.find(id = "body2").string


# In[11]:


html = """
    <html>
        <body>
            <ul class ="greet">
                <li>hello</li>
                <li>bye</li>
                <li>welcome</li>
            </ul>
            <ul class = "reply">
                <li>ok</li>
                <li>no</li>
                <li>sure</li>
            </ul>
            <div>
                <ul>
                    <li>open</li>
                    <li>close</li>
                </ul>
            </div>
        </body>
    </html>
    """


# In[12]:


get_html = BeautifulSoup(html, "html.parser")


# In[13]:


get_html


# In[14]:


ul = get_html.find("ul",{"class":"reply"})
ul


# In[27]:


#리스트로 저장
li = get_html.findAll('li')
li 


# In[24]:


for item in get_html.findAll("li"):
    print(item.text)


# In[23]:


for item in get_html.findAll("li"):
    print("itme text   = ",item.text)
    print("itme string = ",item.string)
    print("="*25)


# In[28]:


# 안에 있는 내용만 모두 보이게 하는 법
for item in li :
    print(item.text)
    


# In[ ]:


# class : reply 안에 li 태그
soup.find("ul",{"class":"reply"}).findAll("li")


# In[ ]:


for item in soup.find("ul",{"class":"reply"}).findAll("li"):
    print(item.text)


# In[ ]:


# 네이버 스크래핑
url = "https://www.naver.com"


# In[ ]:


# url에서 웹페이지 가져올 객체 생성
request = urllib.request.urlopen(url)


# In[ ]:


naver_web_page = BeautifulSoup(request, "html.parser")


# In[ ]:


naver_web_page.find("ul",{"class":"type_fix"})


# In[ ]:


naver_web_page.find("ul",{"class":"type_fix"}).findAll("li")


# In[ ]:


for item in naver_web_page.find("ul",{"class":"type_fix"}).findAll("li"):
    print("item.string = ", item.text)
    print("item.text = ", item.string)
    print("-"*50)


# In[42]:


compare_string_text = """
    <li>안녕</li>
    <li>
        또만나
    </li>
    <li><a href = "https://www.naver.com">반가워</a></li>
    <li>
        <a href = "https://www.naver.com">고마워</a>
    </li>
    <li><a href = "https://www.naver.com">미안해</a>
        <a href = "https://www.naver.com"></a></li>
    <li><a href = "https://www.naver.com">good</a>
        <a href = "https://www.naver.com"></li>
    <li>
        <a href = "https://www.naver.com">Good!!</a>
        <a href = "https://www.naver.com">Bad!!</a></li>
    """


# In[43]:


get_compare_html = BeautifulSoup(compare_string_text, "html.parser")
get_compare_html


# In[44]:


for item in get_compare_html.findAll("li"):
    print("item.text: ",item.text.strip())
    print("item.string: ",item.string)
    print('-'*25)


# In[ ]:




