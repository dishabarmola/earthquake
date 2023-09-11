import streamlit as st
import pickle 






st.title("EARTHQUAKE PREDICTION ")
Latitude=st.number_input('Latitude')
Longitude=st.number_input('Longitude')
Type=st.radio('Type',[0,1])



clicked=st.button("Get Prediction")

#model = pickle.load(open('rfcc.dat', 'rb'))
with open ('rfc.dat','rb') as f:
   model= pickle.load(f)
  
    



if clicked ==True:
    
    data=[Latitude,Longitude]
    print(data)
    
    pred=model.predict([data])
    print(pred)
    st.header("MAGNITUDE")
    st.subheader(pred[0][0])
    print(pred[0][0])
    st.header("DEPTH")
    st.subheader(pred[0][1])
    print(pred[0][1])
    
  
    

  

