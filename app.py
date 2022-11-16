import streamlit as st
import pandas as pd
import numpy as np

st.write('Welcome to my app')

location = st.text_input('Pick Up Location', 'Empire State')

st.write('The current location is', location)

@st.cache
def get_line_chart_data():

    return pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )

df = get_line_chart_data()

st.line_chart(df)