import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Welcome Back!", layout="wide")

# Function to encode image to Base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Encode background image
background_base64 = encode_image("C:\\Users\\DELL\\OneDrive\\Desktop\\p\\b.jpg")  # Correct image path

# Add custom CSS for background image, layout, and styling with animations
st.markdown(
    f"""
    <style>
        ::-webkit-scrollbar {{
            display: none; /* Hide scrollbar for webkit browsers */
        }}
        body {{
            background-image: url("data:image/png;base64,{background_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            margin: 0;
            padding: 0;
            height: 100vh;
            overflow: hidden; /* Disable body scrolling */
            animation: fadeIn 1s ease-in-out;
        }}
        .stApp {{
            position: absolute;
            top: 50%;
            left: 10%;
            transform: translateY(-50%);
            max-width: 1200px;
            height: 700px; /* Adjust height */
            background: rgba(211, 211, 211, 0.6);
            padding: 5px; /* Reduce padding */
            border-radius: 8px; /* Slightly smaller border radius */
            border: 1px solid #ccc;
            box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.2);
            overflow: hidden; /* Disable scrolling for the container */
            animation: slideUp 1s ease-out;
        }}
        h1, h2, h3, h4, h5, h6 {{
            margin-top: 10px; /* Reduce top margins for headings */
            margin-bottom: 10px; /* Reduce bottom margins for headings */
            animation: fadeInText 2s ease-in-out;
        }}
        button {{
            margin-top: 10px; /* Reduce spacing above buttons */
            transition: background-color 0.3s ease, transform 0.2s ease;
        }}
        button:hover {{
            background-color: #4CAF50;
            color: white;
            animation: bounce 0.5s ease-out;
        }}
        /* Keyframes for animations */
        @keyframes fadeIn {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        @keyframes slideUp {{
            0% {{ transform: translateY(100%); }}
            100% {{ transform: translateY(0); }}
        }}
        @keyframes fadeInText {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        @keyframes bounce {{
            0% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0); }}
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Power BI Embed
st.title("Dashboard")

# Power BI Embed URL
power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=a7da3ab4-9275-404c-9114-b60f1c297297&autoAuth=true&ctid=7402bea1-1360-40f4-8265-f62014f87ab5"

# Iframe with border and animation
iframe_code = f"""
<div style="position: relative; height: 0; padding-bottom: 56.25%; overflow: hidden; max-width: 100%; height: auto; animation: fadeIn 1.5s ease-in-out;">
    <iframe
        src="{power_bi_url}"
        frameborder="0"
        style="position: absolute; width: 100%; height: 100%; border: 3px solid black; border-radius: 10px; box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);"
        allowFullScreen="true">
    </iframe>
</div>

<style>
    @keyframes fadeIn {{
        0% {{ opacity: 0; transform: scale(0.9); }}
        100% {{ opacity: 1; transform: scale(1); }}
    }}
</style>
"""

# Display the responsive iframe
st.markdown(iframe_code, unsafe_allow_html=True)

# Add links in sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("### Dashboard Links")
# Links for Dashboard1 and Dashboard2
st.sidebar.page_link("pages/Dashboard1.py", label="Dashboard of Superstore Sales", icon="1️⃣")
st.sidebar.page_link("pages/Dashboard2.py", label="Create a Dashboard", icon="➕")
