import streamlit as st
import base64
import re

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
            background-size: contain;  /* Adjust to fit the image */
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
        .footer-icons img {{
            margin: 0 10px; /* Reduce spacing between icons */
            transition: transform 0.2s;
            animation: pulse 1.5s infinite ease-in-out;
        }}
        .footer-icons img:hover {{
            transform: scale(1.2);
        }}
        input[type="text"], input[type="password"] {{
            margin-bottom: 5px; /* Reduce spacing between input fields */
            transition: transform 0.2s ease;
            padding:15px;
        }}
        input[type="text"]:focus, input[type="password"]:focus {{
            transform: scale(1.05); /* Slightly enlarge input fields on focus */
            padding:15px;
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
        .invalid-input {{
            animation: shake 0.5s ease-in-out;
        }}

        /* Keyframes for animations */
        @keyframes fadeIn {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
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
        @keyframes pulse {{
            0% {{ transform: scale(1); opacity: 1; }}
            50% {{ transform: scale(1.1); opacity: 0.8; }}
            100% {{ transform: scale(1); opacity: 1; }}
        }}
        @keyframes shake {{
            0% {{ transform: translateX(0); }}
            25% {{ transform: translateX(-5px); }}
            50% {{ transform: translateX(5px); }}
            75% {{ transform: translateX(-5px); }}
            100% {{ transform: translateX(0); }}
        }}
        /* Dynamic Slide Animation for Sign-in/Sign-up */
        @keyframes slideIn {{
            0% {{ transform: translateX(100%); opacity: 0; }}
            100% {{ transform: translateX(0); opacity: 1; }}
        }}
        .sign-in-up-box {{
            animation: slideIn 1s ease-out;
        }}

        /* Border for the image */
        .custom-image {{
            width: 900px;  /* Custom width */
            height: 200px; /* Custom height */
            display: block;
            margin-left: auto;
            margin-right: auto;
            border: 3px solid black; /* Add border to the image */
            border-radius: 10px; /* Optional rounded corners for the border */
        }}
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Contact 📗 / Feedback 👍")
# Sidebar for Choose Your Action
action_choice = st.sidebar.selectbox(
    "Choose Your Action", 
    ["Feedback", "Contact Us"]
)

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zAZ0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email)

# Image path
image_path = r"C:\Users\DELL\OneDrive\Desktop\p\d.png"  # Correct image path

# Encode image to Base64
image_base64 = encode_image(image_path)

# Displaying the image at the top of the form with custom width and height using HTML
st.markdown(
    f"""
    <img src="data:image/png;base64,{image_base64}" class="custom-image"/>
    """,
    unsafe_allow_html=True,
)

# Depending on the choice in the sidebar, show different forms
if action_choice == "Feedback":
    with st.form(key="feedback_form"):
        # Basic information
        name = st.text_input("What is your name?")
        email = st.text_input("What is your email address?")
        
        # Product/Service rating
        rating = st.radio("How would you rate your experience with our service?", ["Excellent", "Good", "Average", "Poor"])
        
        # Suggestion/Comment
        suggestion = st.text_area("What do you think we can improve?")
        
        # Customer Satisfaction
        satisfaction = st.radio("How satisfied are you with our product/service?", ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"])
        
        # Future Improvements
        improvements = st.text_area("What features or services would you like to see in the future?")
        
        # Submit button
        submit_button = st.form_submit_button("Submit Feedback")
        
        if submit_button:
            # Handle form submission
            if not name or not email or not suggestion:
                st.error("Please fill in all required fields!")
            else:
                st.success("Thank you for your valuable feedback!")

elif action_choice == "Contact Us":
    with st.form(key="contact_form"):
        # Input fields for the form
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")

        # Initialize error message
        error_message = ""
        
        # Submit button
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            # Field validation
            if not name or not email or not message:
                error_message = "All fields are required!"
            elif not is_valid_email(email):
                error_message = "Please enter a valid email address."
            
            # If no errors, show success message, else show error
            if error_message:
                st.error(error_message)
            else:
                st.success("Thank you for your message!")
                # Optionally, save the form data to a database or send an email here.
                
                # Clear the form data
                st.session_state.name = ""
                st.session_state.email = ""
                st.session_state.message = ""  