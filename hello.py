import streamlit as st

# Title of the app with an icon
st.title("📏 Unit Converter: ")
st.subheader("Convert between different units of length, mass, and temperature.")

# Available conversions with icons
conversions_available = [
    (1, "km", "m", "🌍", "📏"),
    (2, "m", "cm", "📏", "📐"),
    (3, "kg", "g", "⚖️", "🍎"),
    (4, "g", "mg", "🍎", "⚖️"),
    (5, "C", "F", "🌡️", "🔥"),
    (6, "F", "C", "🔥", "🌡️")
]

# Display available conversions in a user-friendly way
st.markdown("### Available Conversions:")
for conversion_number, unit_from, unit_to, icon_from, icon_to in conversions_available:
    st.write(f"(Option {conversion_number}) {icon_from} **{unit_from}** ➡️ {icon_to} **{unit_to}**")

# User input for conversion choice
conversion = st.selectbox(
    "Select the conversion you want to perform:",
    options=[1, 2, 3, 4, 5, 6],
    format_func=lambda x: f"Option {x}"
)

# Get the selected conversion details
conversion_index = conversion - 1
conversion_number, unit_from, unit_to, icon_from, icon_to = conversions_available[conversion_index]

# User input for the value to convert
from_value = st.number_input(
    f"Enter the value in {icon_from} {unit_from}:",
    min_value=0.0,
    value=1.0
)

# Perform the conversion
if conversion_number == 1:
    to_value = from_value * 1000  # km to m
elif conversion_number == 2:
    to_value = from_value * 100  # m to cm
elif conversion_number == 3:
    to_value = from_value * 1000  # kg to g
elif conversion_number == 4:
    to_value = from_value * 1000  # g to mg
elif conversion_number == 5:
    to_value = (from_value * 1.8) + 32  # C to F
elif conversion_number == 6:
    to_value = (from_value - 32) / 1.8  # F to C

# Display the result in a visually appealing way
st.markdown("### Conversion Result:")
st.success(f"{icon_from} **{from_value} {unit_from}** ➡️ {icon_to} **{to_value:.2f} {unit_to}**")

    



