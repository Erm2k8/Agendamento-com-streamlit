import streamlit as st
from .client_ui import ClientUI
from .services_ui import ServicesUI
from .schedules_ui import SchedulesUI

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
        tab_list, tab_insert, tab_update, tab_delete = st.tabs(["List", "Insert", "Update", "Delete"])

        with tab_insert:
            ServicesUI.insert()

        with tab_list:
            ServicesUI.list()

        with tab_update:
            ServicesUI.update()

        with tab_delete:
            ServicesUI.delete()

        ServicesUI.hello_world()

    @classmethod
    def schedules(cls):
        tab_list, tab_insert, tab_update, tab_delete = st.tabs(["List", "Insert", "Update", "Delete"])

        with tab_insert:
            SchedulesUI.insert()

        with tab_list:  
            SchedulesUI.list()

        with tab_update:
            SchedulesUI.update()

        with tab_delete:
            SchedulesUI.delete()
            
        SchedulesUI.hello_world()

