import pandas as pd
import streamlit as st
from database import *
def update_ticketf():
    fti=st.text_input("Enter Flight Trip Id: ")
    result = view_flight_trip_i(fti)
    df1 = pd.DataFrame(result,columns=['Flight Trip ID','Depart Airport','Depart Time','Arrival Airport','Arrival Time','User Email','Distance','Amount','Currency'])
    st.dataframe(df1)
    result1 = view_traveller_id(fti)
    df2 = pd.DataFrame(result1,columns=['Flight Trip ID','Traveller ID','First Name','Last Name','Phone Number','Email id','Seat Number','Airplane Number'])
    st.dataframe(df2)
    if result1:
        fti1 = result1[0][0]
        tid = result1[0][1]
        result2 = view_traveller_iti(tid)
        first_name = result2[0][1]
        last_name = result2[0][2]
        phone = result2[0][3]
        email = result2[0][4]
        col1, col2 = st.columns(2)
        with col1:
            new_first_name = st.text_input("First Name: ",first_name)
            new_last_name = st.text_input("Last Name: ",last_name)
        with col2:
            new_phone = st.text_input("Phone: ",phone)
            new_email = st.text_input("email: ",email)
        if st.button("Update Details"):
            update_traveller(tid,new_first_name,new_last_name,new_phone,new_email)
            update_flight(fti1,new_email)
            st.success("Successfully Updated")