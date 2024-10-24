from ui.index import Index
import streamlit as st

st.set_page_config(
    page_title="Clients",
    page_icon="👥"
)

def main():
    st.sidebar.title("Page")
    page = st.sidebar.selectbox("Select the page", ["Clients", "Schedules", "Services"])
    
    if page == "Clients":
        Index.clients()
    elif page == "Schedules":
        Index.schedules()
    elif page == "Services":
        Index.services()

if __name__ == '__main__':
    main()