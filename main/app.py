import streamlit as st
import pandas as pd
import os
from utils import available_check, format_output, filter_column
from copy import deepcopy
from layout import image, link, layout, footer


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def data_loader():
    file_path = os.path.join(os.getcwd(), "data/district_mapping.csv")
    file_path = os.path.join(os.getcwd(), "data/Pincode_30052019.csv")
    data = pd.read_csv(file_path)
    data['District'] = data['District'].str.title()
    for column in data.columns:
        data[column] = data[column].astype(str)
    return data
    

df = data_loader()

numdays = st.sidebar.slider('Select Date Range', 0, 7, 2)

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

# flag = st.selectbox("Show Only Availible Slots: ", [False, True]

output = available_check(numdays, pincode)

if type(output) != list:
    st.error("Sorry CO Win API limit reached")
else:
    new_output = format_output(output)




if isinstance(new_output, str):
    st.error(new_output)

else:
    # filter = st.checkbox('Filter')
    # if filter:
    left_column_1, center_column_1, right_column_1, right_column_2 = st.beta_columns(4)
    
    # with left_column_1:
    #     flag = st.selectbox("Vaccine Type: ",[""] + ["COVISHIELD", "COVAXIN"])
    #     print(flag)
    #     if flag != "":
    #         print(type(new_output['Vaccine Type'][1]))
    #         # final_df = new_output[new_output['Vaccine Type'] == flag]
    #         final_df = filter_column(new_output, "Vaccine Type", flag)
    
    
    # with center_column_1:
    #     vals = ['Free', 'Paid']
    #     fee_type = st.selectbox("Show Fee Type: ", vals ) 
    #     if fee_type != "":
    #         final_df = new_output[new_output['Fee Type'] == fee_type]
    #         # final_df = filter_column(new_output, "Fee Type", fee_type)
            
    with right_column_1:
        valid_capacity = ["", "Available"]
        cap_inp = st.selectbox('Select Availablilty', [""] + valid_capacity)
        if cap_inp != "": 
            final_df = new_output[new_output['Available Capacity'] > 0]
            
    # with right_column_2:
    #     min_age = ["", "18", "45"]
    #     ages = st.selectbox("Select Age Group: ", min_age)
    #     if min_age!= "":
    #         final_df = new_output[new_output['Minimum Age Limit'] == ages]
        
    # else:
    #     final_df = new_output
    table = deepcopy(final_df)
    st.table(table)
    # st.beta_set_page_config(layout="wide")


