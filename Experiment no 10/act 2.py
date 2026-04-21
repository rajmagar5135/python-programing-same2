# -*- create a BMI heaith checker app-*-
"""
Created on Tue Apr 21 10:52:25 2026

@author: RAJ MAGAR
"""

import streamlit as st

st.title("BMI Health Checker")

# Inputs
weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (meters):", min_value=0.1)

# Button
if st.button("Check BMI"):
    bmi = weight / (height ** 2)
    st.success("BMI Calculated!")

    st.write("Your BMI is:", round(bmi, 2))

    if bmi < 18.5:
        st.write("Status: Underweight")
    elif bmi < 25:
        st.write("Status: Normal")
    elif bmi < 30:
        st.write("Status: Overweight")
    else:
        st.write("Status: Obese")
