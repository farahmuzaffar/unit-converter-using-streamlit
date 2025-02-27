📏 Unit Converter App
A simple and interactive Unit Converter built using Streamlit. This app allows users to convert between different units of length, mass, and temperature with a visually appealing interface.

🚀 Features
Interactive Interface: Users can select the type of conversion they want to perform from a dropdown menu.

Multiple Conversions:

Length: Kilometers to Meters, Meters to Centimeters

Mass: Kilograms to Grams, Grams to Milligrams

Temperature: Celsius to Fahrenheit, Fahrenheit to Celsius

Visual Icons: Emojis are used to make the app more engaging and intuitive.

Real-Time Results: The converted value is displayed instantly in a success box.

🛠️ How to Run the App
Prerequisites
Python: Ensure Python 3.7 or higher is installed on your system.

Streamlit: Install Streamlit using pip if you don't have it already.

pip install streamlit
Steps to Run
Clone the repository or download the code file (hello.py).

Navigate to the directory where the code is saved.

Run the Streamlit app using the following command:


streamlit run hello.py
The app will open in your default web browser. You can now interact with the Unit Converter.

🖥️ App Interface
1. Title and Subheader
The app displays a title (📏 Unit Converter) and a subheader explaining its purpose.

2. Available Conversions
A list of available conversions is displayed with emojis for better visualization.

3. User Input
Users can:

Select the type of conversion from a dropdown menu.

Enter the value they want to convert.

4. Conversion Result
The converted value is displayed in a success box with the appropriate units and emojis.

📝 Code Overview
Key Components
Conversions Available:

A list of tuples stores the conversion options, including unit names and corresponding emojis.


conversions_available = [
    (1, "km", "m", "🌍", "📏"),
    (2, "m", "cm", "📏", "📐"),
    (3, "kg", "g", "⚖️", "🍎"),
    (4, "g", "mg", "🍎", "⚖️"),
    (5, "C", "F", "🌡️", "🔥"),
    (6, "F", "C", "🔥", "🌡️")
]
User Input:

st.selectbox: Allows users to select the conversion type.

st.number_input: Allows users to input the value to convert.

Conversion Logic:

Simple mathematical operations are used to perform the conversions.

Display Result:

The result is displayed using st.success() for a visually appealing output.

📸 Screenshots
Unit Converter App
Example of the app interface.

🤝 Contributing
Contributions are welcome! If you'd like to improve this project, feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a pull request.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙏 Acknowledgments
Built with ❤️ using Streamlit.

Emojis from Emoji Cheat Sheet.

Enjoy converting units with ease! 🎉
