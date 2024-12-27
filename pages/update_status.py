import streamlit as st
from database import update_status, get_all_vendors

def update_vendor_status():
    st.title("Update Vendor Status")
    vendor_id = st.text_input("Enter Vendor ID")
    new_status = st.selectbox("New Status", ["Active", "Inactive"])
    if st.button("Update Status"):
        try:
            update_status(int(vendor_id), new_status)
            st.success("Status updated successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
