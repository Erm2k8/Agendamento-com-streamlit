import streamlit as st
from .client_ui import ClientUI
from .services_ui import Services
from .schedules_ui import schedules_ui

class Index:
    @classmethod
    def clients(cls):
        tab_list, tab_insert, tab_update, tab_delete = st.tabs(["List", "Insert", "Update", "Delete"])

        with tab_insert:
            ClientUI.insert()

        with tab_list:
            ClientUI.list_clients()

        with tab_update:
            ClientUI.update()

        with tab_delete:
            ClientUI.delete()

    @classmethod
    def services(cls):
        Services.hello_world()

    @classmethod
    def schedules(cls):
        Schedules.hello_world()

