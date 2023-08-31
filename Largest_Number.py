import streamlit as st
st.write("""
#Largest of Three Numbers
This app Outputs the largest out of 3 numbers         
""")
st.header("Numbers")
n1 = st.number_input("Number 1")
n2 = st.number_input("Number 2")
n3 = st.number_input("Number 3")
larger = (n1 if (n1 > n2 and n1 > n3) else
     (n2 if (n2 > n1 and n2 > n3) else n3))
st.header("Output")
out  =  "The largest of 3 numbers is : "+larger
st.write(out)
