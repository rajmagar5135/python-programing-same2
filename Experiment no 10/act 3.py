# -*- create astudent result calculator app-*-
"""
Created on Tue Apr 21 10:55:13 2026

@author: RAJ MAGAR
"""
import streamlit as st

st.title("Student Result Calculator")

# Inputs
sub1 = st.number_input("Marks in Subject 1:", min_value=0, max_value=100)
sub2 = st.number_input("Marks in Subject 2:", min_value=0, max_value=100)
sub3 = st.number_input("Marks in Subject 3:", min_value=0, max_value=100)

# Button
if st.button("Calculate Result"):
    total = sub1 + sub2 + sub3
    percentage = total / 3

    st.success("Result Calculated!")

    st.write("Total Marks:", total)
    st.write("Percentage:", percentage)

    if percentage >= 75:
        st.write("Grade: Distinction")
    elif percentage >= 60:
        st.write("Grade: First Class")
    elif percentage >= 50:
        st.write("Grade: Second Class")
    elif percentage >= 35:
        st.write("Grade: Pass")
    else:
        st.write("Grade: Fail")

