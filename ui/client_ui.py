import streamlit as st
import pandas as pd
from .views import View

class ClientUI:
    @classmethod
    def insert(cls):
        st.title("Insert a Client")

    @classmethod
    def list_clients(cls):
        st.title("Listing Clients")

        clients_list = View.list_clients()
        
        dataframe = pd.DataFrame(clients_list)

        st.dataframe(
            data=dataframe,
            hide_index=True,
            use_container_width=True)

    @classmethod
    def update(cls):
        st.title("Update a Client")

    @classmethod
    def delete(cls):
        st.title("Delete a Client")
        