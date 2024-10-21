import streamlit as st
import pandas as pd
from .views import View

class ClientUI:
    @classmethod
    def insert(cls):
        st.title("Insert a Client")

        with st.form("insert_client"):
            name = st.text_input(label="Name")
            email = st.text_input(label="Email")
            phone = st.text_input(label="Phone")
            submit = st.form_submit_button("Insert")

            if name and email and phone:
                if submit:
                    try:                        
                        View.insert_client({"id": 0,"name": name, "email": email, "phone": phone})
                        st.success("Client inserted successfully")
                    except ValueError:
                        st.error(f"Invalid Data")
            else:
                st.warning("All fields are required")

            


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

        with st.form("update_client"):
            st.form_submit_button("Update")

    @classmethod
    def delete(cls):
        st.title("Delete a Client")
        