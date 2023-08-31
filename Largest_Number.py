import streamlit as st
st.header("Largest of 3 Numbers")
st.write("This app Outputs the largest out of 3 numbers")
st.subheader("Numbers")
n1 = st.number_input("Number 1")
n2 = st.number_input("Number 2")
n3 = st.number_input("Number 3")
larger = (n1 if (n1 > n2 and n1 > n3) else
     (n2 if (n2 > n1 and n2 > n3) else n3))
st.subheader("Output")
out  =  "The largest of 3 numbers is : "+str(larger)
st.write(out)
