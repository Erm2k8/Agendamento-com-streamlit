import streamlit as st
import pandas as pd
from time import sleep
from datetime import datetime, timedelta, time
from .views import View

class SchedulesUI:
    @classmethod
    def hello_world(cls):
        st.title("Schedules")

    @classmethod
    def list(cls):
        st.title("List Schedules")
        schedules = View.list_schedules()
        if schedules:
            df = pd.DataFrame(schedules)
            st.dataframe(df, hide_index=True, use_container_width=True)
        else:
            st.warning("No schedules available.")

    @classmethod
    def insert(cls):
        st.title("Insert Schedule")

        services = View.list_services()
        clients = View.list_clients()

        service_description = st.selectbox("Select Service", [s["description"] for s in services])
        client_name = st.selectbox("Select Client", [c["name"] for c in clients])

        service_data = next((s for s in services if s["description"] == service_description), None)
        client_data = next((c for c in clients if c["name"] == client_name), None)

        if service_data and client_data:
            start_time = cls.convert_to_time(service_data["start_time"])
            end_time = cls.convert_to_time(service_data["end_time"])
            duration = service_data["duration"]
            interval = service_data["interval"]

            available_times = cls.get_available_times(start_time, end_time, duration, interval)

            schedule_time = st.selectbox("Schedule Time", available_times)
            date = st.date_input("Date")
            confirmed = st.checkbox("Confirmed")

            submit = st.button("Insert")

            if submit:
                if service_description and date and schedule_time and client_name:
                    try:
                        schedule_datetime = datetime.combine(date, schedule_time)
                        View.insert_schedule({
                            "id": 0,
                            "service_id": service_data["id"],
                            "client_id": client_data["id"],
                            "date": date.isoformat(), 
                            "time": schedule_datetime.strftime("%H:%M:%S"),
                            "confirmed": confirmed
                        })
                        st.success("Schedule inserted successfully.")
                        sleep(2)
                        st.rerun()
                    except ValueError:
                        st.error("Invalid data.")
                else:
                    st.warning("All fields are required.")

    @classmethod
    def update(cls):
        st.title("Update Schedule")
        schedules = View.list_schedules()
        services = View.list_services()
        clients = View.list_clients()

        if not schedules:
            st.warning("No schedules available to update.")
            return

        with st.form("update_schedule", clear_on_submit=True):
            schedule_id = st.selectbox("Select Schedule", [s["id"] for s in schedules])
            selected_schedule = next((s for s in schedules if s["id"] == schedule_id), None)

            if selected_schedule:
                service_description = selected_schedule.get("service", "")
                client_name = selected_schedule.get("client", "")

                new_service = st.selectbox(
                    "New Service",
                    [s["description"] for s in services],
                    index=([s["description"] for s in services].index(service_description)
                            if service_description in [s["description"] for s in services]
                            else 0)
                )
                new_client = st.selectbox(
                    "New Client",
                    [c["name"] for c in clients],
                    index=([c["name"] for c in clients].index(client_name)
                            if client_name in [c["name"] for c in clients]
                            else 0)
                )

                new_date_str = selected_schedule.get("date")

                if new_date_str:
                    new_date_str = new_date_str.split('T')[0]
                    new_date = datetime.strptime(new_date_str, "%Y-%m-%d").date()
                else:
                    new_date = datetime.now().date()

                new_date = st.date_input("New Date", value=new_date)

                service_data = next((s for s in services if s["description"] == new_service), None)

                if service_data:
                    start_time = cls.convert_to_time(service_data["start_time"])
                    end_time = cls.convert_to_time(service_data["end_time"])
                    duration = service_data["duration"]
                    interval = service_data["interval"]
                    # print("AAAAAAAAAAAAAAAAAAAAAAAAA")
                    # print(new_service)
                    # print(start_time)
                    # print(end_time)
                    # print(duration)
                    # print(interval)
                    # available_times = cls.get_available_times(start_time, end_time, duration, interval)
                    # print(available_times)
                else:
                    available_times = []

                new_time = st.selectbox("Schedule Time", available_times)

                confirmed = st.checkbox("Confirmed", value=selected_schedule.get("confirmed", False))

                submit = st.form_submit_button("Update")

            if submit:
                if new_service and new_client and new_date and new_time:
                    try:
                        service_data = next((s for s in services if s["description"] == new_service), None)
                        client_data = next((c for c in clients if c["name"] == new_client), None)

                        if service_data and client_data:
                            View.update_schedule(schedule_id, {
                                "id": selected_schedule.get("id"),
                                "service_id": service_data["id"],
                                "client_id": client_data["id"],
                                "date": new_date.isoformat(),
                                "time": new_time.strftime("%H:%M:%S"),
                                "confirmed": confirmed
                            })
                            st.success("Schedule updated successfully.")
                            sleep(2)
                            st.rerun()
                        else:
                            st.error("Service or Client not found.")
                    except ValueError:
                        st.error("Invalid data.")
                else:
                    st.warning("All fields are required.")

    @classmethod
    def delete(cls):
        st.title("Delete Schedule")
        schedules = View.list_schedules()
        if schedules:
            with st.form("delete_schedule", clear_on_submit=True):
                schedule_id = st.selectbox("Select Schedule", [s["id"] for s in schedules])
                submit = st.form_submit_button("Delete")
                if submit:
                    try:
                        View.delete_schedule(schedule_id)
                        st.success("Schedule deleted successfully.")
                        sleep(2)
                        st.rerun()
                    except ValueError:
                        st.error("Invalid data.")
        else:
            st.warning("No schedules available to delete.")

    @classmethod
    def get_available_times(cls, start_time, end_time, duration, interval):
        available_times = []
        start_datetime = datetime.combine(datetime.today(), start_time)
        end_datetime = datetime.combine(datetime.today(), end_time)

        current_time = start_datetime

        while current_time + timedelta(minutes=duration) <= end_datetime:
            available_times.append(current_time.time())
            current_time += timedelta(minutes=interval)

        return available_times

    @classmethod
    def convert_to_time(cls, time_str):
        if isinstance(time_str, str):
            return time.fromisoformat(time_str)
        return time_str
