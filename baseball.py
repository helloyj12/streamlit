# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# plt.rcParams['font.family'] = 'NanumGothic'

# def bar_chart():

#     url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year="

#     years = ['2015', '2016','2017', '2018', '2019', '2020', '2021', '2022' ]

#     baseball = pd.DataFrame([]) 

#     for i in years: 
#         df1 = pd.read_html(url+i)[0]
#         df1['년도'] =  i 
#         baseball = pd.concat([baseball, df1], axis=0)
        
#     # baseball.팀.replace({'두산':'Dusan','삼성':'SS','키움':'KU','한화': 'HH','롯데':'Lotte','넥센':'NecSen'}, inplace=True)
    
#     option = st.selectbox(
#         'How would you like to choice year ?',
#         ('2015', '2016','2017', '2018', '2019', '2020', '2021', '2022'))

#     st.write('You selected:', option)

#     baseball_graph = baseball[baseball.년도==option]
#     x = baseball_graph.팀
#     y = baseball_graph.승률
    
#     fig, ax = plt.subplots(figsize=(12,8))

#     colors = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7' ,'C8', 'C9', 'C10' ]
#     plt.bar(x, y, color= colors ) 

#     for i, v in enumerate( y ):
#         plt.text(i-0.4, v+0.01, v)

#     plt.title( "year korea baseball winrate data", position=(0.5,1.1))
#     st.pyplot(fig)
#     st.dataframe(baseball_graph)

        

# with st.form(key ='Form1'):
#     with st.sidebar:
        
#         select_language = st.sidebar.radio('What do you want ?', ('line', 'bar', 'pie'))
        
        
# if select_language =='bar':
#     bar_chart()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def  plotting_demo():
    
    #uploaded_file = st.file_uploader("Choose a file")

    #money=pd.read_csv(uploaded_file)
    money = pd.read_csv("money_data7.csv")

    option = st.selectbox(
        'How would you like to choice year ?',
        ('2020', '2021', '2022'))

    option2 = int(option)

    st.write('You selected:', option)

    money = money[:] [money['A_YEAR']== option2]

    fig, ax = plt.subplots(2,2, figsize=(12,8))

    plt.subplot(221)
    plt.plot(  list( money['A_MONTH'] ), list( money['A_RATE'] ), color='gold' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('America rate')


    plt.subplot(222)
    plt.plot(  list( money['A_MONTH'] ), list( money['K_RATE'] ), color='seagreen' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('Korea rate')

    plt.subplot(223)
    plt.plot(  list( money['A_MONTH'] ), list( money['KOSPI'] ), color='palevioletred' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('Kospi Rate')

    plt.subplot(224)
    plt.plot(  list( money['A_MONTH'] ), list( money['HOUSE_PRICE'] ), color='cornflowerblue' , marker='o'     ) 
    plt.xticks(tuple(money['A_MONTH']) )
    plt.title('House Price')

    st.pyplot(fig)
    st.dataframe(money)
       

def bar_chart():

    url = "https://sports.news.naver.com/kbaseball/record/index?category=kbo&year="

    years = ['2015', '2016','2017', '2018', '2019', '2020', '2021', '2022' ]

    baseball = pd.DataFrame([]) 

    for i in years: 
        df1 = pd.read_html(url+i)[0]
        df1['년도'] =  i 
        baseball = pd.concat([baseball, df1], axis=0)
        
     # baseball.팀.replace({'두산':'Dusan','삼성':'SS','키움':'KU','한화': 'HH','롯데':'Lotte','넥센':'NecSen'}, inplace=True)
    
    option = st.selectbox(
        'How would you like to choice year ?',
        ('2015', '2016','2017', '2018', '2019', '2020', '2021', '2022'))

    st.write('You selected:', option)

    baseball_graph = baseball[baseball.년도==option]
    x = baseball_graph.팀
    y = baseball_graph.승률
    
    fig, ax = plt.subplots(figsize=(12,8))

    colors = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7' ,'C8', 'C9', 'C10' ]
    plt.bar(x, y, color= colors ) 

    for i, v in enumerate( y ):
        plt.text(i-0.4, v+0.01, v)

    plt.title( "year korea baseball winrate data", position=(0.5,1.1))
    st.pyplot(fig)
    st.dataframe(baseball_graph)    

with st.form(key ='Form1'):
    with st.sidebar:
        
        select_language = st.sidebar.radio('데이터 분석 결과', ('금리와 집값 빠르게 파악하기', '야구 순위와 승률 빠르게 파악하기', '다른 데이터 분석'))
        
        
if select_language =='금리와 집값 빠르게 파악하기':  
    plotting_demo()
  

        
elif select_language =='야구 순위와 승률 빠르게 파악하기':
    bar_chart()
