import streamlit as st
import re


def formatter(equation: str, fig: int = 2) -> str:
    formatted = re.sub(r'(\d+)x', r'\1*x', equation)
    formatted = formatted.replace("^", "**")
    formatted = formatted.replace("x", str(fig))
    equals = eval(formatted)
    return equals

def result():
    ans = formatter(equation=equation)
    return ans

st.title("PLOTLY")
st.subheader("Plot interactive graph from equations")

st.markdown("blablablabla")
equation = st.text_input(label= "enter an equation, pls ensure it is entered in the right format like the above examples")

if equation:
    try:
        st.markdown(result())
    except Exception as e:
        st.markdown(e)

