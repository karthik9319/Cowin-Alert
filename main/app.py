import streamlit as st
import pandas as pd
import os
from utils import available_check, format_output


@st.cache
def data_loader():
    file_path = os.path.join(os.getcwd(), "data/district_mapping.csv")
    file_path = os.path.join(os.getcwd(), "data/Pincode_30052019.csv")
    data = pd.read_csv(file_path)
    data['District'] = data['District'].str.title()
    for column in data.columns:
        data[column] = data[column].astype(str)
    return data
    

df = data_loader()

numdays = st.sidebar.slider('Select Date Range', 0, 25, 5)

# state = st.sidebar.selectbox("State: ", sorted(df['state_name'].unique()))
state = st.sidebar.selectbox("State: ", sorted(df['StateName'].unique()))

# district_df = df[df['state_name']== state]
district_df = df[df['StateName']== state]
# district = st.sidebar.selectbox("District: ", sorted(district_df['district name'].unique()))
district = st.sidebar.selectbox("District: ", sorted(district_df['District'].unique()))

# district_id = df[df['district name'] == district]
division_df = df[df['District'] == district]
region = st.sidebar.selectbox("Region: ", sorted(division_df['Division Name'].unique()))

pincode_df = df[df['Division Name'] == region]
pincode = st.sidebar.selectbox("Pincode: ", sorted(pincode_df['Pincode'].unique()))

flag = st.selectbox("Show Only Availible Slots: ", [False, True])

output = available_check(numdays, pincode, flag)

new_output = format_output(output)




if isinstance(new_output, str):
    st.error(new_output)
else:
    st.dataframe(new_output)

# left_column_2, center_column_2, right_column_2, right_column_2a,  right_column_2b = st.beta_columns(5)
# st.write(output)
# st.table(new_output)
# st.dataframe(new_output)


# st.write(available_check(numdays, district_id))