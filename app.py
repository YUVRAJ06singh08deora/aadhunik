import streamlit as st
from pytezos import pytezos

pytezos = pytezos.using(shell = 'https://granadanet.smartpy.io', key='edskRn4MXH7DD9M9QiAKhKRNLCp4LU11iqEcNp6vSqNWB8qksLZckKgQZozdVuX4wum61fNwaesWjgtydm8f3h6NYggFAtPx4f')
contract = pytezos.contract('KT1RNQMAx4WcKXqAXHyLcKa8CvGFEfvc8E42')

def welcome():
    return "Welcome To Decentralised Medical Records"

def addPatientRecord():
  name = st.text_input("Enter Full Name of the Patient")
  PhoneNumber = st.number_input("Enter the Contact Number", step=1, min_value=1)
  age = st.number_input("Enter Age", step=1, min_value=1)
  gender = st.text_input("Enter Gender")
  Hid = st.text_input("Enter your Unique aadhar Id")
  Record=st.text_input("Enter the record details")


  if st.button("Register Patient"):
    a = pytezos.using(shell = 'https://granadanet.smartpy.io', key='edskRn4MXH7DD9M9QiAKhKRNLCp4LU11iqEcNp6vSqNWB8qksLZckKgQZozdVuX4wum61fNwaesWjgtydm8f3h6NYggFAtPx4f')
    contract = a.contract('KT1RNQMAx4WcKXqAXHyLcKa8CvGFEfvc8E42')

    contract.addPatientRecord(age = age, gender = gender, name = name, PhoneNumber = PhoneNumber, Hid = Hid , Record=Record).with_amount(0).as_transaction().fill().sign().inject()   

def ViewPatientRecord():
  Hid = st.text_input("Enter Unique aadhar Id of Patient")
  if st.button("View Records"):
    usds = pytezos.using(shell = 'https://granadanet.smartpy.io').contract('KT1RNQMAx4WcKXqAXHyLcKa8CvGFEfvc8E42')
    st.text(usds.storage[Hid]['Record']())
   
def main():
    
    st.set_page_config(page_title="Decentralised Health Records")
   
    st.title("Blockchain Based Medical Records")
    st.markdown(
        """<div style="background-color:#e1f0fa;padding:10px">
                    <h1 style='text-align: center; color: #304189;font-family:Helvetica'><strong>
                    Panjiyan</strong></h1></div><br>""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """<p style='text-align: center;font-family:Helvetica;'>
                   This project greatly decreases any chances of misuse or the manipulation of the medical Records</p>""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """<h3 style='text-align: center; color: white; font-family:'Lato';font-family:Helvetica;'>
                   The proposed solution is going to help our nation in decreasing the crime related to the data manipulation in Medical records for there own benefits. #VaxForAll.
                   </h3>""",
        unsafe_allow_html=True,
    )

    st.sidebar.title("Choose your entry point")
    st.sidebar.markdown("Select the entry point accordingly:")

    algo = st.sidebar.selectbox(
        "Select the Option", options=[
          "Register Patient",
          "View Patient Data"
          ]
    )

    if algo == "Register Patient":
        addPatientRecord()
    if algo == "View Patient Data":
        ViewPatientRecord()    
   
if __name__ == "__main__":
  main()
