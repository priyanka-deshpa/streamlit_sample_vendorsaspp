import sqlite3

# Initialize database
def init_db():
    conn = sqlite3.connect("vendors.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendors (
            vendor_id INTEGER PRIMARY KEY,
            vendor_name TEXT NOT NULL,
            category TEXT NOT NULL,
            years_in_business TEXT NOT NULL,
            contact TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Add a vendor
def add_vendor(vendor_id, vendor_name, category, years_in_business, contact, status):
    conn = sqlite3.connect("vendors.db")
    cursor = conn.cursor()
    category = ", ".join(category) if category else ""
    cursor.execute('''
        INSERT INTO vendors (vendor_id, vendor_name, category, years_in_business, contact, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (vendor_id, vendor_name, category, years_in_business, contact, status))
    conn.commit()
    conn.close()

# Get all vendors
def get_all_vendors():
    conn = sqlite3.connect("vendors.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vendors')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Update vendor status
def update_status(vendor_id, status):
    conn = sqlite3.connect("vendors.db")
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE vendors
        SET status = ?
        WHERE vendor_id = ?
    ''', (status, vendor_id))
    conn.commit()
    conn.close()

def add_vendors_bulk(vendor_list):
    conn = sqlite3.connect("vendors.db")
    cursor = conn.cursor()
    category = ", ".join(category) if category else ""
    cursor.executemany('''
        INSERT OR IGNORE INTO vendors (vendor_id, vendor_name, category, years_in_business, contact, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', vendor_list)
    conn.commit()
    conn.close()