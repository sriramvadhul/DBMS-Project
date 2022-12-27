import pandas as pd
import streamlit as st
from database import *

def read_airplane():
    lists=['Airline Companies','Airplanes','Airports','Plane Port Access']
    selected_table=st.selectbox("Select to view",lists)
    with st.expander("View Selected"):
        if selected_table == 'Airline Companies':
            view_airline_company_app()
        elif selected_table == 'Airplanes':
            view_airplane_app()
        elif selected_table == 'Airports':
            view_airport_app()
        elif selected_table == 'Plane Port Access':
            view_port_access_app()
def read_traveller():
    list_t=['Traveller Details','Traveller Itinerary','Traveller Flight Ticket Details']
    selected_t=st.selectbox("Select to view",list_t)
    with st.expander("View Selected"):
        if selected_t == 'Traveller Details':
            view_traveller_app()
        elif selected_t == 'Traveller Itinerary':
            view_traveller_i_app()
        elif selected_t == 'Traveller Flight Ticket Details':
            view_flight_trip_app()
def show_tables_app():
    result1 = show_tables()
    df1 = pd.DataFrame(result1,columns=['Tables Present'])
    st.dataframe(df1)
def  view_airline_company_app():
    result2 = view_airline_company()
    df2 = pd.DataFrame(result2,columns=['Company ID','Company Name'])
    st.dataframe(df2)
def  view_airplane_app():
    result3 = view_airplane()
    df3 = pd.DataFrame(result3,columns=['Airplane No','Seating Capacity','Company'])
    st.dataframe(df3)
def  view_airport_app():
    result4 = view_airport()
    df4 = pd.DataFrame(result4,columns=['Airport Code','Airport Name','Location','City','Airport State','Country','Zip Code'])
    st.dataframe(df4)
def view_traveller_app():
    result5 = view_traveller()
    df5 = pd.DataFrame(result5,columns=['Traveller ID','First Name','Last Name','Phone','Email ID'])
    st.dataframe(df5)
def view_traveller_i_app():
    result6 = view_traveller_i()
    df6 = pd.DataFrame(result6,columns=['Flight Trip ID','Traveller ID','Seat Number','Airplane Number'])
    st.dataframe(df6)
def view_port_access_app():
    result7 = view_port_access()
    df7 = pd.DataFrame(result7,columns=['Airport','Airplane Number'])
    st.dataframe(df7)
def view_flight_trip_app():
    result8 = view_flight_trip()
    df8 = pd.DataFrame(result8,columns=['Flight Trip ID','Depart Airport','Depart Time','Arrival Airport','Arrival Time','User Email','Distance','Amount','Currency'])
    st.dataframe(df8)

