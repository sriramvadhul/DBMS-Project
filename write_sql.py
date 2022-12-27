import streamlit as st
import pandas as pd
from database import exec_custom_query

def write_sqlf():
    query = st.text_input("Enter SQL Query to execute:")
    if st.button("Execute"):
        res = exec_custom_query(query)
        st.success("Successfully executed the query!")
        if res:
            st.write("Query Result : ")
            st.dataframe(res)