import streamlit as st
from database import init_db
from pages.home import home_page
from pages.view_vendors import view_vendors
from pages.add_vendors import add_vendor_page
from pages.update_status import update_vendor_status
from pages.upload_from_excel import upload_data

# Initialize database
init_db()

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home","Add Vendor", "Upload Vendor Data", "View Vendors", "Update Vendor Status"])

# Render pages based on sidebar selection
if page == "Home":
    home_page()
elif page == "Add Vendor":
    add_vendor_page()
elif page == "Upload Vendor Data":
    upload_data()        
elif page == "View Vendors":
    view_vendors()
elif page == "Update Vendor Status":
    update_vendor_status()
    
