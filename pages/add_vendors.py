import streamlit as st
from database import add_vendor

PRODUCTS = [
    "Electronics",
    "Apparel",
    "Groceries",
    "Software",
    "Other"
]

def add_vendor_page():
    st.title("Add Vendor")
    with st.form("add_vendor_form"):
        vendor_id = st.text_input("Vendor ID")
        vendor_name = st.text_input("Vendor Name")
        category = st.multiselect("Category", options=PRODUCTS)
        years_in_business = st.slider("Years in Business", 0, 50, 5)
        contact = st.text_input("Contact")
        status = st.selectbox("Status", ["Active", "Inactive"])
        submit = st.form_submit_button("Add Vendor")
        
        if submit:
            try:
                add_vendor(int(vendor_id), vendor_name, category, years_in_business, contact, status)
                st.success("Vendor added successfully!")
            except Exception as e:
                st.error(f"Error: {e}")
