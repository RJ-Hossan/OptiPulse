import streamlit as st

def run():
    st.title("Collaborators")
    st.markdown("""
    ## Meet the Team
    Our project team consists of 15 collaborators, divided into 3 groups. Each group brings unique skills and expertise to the table.
    """)

    # Group 1
    st.subheader("Anomaly Detection")
    st.text("1. Sabik Aftahee (ID: 1904024)")
    st.text("2. Tareque MD Hanif (ID: 102)")
    st.text("3. Nure Hadi (ID: 103)")
    st.text("4. Mostak(ID: 104)")
    st.text("5. Alif Sheikh (ID: 105)")

    # Group 2
    st.subheader("Customer Satisfaction Analysis")
    st.text("1. Abu Md. Masbah Uddin (SID: 1904001)")
    st.text("2. Tofayel Ahmmed Babu (SID: 1904005)")
    st.text("3. Md. Refaj Hossan (SID: 1904007)")
    st.text("4. Zillur Rahman Zihad (SID: 1904028)")
    st.text("5. Mostak Mahmud (SID: 1904055)")

    # Group 3
    st.subheader("Customer Segementation")
    st.text("1. Nabiha Fiza (ID: 301)")
    st.text("2. Prithula saha (ID: 302)")
    st.text("3. Nowshin (ID: 303)")

    st.markdown("""
    Each collaborator has played a vital role in making this project a success. Thank you for your hard work and dedication!
    """)
