import streamlit as st
import pandas as pd
from .views import View

class ClientUI:
    @classmethod
    def insert(cls):
        st.title("Clients Register")

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
        st.title("Clients Update")

        with st.form("update_client"):
            client_name = st.selectbox("Select Client", [c["name"] for c in View.list_clients()])
            client_id = next((c for c in View.list_clients() if c["name"] == client_name), None)["id"]

            new_name = st.text_input(label="New Name")
            new_email = st.text_input(label="New Email")
            new_phone = st.text_input(label="New Phone")
            submit = st.form_submit_button("Update")
            
            if submit:
                if new_name and new_email and new_phone:
                    try:
                        new_data = {"id": client_id, "name": new_name, "email": new_email, "phone": new_phone}

                        View.update_client(client_id, new_data)
                        
                        st.success("Client updated successfully")
                    except ValueError:
                        st.error(f"Invalid Data")
                else:
                    st.warning("All fields are required")

    @classmethod
    def delete(cls):
        st.title("Delete a Client")
        