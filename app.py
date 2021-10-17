import streamlit as st
from pytezos import pytezos

pytezos = pytezos.using(shell = 'https://florencenet.smartpy.io', key='edskRxw1a6qfy3w3dsFyueoW9E6T1B5fqCVMfyTBGsGWPu1c7tukkM4s1gAoueebMy1HZA2jvSG8shtvQCaGEuDe3FgXH51LMu')
contract = pytezos.contract('KT1BdoSDUgkxzbAkwkTfQYzvjiK7s71rPogV')

def welcome():
    return "Welcome To Decentralised Medical Records"

def addPatientRecord():
  name = st.text_input("Enter your Full Name")
  PhoneNumber = st.number_input("Enter your Phone Number", step=1, min_value=1)
  age = st.number_input("Enter your Age", step=1, min_value=1)
  gender = st.text_input("Male/Female/Prefer Not Say")
  Hid = st.text_input("Enter your Health Id")
  Record=st.text_input("Enter the record details")


  if st.button("Register Now"):
    a = pytezos.using(shell = 'https://florencenet.smartpy.io', key='edskRxw1a6qfy3w3dsFyueoW9E6T1B5fqCVMfyTBGsGWPu1c7tukkM4s1gAoueebMy1HZA2jvSG8shtvQCaGEuDe3FgXH51LMu')
    contract = a.contract('KT1BdoSDUgkxzbAkwkTfQYzvjiK7s71rPogV')

    contract.addPatientRecord(age = age, gender = gender, name = name, PhoneNumber = PhoneNumber, Hid = Hid , Record=Record).with_amount(0).as_transaction().fill().sign().inject()   


def main():
    
    st.set_page_config(page_title="Decentralised Health Records")
   
    st.title("Blockchain Based Medical Records")
    st.markdown(
        """<div style="background-color:#e1f0fa;padding:10px">
                    <h1 style='text-align: center; color: #304189;font-family:Helvetica'><strong>
                    Vaccine For All</strong></h1></div><br>""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """<p style='text-align: center;font-family:Helvetica;'>
                   This project greatly decreases any chances of misuse of the vaccine. As Our country is facing a shortage of vaccine due to some unfaithful people who are responsible for lots of innocent deaths So to bring these malpractices to an end becomes our priority. We tried to help our nation by building a website that helps to track all the information of covid vaccine through blockchain technology.</p>""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """<h3 style='text-align: center; color: white; font-family:'Lato';font-family:Helvetica;'>
                   The proposed solution is going to help our nation overcome our vaccine shortage problem
by keeping all the information decentralized and available to all. #VaxForAll.
                   </h3>""",
        unsafe_allow_html=True,
    )

    st.sidebar.title("Choose your entry point")
    st.sidebar.markdown("Select the entry point accordingly:")

    algo = st.sidebar.selectbox(
        "Select the Option", options=[
          "Register Patient"
          ]
    )

    if algo == "Register Patient":
        addPatientRecord()
   
if __name__ == "__main__":
  main()
