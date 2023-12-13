import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

st.title('Find the Largest Number')

st.write('Enter three numbers to find the largest among them.')

# Input fields for the numbers
number1 = st.number_input('Enter first number', 0.0)
number2 = st.number_input('Enter second number', 0.0)
number3 = st.number_input('Enter third number', 0.0)

if st.button('Find Largest Number'):
    largest = find_largest_number(number1, number2, number3)
    st.write(f'The largest number is: {largest}')
