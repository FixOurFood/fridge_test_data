import streamlit as st
import pandas as pd

data_url = 'https://docs.google.com/spreadsheets/d/e/' \
           + '2PACX-1vQgzBjOTgcTLekn38loPWBIZY82PDkEg349snHFnPVlmGJT'\
           + 'AH1tUZ98RFvvjugG8_sRNYI1nCgP7IOz'\
           + '/pub?gid=493561849&single=true&output=csv'

def get_fridge_data(pulses, alt, chicken, df):
    """Get fridge data based on user inputs."""
    filtered_df = df[
        (df['Eat more beans and lentils'] == f'{pulses}%') &
        (df['Eat more alternative meat and dairy'] == f'{alt}%') &
        (df['Eat more chicken'] == f'{chicken}%')
    ]

    result = {}

    if not filtered_df.empty:
        row = filtered_df.iloc[0]
        result = {
            'fridge top door': row['fridge top door'],
            'fridge top middle': row['fridge top middle'],
            'fridge top left': row['fridge top left'],
            'fridge middle left': row['fridge middle left'],
            'fridge bottom right': row['fridge bottom right'],
            'fridge middle right': row['fridge middle right'],

            'cupboard left': row['cupboard left'],
            'fridge top right': row['fridge top right'],
            'countertop': row['Countertop'],
        }

    return result

def fill_fridge(fridge_dict):

    cols = st.columns(3)

    with cols[0]:
        st.write(fridge_dict.get('fridge top left', 'No data'))
        st.write(fridge_dict.get('fridge middle left', 'No data'))
        st.write(fridge_dict.get('fridge bottom left', 'No data'))

    with cols[1]:
        st.write(fridge_dict.get('fridge top right', 'No data'))
        st.write(fridge_dict.get('fridge middle right', 'No data'))
        st.write(fridge_dict.get('fridge bottom right', 'No data'))

    with cols[2]:
        st.write(fridge_dict.get('fridge top door', 'No data'))
        st.write(fridge_dict.get('countertop', 'No data'))
        st.write(fridge_dict.get('cupboard left', 'No data'))

@st.cache_data(ttl=24*3600)
def get_fridge_csv(data_url=data_url):
    data = pd.read_csv(data_url, header=1, index_col=0)
    return data
