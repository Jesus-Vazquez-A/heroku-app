# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:40:08 2022

@author: PC SWAN PLUS
"""



import streamlit as st
import joblib
import numpy as np

st.cache(allow_output_mutation=True)

def UserInputs():
    

                                                    
    
    gender = st.radio('Gender',('Male','Female'))
    
    
    height = st.number_input('Height in inches',min_value = 56.39,max_value = 76.70)
    

       

    return gender,height


def preprocessing():
    
    gender,height = UserInputs()
    
    gender = np.where(gender == 'Male',1,0)
    
    new_data = [gender,height]
    
    return np.asarray([new_data])



st.cache(allow_output_mutation=True)


def predict(new_data):
    
    model = joblib.load("model.pkl")
    
    return model.predict(new_data)




st.cache(allow_output_mutation=True)

def main():
    
    st.subheader("""Predict Weight""")
    st.image("img.jpg")
  
    new_data = preprocessing()
    
    if st.button(label = 'Predict'):
        
        weight=predict(new_data)
        weight = np.round(weight,2)
        
        st.success(f'The estimated weight  is: $ {weight} pounds')


st.cache(allow_output_mutation=True)

if __name__ == '__main__':
    main()
