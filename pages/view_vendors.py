import streamlit as st
import pandas as pd
from database import get_all_vendors

def view_vendors():
    st.title("View Vendors")
    vendors = get_all_vendors()
    if vendors:
        vendors_df = pd.DataFrame(vendors, columns=["Vendor ID", "Vendor Name", "Category", "Years in business", "Contact", "Status"])
        # st.dataframe(vendors)
        st.dataframe(vendors_df)
    else:
        st.warning("No vendors found.")
