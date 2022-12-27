import pandas as pd
import streamlit as st
from database import *
def delete_ticketf():
    fti=st.text_input("Enter Flight Trip Id: ")
    result = view_flight_trip_i(fti)
    df1 = pd.DataFrame(result,columns=['Flight Trip ID','Depart Airport','Depart Time','Arrival Airport','Arrival Time','User Email','Distance','Amount','Currency'])
    st.dataframe(df1)
    result1 = view_traveller_id(fti)
    df2 = pd.DataFrame(result1,columns=['Flight Trip ID','Traveller ID','First Name','Last Name','Phone Number','Email id','Seat Number','Airplane Number'])
    st.dataframe(df2)
    st.write("Please confirm is this your following itinerary details:")
    if st.button("Confirm Cancelation"):
        delete_traveller(fti)
        delete_traveller_t(fti)
        delete_flight(fti)
        st.success("Cancelled Successfully")