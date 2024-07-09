import streamlit as st
import pandas as pd
import pickle
import numpy as np
import time
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('diamondcleaned.csv')

# Create Streamlit container
interface = st.container()
sidebar=st.sidebar.container()

with interface:

    def label_encode_process(data_frame):
        le = LabelEncoder()
        for column in data_frame.columns:
            if data_frame[column].dtype == 'object':
                data_frame[column] = le.fit_transform(data_frame[column])
        return data_frame
    
    label_encoder = LabelEncoder()
    
    cut_encoding = label_encoder.fit_transform(df['cut'])
    cut_mapping = {name: value for name, value in zip(df['cut'].str.capitalize().tolist(), cut_encoding)}
    
    color_encoding = label_encoder.fit_transform(df['color'])
    color_mapping = {name: value for name, value in zip(df['color'].str.capitalize().tolist(), color_encoding)}
    
    clarity_encoding = label_encoder.fit_transform(df['clarity'])
    clarity_mapping = {name: value for name, value in zip(df['clarity'].str.capitalize().tolist(), clarity_encoding)}
    
    st.write("<h1 style='text-align: center;'>Diamond Price Predictor💎</h1>", unsafe_allow_html=True)
    st.write('***')
    st.write('### Enter Diamond Features')

    cut_col, color_col, clarity_col = st.columns(3)
    
    with cut_col:
        cut = st.selectbox(label='Quality of the Cut', options=df['cut'].str.capitalize().sort_values().unique().tolist())
        carat = st.number_input(label='Carat', max_value=df['carat'].max())
        
    with color_col:
        color = st.selectbox(label='Diamond Colour', options=df['color'].str.capitalize().sort_values().unique().tolist())
        size = st.number_input(label='Size', max_value=df['size'].max())
        
    with clarity_col:
        clarity = st.selectbox(label='How clear the Diamond', options=df['clarity'].str.capitalize().sort_values().unique().tolist())
        
    st.markdown('***')
    
    cut_encoded = cut_mapping[cut]
    color_encoded = color_mapping[color]
    clarity_encoded = clarity_mapping[clarity]
    
    input_features = pd.DataFrame({
        'carat': [carat],
        'size': [size],
        'cut': [cut_encoded],
        'color': [color_encoded],
        'clarity': [clarity_encoded]
    })
    
    st.subheader('Model Prediction')
    with open('final_model.pickle', 'rb') as pickled_model:
        model = pickle.load(pickled_model)

    
    if st.button('Predict'):
            dia_price = model.predict(input_features)
            
            with st.spinner('Sending input features to model...'):
                time.sleep(2)
    
            st.success('Prediction is ready')
            time.sleep(1)
            if dia_price[0]<0:
                st.markdown(f'### Diamond has no price')
            else:
                st.markdown(f'### Diamond\'s estimated price is {int(dia_price[0])} USD')
with sidebar:
    st.title(body='Content')
    st.markdown('- **price** - Price in US dollars (326–18,823)')
    st.markdown('- **carat** - Weight of the diamond (0.2–5.01)')
    st.markdown('- **cut** - Quality of the cut (Fair, Good, Very Good, Premium, Ideal)')
    st.markdown('- **color** - Diamond color, from J (worst) to D (best)')
    st.markdown('- **clarity** - Measurement of how clear the diamond is (I1 (worst), SI2, SI1, VS2, VS1, VVS2, VVS1, IF (best))')
    st.markdown('- **size** - Volume of the diamond (x * y * z)')