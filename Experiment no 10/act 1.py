# -*- Create a Streamlit grocery bill calculator.
"""
Created on Tue Apr 21 10:49:24 2026

@author: RAJ MAGAR
"""

import streamlit as st

st.title("Grocery Bill Calculator")

# Inputs
item1 = st.number_input("Price of Item 1:", min_value=0)
item2 = st.number_input("Price of Item 2:", min_value=0)
item3 = st.number_input("Price of Item 3:", min_value=0)

# Button
if st.button("Calculate Total"):
    total = item1 + item2 + item3
    st.success("Total Bill Calculated!")

    st.write("Total Amount:", total)
