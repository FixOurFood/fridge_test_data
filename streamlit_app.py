import streamlit as st
import pandas as pd
from utils import get_fridge_data, fill_fridge, get_fridge_csv

# Create two columns
col1, col2 = st.columns([1,2])

# First column with sliders
with col1:

    if st.button("Reset sliders"):
        st.session_state['pulses'] = 0
        st.session_state['alt'] = 0
        st.session_state['chicken'] = 0

    if st.button("Clear data cache"):
        get_fridge_csv.clear()

    pulses = st.select_slider(
        "Pulses",
        options=[0, 33, 50, 100],
    )
    
    alt = st.select_slider(
        "Alt meat",
        options=[0, 33, 50, 100],
    )
    
    chicken = st.select_slider(
        "Chicken",
        options=[0, 33, 50, 100],
    )

    st.write(f"Total beef and dairy reduction: {pulses+alt+chicken}%")

# Second column (empty for now)
with col2:
    data = get_fridge_csv()
    fridge_contents = get_fridge_data(pulses, alt, chicken, data)
    fill_fridge(fridge_contents)
    