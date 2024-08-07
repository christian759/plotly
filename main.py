import streamlit as st
import re


def formatter(equation:str, fig = 2) -> str:
    pattern = r'(\d+)x'
    output_string = re.sub(pattern, r'\1*x', equation)
    formatted = output_string.replace("^", "**")
    formatted = formatted.replace("x", str(fig))
    equa = eval(formatted)
    return equa

st.title("PLOTLY")
st.subheader("Plot interactive graph from equations")

st.markdown("blablablabla")
equation = st.text_input(label= "enter an equation, pls ensure it is entered in the right format like the above examples")
def result():
    ans = formatter(equation=equation, fig=4)
    return ans

if equation:
    st.markdown(result())

