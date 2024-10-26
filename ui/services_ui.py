import streamlit as st
import pandas as pd
from time import sleep
from .views import View

class ServicesUI:
    @classmethod
    def hello_world(cls):
        st.title("Services")

    @classmethod
    def list(cls):
        st.title("List Services")

        services_list = View.list_services()
        if services_list:
            dataframe = pd.DataFrame(services_list)
            st.dataframe(data=dataframe, hide_index=True, use_container_width=True)
        else:
            st.warning("No services available.")

    @classmethod
    def insert(cls):
        st.title("Insert Services")

        with st.form("insert_service", clear_on_submit=True):
            description = st.text_input(label="Description")
            price = st.number_input(label="Price", min_value=0.0, step=0.01, format="%.2f")
            duration = st.number_input(label="Duration (minutes)", min_value=1, step=1)
            submit = st.form_submit_button("Insert")

            if submit:
                if description and price and duration:
                    try:
                        View.insert_service({"id": 0, "description": description, "price": price, "duration": duration})
                        st.success("Service Inserted")
                        sleep(2)
                        st.rerun()
                    except ValueError:
                        st.error("Invalid Data")
                else:
                    st.warning("All fields are required")
    
    @classmethod
    def update(cls):
        st.title("Update Services")

        services_list = View.list_services()
        if services_list:
            with st.form("update_service", clear_on_submit=True):
                service_name = st.selectbox("Select Service", [s["description"] for s in services_list])
                service_id = next((s for s in services_list if s["description"] == service_name), None)["id"]
                new_description = st.text_input(label="New Description")
                new_price = st.number_input(label="Price", min_value=0.0, step=0.01, format="%.2f")
                new_duration = st.number_input(label="New Duration (minutes)", min_value=1, step=1)
                submit = st.form_submit_button("Update")
                
                if submit:
                    if new_description and new_price and new_duration:
                        try:
                            new_data = {"id": service_id, "description": new_description, "price": new_price, "duration": new_duration}
                            View.update_service(service_id, new_data)
                            st.success("Service updated successfully")
                        except ValueError:
                            st.error("Invalid Data")
                    else:
                        st.warning("All fields are required")
        else:
            st.warning("No services available to update.")

    @classmethod
    def delete(cls):
        st.title("Delete Services")

        services_list = View.list_services()
        if services_list:
            with st.form("delete_service", clear_on_submit=True):
                service_name = st.selectbox("Select Service", [s["description"] for s in services_list])
                service_id = next((s for s in services_list if s["description"] == service_name), None)["id"]
                submit = st.form_submit_button("Delete")

                if submit:
                    try:
                        View.delete_service(service_id)
                        st.success("Service deleted successfully")
                        sleep(2)                    
                        st.rerun()
                    except ValueError:
                        st.error("Invalid Data")
        else:
            st.warning("No services available to delete.")
