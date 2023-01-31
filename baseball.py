import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'NanumGothic'

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
        
        select_language = st.sidebar.radio('What do you want ?', ('line', 'bar', 'pie'))
        
        
if select_language =='bar':
    bar_chart()
