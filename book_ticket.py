import pandas as pd
import streamlit as st
import random 
from database import *
from st_aggrid import *
import altair as alt
def book_ticketf():
    row1,row2 =st.columns(2)
    row3,row4 = st.columns(2)
    with row1:
        fname = st.text_input("Enter First Name: ",)
        lname = st.text_input("Enter Last Name: ",)  
    with row2:
        phone = st.text_input("Enter Phone Number: ",)
        email= st.text_input("Enter Email ID: ",)
    locations = ['Charlotte','Dallas','Los Angels','Raleigh']
    with row3:
        From = st.selectbox("Select location of Departure: ",locations)
    with row4:
        To = st.selectbox("Select location of Arrival: ",locations)    
    seat_types=["BUSINESS","ECONOMY"]
    if From != To:
        From = str(From)
        To = str(To)
        planes = view_planes(From,To)
        list_of_planes1= [i[0] for i in planes]
        if From=="Raleigh" or To=="Raleigh":
            p1=get_airplane_time_rdu(list_of_planes1,From,To)
        else:
            p1=get_airplane_time(list_of_planes1,From,To)
        p2= pd.DataFrame(p1,columns=['Airplane Number','Departure Airport','Arrival Airport','Departure Time','Arrival Time','Distance'])
        st.dataframe(p2)
        list_of_planes2=[i[0] for i in p1]
        plane=st.selectbox("Select Available Planes: ",list_of_planes2)
        selected_plane = get_airplane_time_i(plane,From,To)
        p4= pd.DataFrame(selected_plane,columns=['Airplane Number','Departure Airport','Arrival Airport','Departure Time','Arrival Time','Distance'])
        st.dataframe(p4)
        seat_type=st.selectbox("Select Seat Class: ",seat_types)
        depart_time=selected_plane[0][3]
        arrival_time=selected_plane[0][4]
        no_of_yes_seats = no_of_seat_yes(plane,depart_time,arrival_time)
        noys = no_of_yes_seats[0][0]
        no_of_no_seats = no_of_seat_no(plane,depart_time,arrival_time)
        nons = no_of_no_seats[0][0]
        st.write("Number of seats available: ",noys)
        st.write("Number of already booked: ",nons)
        noys=int(noys)
        nons=int(nons)
        source = pd.DataFrame({
        'Number of Seats': [noys,nons],
        'Booked': ['Yes','No']
        })
        bar_chart = alt.Chart(source).mark_bar().encode(
        y='Number of Seats:Q',
        x='Booked:O',
        )
        st.altair_chart(bar_chart, use_container_width=True)
        seats = [i[0] for i in view_seats(plane,seat_type,depart_time,arrival_time)]
        seat = st.selectbox("Select Seat: ",seats)
        if st.button("Book Ticket"):
            add_traveller(fname,lname,phone,email)
            flight_trip_id=fname[0:3]+phone[6:]+From+To
            depart_airport=selected_plane[0][1]
            arrival_airport=selected_plane[0][2]
            distance=selected_plane[0][5]
            idi=get_id(fname,lname,phone,email)
            add_flight_trip(flight_trip_id,depart_airport,depart_time,arrival_airport,arrival_time,email,distance)
            idi=idi[0][0]
            add_flight_trip_i(flight_trip_id,idi,seat,plane)
            st.success("Booked Successfully")
    else:
        st.write("The Arrival and Departure Locations are Same")