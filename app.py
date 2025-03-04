import streamlit as st

# Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="📏")

# Title
st.title("📏 Unit Converter")
st.write("""
Welcome to the Unit Converter! This app allows you to convert between different units of length, weight, and temperature.
""")

# Sidebar for Unit Selection
unit_type = st.sidebar.selectbox("Select the type of unit you want to convert:", ["Length", "Weight", "Temperature"])

# Length Converter
if unit_type == "Length":
    st.header("Length Converter")
    length_units = ["Meters", "Kilometers", "Feet", "Miles", "Inches"]
    from_length = st.selectbox("From:", length_units)
    to_length = st.selectbox("To:", length_units)
    length_value = st.number_input("Enter the value to convert:", min_value=0.0)

    if st.button("Convert Length"):
        # Conversion logic
        if from_length == "Meters":
            if to_length == "Kilometers":
                result = length_value / 1000
            elif to_length == "Feet":
                result = length_value * 3.28084
            elif to_length == "Miles":
                result = length_value * 0.000621371
            elif to_length == "Inches":
                result = length_value * 39.3701
            else:
                result = length_value
        elif from_length == "Kilometers":
            if to_length == "Meters":
                result = length_value * 1000
            elif to_length == "Feet":
                result = length_value * 3280.84
            elif to_length == "Miles":
                result = length_value * 0.621371
            elif to_length == "Inches":
                result = length_value * 39370.1
            else:
                result = length_value
        elif from_length == "Feet":
            if to_length == "Meters":
                result = length_value / 3.28084
            elif to_length == "Kilometers":
                result = length_value / 3280.84
            elif to_length == "Miles":
                result = length_value * 0.000189394
            elif to_length == "Inches":
                result = length_value * 12
            else:
                result = length_value
        elif from_length == "Miles":
            if to_length == "Meters":
                result = length_value * 1609.34
            elif to_length == "Kilometers":
                result = length_value * 1.60934
            elif to_length == "Feet":
                result = length_value * 5280
            elif to_length == "Inches":
                result = length_value * 63360
            else:
                result = length_value
        elif from_length == "Inches":
            if to_length == "Meters":
                result = length_value / 39.3701
            elif to_length == "Kilometers":
                result = length_value / 39370.1
            elif to_length == "Feet":
                result = length_value / 12
            elif to_length == "Miles":
                result = length_value / 63360
            else:
                result = length_value

        st.success(f"Converted Value: {result:.2f} {to_length}")

# Weight Converter
elif unit_type == "Weight":
    st.header("Weight Converter")
    weight_units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    from_weight = st.selectbox("From:", weight_units)
    to_weight = st.selectbox("To:", weight_units)
    weight_value = st.number_input("Enter the value to convert:", min_value=0.0)

    if st.button("Convert Weight"):
        # Conversion logic
        if from_weight == "Kilograms":
            if to_weight == "Grams":
                result = weight_value * 1000
            elif to_weight == "Pounds":
                result = weight_value * 2.20462
            elif to_weight == "Ounces":
                result = weight_value * 35.274
            else:
                result = weight_value
        elif from_weight == "Grams":
            if to_weight == "Kilograms":
                result = weight_value / 1000
            elif to_weight == "Pounds":
                result = weight_value * 0.00220462
            elif to_weight == "Ounces":
                result = weight_value * 0.035274
            else:
                result = weight_value
        elif from_weight == "Pounds":
            if to_weight == "Kilograms":
                result = weight_value * 0.453592
            elif to_weight == "Grams":
                result = weight_value * 453.592
            elif to_weight == "Ounces":
                result = weight_value * 16
            else:
                result = weight_value
        elif from_weight == "Ounces":
            if to_weight == "Kilograms":
                result = weight_value * 0.0283495
            elif to_weight == "Grams":
                result = weight_value * 28.3495
            elif to_weight == "Pounds":
                result = weight_value * 0.0625
            else:
                result = weight_value

        st.success(f"Converted Value: {result:.2f} {to_weight}")

# Temperature Converter
elif unit_type == "Temperature":
    st.header("Temperature Converter")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_temp = st.selectbox("From:", temp_units)
    to_temp = st.selectbox("To:", temp_units)
    temp_value = st.number_input("Enter the value to convert:")

    if st.button("Convert Temperature"):
        # Conversion logic
        if from_temp == "Celsius":
            if to_temp == "Fahrenheit":
                result = (temp_value * 9/5) + 32
            elif to_temp == "Kelvin":
                result = temp_value + 273.15
            else:
                result = temp_value
        elif from_temp == "Fahrenheit":
            if to_temp == "Celsius":
                result = (temp_value - 32) * 5/9
            elif to_temp == "Kelvin":
                result = (temp_value - 32) * 5/9 + 273.15
            else:
                result = temp_value
        elif from_temp == "Kelvin":
            if to_temp == "Celsius":
                result = temp_value - 273.15
            elif to_temp == "Fahrenheit":
                result = (temp_value - 273.15) * 9/5 + 32
            else:
                result = temp_value

        st.success(f"Converted Value: {result:.2f} {to_temp}")

# Signature at the Bottom
st.write("\n")
st.write("Created with ❤️ by **Kanwal Heer**.")