import streamlit as st
import pandas as pd

class ClientUI:
    @classmethod
    def insert(cls):
        st.title("Insert")

    @classmethod
    def list_clients(cls):
        st.title("List")

    @classmethod
    def update(cls):
        st.title("Update")

    @classmethod
    def delete(cls):
        st.title("Delete")