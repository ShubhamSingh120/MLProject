import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Parkinsons Disease Prediction System', ['Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('Average vocal fundamental frequency')
        
    with col2:
        fhi = st.text_input('Maximum vocal fundamental frequency')
        
    with col3:
        flo = st.text_input('Manimum vocal fundamental frequency')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter measure(in %)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter measure(in Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:Relative Average Perturbation')
        
    with col2:
        PPQ = st.text_input('MDVP:Period Perturbation Quotient')
        
    with col3:
        DDP = st.text_input('Jitter:average absolute difference of differences between jitter cycles.')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB) variation in amplitude')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3 quotient of amplitude disturbance in 3 period')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5 quotient of amplitude disturbance in 5 period')
        
    with col3:
        APQ = st.text_input('MDVP:amplitude perturbation quotient')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA absolute differences between the amplitudes of consecutive periods')
        
    with col5:
        NHR = st.text_input('NHR (noise/harmonic ratio)')
        
    with col1:
        HNR = st.text_input('HNR (harmonic/noiseratio)')
        
    with col2:
        RPDE = st.text_input('RPDE (recurrence period density entropy)')
        
    with col3:
        DFA = st.text_input('DFA (Detrended fluctuation analysis)')
        
    with col4:
        spread1 = st.text_input('spread1 Dysphonic Voice Pattern Analysis')
        
    with col5:
        spread2 = st.text_input('spread2 Dysphonic Voice Pattern Analysis')
        
    with col1:
        D2 = st.text_input('D2 ("bass" vocal range )')
        
    with col2:
        PPE = st.text_input('PPE (Perceived phonatory effort)')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
















