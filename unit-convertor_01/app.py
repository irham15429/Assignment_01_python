import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔁", layout="centered")

st.title("🔁 Google-Style Unit Converter")
st.markdown("Convert between various units just like Google does!")

# Define conversion logic
def convert_length(value, from_unit, to_unit):
    factors = {
        "Meter": 1,
        "Kilometer": 1000,
        "Centimeter": 0.01,
        "Millimeter": 0.001,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    factors = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }
    return value * factors[from_unit] / factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15)
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15)
    if from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32)

def convert_volume(value, from_unit, to_unit):
    factors = {
        "Liter": 1,
        "Milliliter": 0.001,
        "Gallon (US)": 3.78541,
        "Quart (US)": 0.946353,
        "Pint (US)": 0.473176,
        "Cup (US)": 0.24
    }
    return value * factors[from_unit] / factors[to_unit]

# Unit options
categories = {
    "Length": list(convert_length.__annotations__.keys()) or [],
    "Weight": list(convert_weight.__annotations__.keys()) or [],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Volume": list(convert_volume.__annotations__.keys()) or []
}

# UI
category = st.selectbox("Choose category", list(categories.keys()))

units = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Volume": ["Liter", "Milliliter", "Gallon (US)", "Quart (US)", "Pint (US)", "Cup (US)"]
}

from_unit = st.selectbox("From", units[category])
to_unit = st.selectbox("To", units[category])
value = st.number_input("Enter value to convert", value=0.0)

if st.button("Convert"):
    if category == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif category == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif category == "Volume":
        result = convert_volume(value, from_unit, to_unit)
    else:
        result = "Unsupported conversion."

    st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
