import streamlit as st
import pandas as pd
from time import sleep
from .views import View

class SchedulesUI:
    @classmethod
    def hello_world(cls):
        st.title("Schedules")

    @classmethod
    def list(cls):
        st.title("List Schedules")

        schedules_list = View.list_schedules()

        dataframe = pd.DataFrame(schedules_list)
        st.dataframe(
            data=dataframe,
            hide_index=True,
            use_container_width=True
        )

    @classmethod
    def insert(cls):
        st.title("Insert Schedules")

        with st.form("insert_schedule", clear_on_submit=True):
            service = st.selectbox("Select Service", [s["name"] for s in View.list_services()])
            client = st.selectbox("Select Client", [c["name"] for c in View.list_clients()])
            date = st.date_input("Schedule")
            schedule = st.time_input("Schedule")
            submit = st.form_submit_button("Insert")

            

    @classmethod
    def update(cls):
        st.title("Update Schedules")

    @classmethod
    def delete(cls):
        st.title("Delete Schedules")