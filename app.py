import mysql.connector
import streamlit as st

from read import *
from book_ticket import *
from delete_ticket import *
from update_ticket import *
from write_sql import *

def main():
    st.title("Airline Reservation System App")
    menu = ["Airline Details","Book Airplane Ticket","Traveller Details","Cancel Airplane Ticket","Update Ticket Details","Write Custom SQL","View Tables"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Airline Details":
        st.subheader("View Airline Details: ")
        read_airplane()  
    
    elif choice == "Traveller Details":
        st.subheader("View Traveller Details: ")
        read_traveller()
    
    elif choice == "Book Airplane Ticket":
        st.subheader("Book Airplane Ticket")
        book_ticketf()

    elif choice == "Cancel Airplane Ticket":
        st.subheader("Cancel Airplane Ticket")
        delete_ticketf()
    
    elif choice == "Update Ticket Details":
        st.subheader("Update Name/ Phone number/ email id")
        update_ticketf()

    elif choice == "View Tables":
        show_tables_app()
    
    elif choice == "Write Custom SQL":
        st.subheader("Write Custom SQL Query")
        write_sqlf()

    else:
        st.subheader("About tasks")

if __name__ == '__main__':
    main()