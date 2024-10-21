import streamlit as st
from .client_ui import ClientUI

def index():
    tab_list, tab_insert, tab_update, tab_delete = st.tabs(["List", "Insert", "Update", "Delete"])

    with tab_insert:
        ClientUI.insert()

    with tab_list:
        ClientUI.list_clients()

    with tab_update:
        ClientUI.update()

    with tab_delete:
        ClientUI.delete()