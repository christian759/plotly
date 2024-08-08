import streamlit as st 
from methods import *
    
st.title("PLOTLY")
st.subheader("Plot interactive graph from equations")

st.markdown("blablablabla")
equation = st.text_input(label= "enter an equation, pls ensure it is entered in the right format like the above examples")

st.markdown("enter the range of values")

start_varable, end_varable = st.select_slider(
"select numbers between 1 to 10",
    options=[
        "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
    ],
    value=("1", "10"),
)
st.write("you selected numbers between", start_varable, "and", end_varable)

def iterate():
    numbers = list(i for i in range(int(start_varable), int(end_varable)+1))
    st.markdown(numbers)        
    
iterate()

st.feedback("stars")

