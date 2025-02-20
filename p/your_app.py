import streamlit as st
import base64
import sqlite3

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
            max-width: 550px;
            height: 500px; /* Adjust height */
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
    </style>
    """,
    unsafe_allow_html=True,
)

# Connect to SQLite database
def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT UNIQUE,
                    password TEXT
                )''')
    conn.commit()
    conn.close()

# Functions for login and registration
def login_user(email, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = c.fetchone()
    conn.close()
    if user:
        return True
    return False

def register_user(name, email, password, confirm_password):
    if password != confirm_password:
        return "Passwords do not match!"
    
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (name, email, password))
        conn.commit()
        conn.close()
        return f"User {name} registered successfully!"
    except sqlite3.IntegrityError:
        conn.close()
        return "Email already registered."

def reset_password(email):
    # Simulate password reset
    return f"Password reset link sent to {email}"

# UI Content
st.title("Welcome Back!")

# Tabs for Login and Registration
tabs = st.tabs(["Login", "Register"])

# Login tab
with tabs[0]:
    st.header("Sign In")
    email = st.text_input("Email Address", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    
    if st.button("Sign In"):
        if login_user(email, password):
            st.success("Logged in successfully!")
            st.page_link("pages/Home.py", label="Home", icon="🏠")
        else:
            st.error("Invalid email or password.")
            st.markdown('<style>.stError{background-color: #F8D7DA;}</style>', unsafe_allow_html=True)

    # Forgot password link
    if st.button("Forgot Password"):
        reset_email = st.text_input("Enter your email address for password reset:")
        if reset_email:
            reset_message = reset_password(reset_email)
            st.info(reset_message)

# Registration tab
with tabs[1]:
    st.header("Sign Up")
    name = st.text_input("Name", key="register_name")
    reg_email = st.text_input("Email Address", key="register_email")
    reg_password = st.text_input("Password", type="password", key="register_password")
    confirm_password = st.text_input(
        "Confirm Password", type="password", key="register_confirm_password"
    )
    if st.button("Sign Up"):
        response = register_user(name, reg_email, reg_password, confirm_password)
        if "successfully" in response:
            st.success(response)
        else:
            st.error(response)

# Footer with social media links
st.markdown(
    """
    <div style="text-align: center; margin-top: 30px;">
        <p>Connect with us:</p>
        <div class="footer-icons">
            <a href="https://facebook.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/128/5968/5968764.png" width="30">
            </a>
            <a href="https://twitter.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/128/3670/3670151.png" width="30">
            </a>
            <a href="https://linkedin.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/128/145/145807.png" width="30">
            </a>
            <a href="https://instagram.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/128/15707/15707749.png" width="30">
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Initialize the database
create_table()
# Define the pages


