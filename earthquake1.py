
import streamlit as st
import pickle 

st.title("EARTHQUAKE PREDICTION ")
Latitude = st.number_input('Latitude')
Longitude = st.number_input('Longitude')
Type = st.radio('Type', [0, 1])

clicked = st.button("Get Prediction")

# Load the model
with open('rfc.dat', 'rb') as f:
    model = pickle.load(f)

if clicked:
    data = [Latitude, Longitude]
    # Make prediction
    pred = model.predict([data])

    # Display results
    st.header("MAGNITUDE")
    st.subheader(pred[0][0])
    st.header("DEPTH")
    st.subheader(pred[0][1])

    # Plotting the results
    st.header("Prediction Visualization")
    st.bar_chart(pred[0])

