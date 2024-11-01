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
    
def tests():
    from hashlib import sha256 as makehash

    password = makehash("senha".encode()).hexdigest()

    print(password) #b7e94be513e96e8c45cd23d162275e5a12ebde9100a425c4ebcdd7fa4dcd897c

if __name__ == '__main__':
    main()
    # tests()