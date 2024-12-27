import streamlit as st
import pandas as pd
from database import add_vendors_bulk

def upload_data():
    st.title("Upload Vendor Data")
    st.write("Upload an Excel file to add multiple vendors to the database.")

    # File uploader
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])
    
    if uploaded_file is not None:
        try:
            # Debugging file metadata
            st.write(f"File name: {uploaded_file.name}")
            st.write(f"File type: {uploaded_file.type}")
            st.write(f"File size: {uploaded_file.size} bytes")
            # Read the uploaded Excel file into a DataFrame
            df = pd.read_excel(uploaded_file)
            st.success("File uploaded successfully!")
            
            # Check if required columns are present
            required_columns = ["Vendor ID", "Vendor Name", "Category", "Years in business","Contact", "Status"]
            if not all(col in df.columns for col in required_columns):
                st.error(f"The uploaded file must contain the following columns: {', '.join(required_columns)}")
                return
            
            # Convert DataFrame to a list of tuples for database insertion
            vendor_list = df[required_columns].values.tolist()
            
            # Add vendors to the database
            add_vendors_bulk(vendor_list)
            st.success(f"Successfully added {len(vendor_list)} vendors to the database!")
        except Exception as e:
            st.error(f"Error reading the Excel file: {e}")
        except Exception as e:
            st.error(f"Error processing the file: {e}")
