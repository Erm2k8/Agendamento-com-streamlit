import streamlit as st
import pandas as pd
from time import sleep
from .views import View

class SchedulesUI:
    @classmethod
    def hello_world(cls):
        st.title("Schedules")

    @classmethod
    def open_schedules(self):
        st.title("Open Schedules")

        with st.form("open_schedule", clear_on_submit=True):
            start = st.time_input("Start Time")
            end = st.time_input("End Time")

        return 

    @classmethod
    def list(cls):
        st.title("List Schedules")

        schedules_list = View.list_schedules()

        if schedules_list:
            dataframe = pd.DataFrame(schedules_list)
            st.dataframe(data=dataframe, hide_index=True, use_container_width=True)
        else:
            st.warning("No schedules available.")

    @classmethod
    def insert(cls):
        st.title("Insert Schedules")

        with st.form("insert_schedule", clear_on_submit=True):
            service = st.selectbox("Select Service", [s["description"] for s in View.list_services()])
            client = st.selectbox("Select Client", [c["name"] for c in View.list_clients()])
            date = st.date_input("Date")
            schedule = st.time_input("Time")
            submit = st.form_submit_button("Insert")

            if submit:
                if service and client and date and schedule:
                    try:
                        View.insert_schedule({"service": service, "client": client, "date": date, "time": schedule})
                        st.success("Schedule Inserted")
                        sleep(2)
                        st.rerun()
                    except ValueError:
                        st.error("Invalid Data")
                else:
                    st.warning("All fields are required")

    @classmethod
    def update(cls):
        st.title("Update Schedules")

        schedules_list = View.list_schedules()
        if schedules_list:
            with st.form("update_schedule", clear_on_submit=True):
                schedule_id = st.selectbox("Select Schedule", [s["id"] for s in schedules_list])
                selected_schedule = next((s for s in schedules_list if s["id"] == schedule_id), None)
                new_service = st.selectbox("New Service", [s["description"] for s in View.list_services()], index=[s["description"] for s in View.list_services()].index(selected_schedule["service"]))
                new_client = st.selectbox("New Client", [c["name"] for c in View.list_clients()], index=[c["name"] for c in View.list_clients()].index(selected_schedule["client"]))
                new_date = st.date_input("New Date", value=selected_schedule["date"])
                new_time = st.time_input("New Time", value=selected_schedule["time"])
                submit = st.form_submit_button("Update")

                if submit:
                    if new_service and new_client and new_date and new_time:
                        try:
                            new_data = {"id": schedule_id, "service": new_service, "client": new_client, "date": new_date, "time": new_time}
                            View.update_schedule(schedule_id, new_data)
                            st.success("Schedule updated successfully")
                        except ValueError:
                            st.error("Invalid Data")
                    else:
                        st.warning("All fields are required")
        else:
            st.warning("No schedules available to update.")

    @classmethod
    def delete(cls):
        st.title("Delete Schedules")

        schedules_list = View.list_schedules()
        if schedules_list:
            with st.form("delete_schedule", clear_on_submit=True):
                schedule_id = st.selectbox("Select Schedule", [s["id"] for s in schedules_list])
                submit = st.form_submit_button("Delete")

                if submit:
                    try:
                        View.delete_schedule(schedule_id)
                        st.success("Schedule deleted successfully")
                        sleep(2)                    
                        st.rerun()
                    except ValueError:
                        st.error("Invalid Data")
        else:
            st.warning("No schedules available to delete.")
