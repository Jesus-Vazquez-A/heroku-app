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
    
    
    height = st.number_input('Mileage',min_value = 56.39,max_value = 76.70)
    

       

    return gender,height


def preprocessing():
    
    gender,height = UserInputs()
    
    gender = np.where(gender == 'Male',1,0)
    
    return np.asarray([gender,height])



st.cache(allow_output_mutation=True)


def predict(new_data):
    
    model = joblib.dump("model.pkl")
    
    return model.predict(new_data)




st.cache(allow_output_mutation=True)

def main():
    
    st.subheader("""Predict Weight""")
    st.image("img.jpeg")
  
    new_data = preprocessing()
    
    if st.button(label = 'Predict'):
        
        weight=predict(new_data)
        st.success(f'The estimated weight  is: $ {weight} pounds')


st.cache(allow_output_mutation=True)

if __name__ == '__main__':
    main()