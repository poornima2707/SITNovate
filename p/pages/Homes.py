import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="Superstore Sales: Interactive Business Insights", layout="wide")

# Function to encode image to Base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Encode background image
background_base64 = encode_image("b.jpg")  # Change this to your image path

# Add custom CSS for background image and layout
st.markdown(
    f"""
    <style>
        body {{
            background-image: url("data:image/png;base64,{background_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            margin: 0;
            padding: 0;
            height: 100vh;
            overflow: hidden; /* Disable body scrolling */
        }}
        .stApp {{
            position: absolute;
            top: 50%;
            left: 10%;
            transform: translateY(-50%);
            max-width: 1200px;
            height: 700px;
            background: rgba(211, 211, 211, 0.7);
            padding: 30px;
            border-radius: 12px;
            border: 1px solid #ccc;
            box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.3);
        }}
        h1, h2, h3 {{
            color: #333;
            font-weight: 600;
            animation: fadeInText 2s ease-in-out;
        }}
        .cta-button {{
            background-color: #4CAF50;
            color: white;
            padding: 15px 30px;
            border-radius: 10px;
            text-align: center;
            cursor: pointer;
            font-size: 20px;
            font-weight: bold;
            box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.2);
        }}
        .cta-button:hover {{
            background-color: #45a049;
        }}
        @keyframes fadeInText {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        .center-button {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)



# Hero Section with CTA button
st.markdown(
    """
    <div style="text-align:center; margin-bottom:20px;">
        <h1>Superstore Sales: Interactive Business Insights</h1>
        
    </div>
    """, unsafe_allow_html=True
)

# Streamlit button for redirection in the sidebar
import streamlit as st

# Sidebar button
if st.sidebar.button('Explore Sales Data'):
    # Display the link after the button is clicked
    st.sidebar.markdown(
        """
        <div style="text-align:center; margin-top:20px;">
            <a href="https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting?resource=download" target="_blank">
                Click here to explore the Sales Data
            </a>
        </div>
        """, unsafe_allow_html=True
    )


st.subheader("Overview")
st.markdown(""" 
    <div style="text-align: justify;">
       Superstore Sales Platform is a cutting-edge solution that provides real-time and historical sales insights, 
       helping businesses stay informed about market trends and consumer behavior. We analyze key sales
       metrics across various dimensions, including Order Date, Segment, Country, City, State, Region, Product 
       Category, and Sub-Category, to deliver accurate sales performance insights.Whether you're tracking regional sales trends,
       optimizing inventory, or identifying high-demand products, Superstore Sales Platform equips you with the tools to understand 
       sales patterns and their impact on business growth. With our platform, you can monitor seasonal trends, analyze customer preferences, 
       forecast future sales, and make data-driven decisions to maximize profitability. Our mission is to provide accessible, easy-to-interpret
       sales analytics so businesses can stay ahead in an ever-evolving retail landscape.
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <iframe width="100%" height="350" src="https://www.youtube.com/embed/S-mJ5yY5nSg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
""", unsafe_allow_html=True)





# Features and Benefits Section
import streamlit as st

st.subheader("How It Works")
st.markdown("""
    <div style="text-align: justify;">
       Superstore Sales Interactive Insights works by aggregating and processing data from various retail 
       transactions and sources to provide both real-time and historical sales analytics. It collects key metrics, 
       including sales revenue, product demand, customer segments, and regional performance, from databases and sales records.
       The collected data undergoes preprocessing to handle missing values, remove duplicates, and standardize formats for consistency. 
       Once cleaned, the data is structured into a star schema format, enabling efficient analysis and visualization.
In Power BI, an interactive dashboard is developed with features such as filters and slicers, allowing users to explore sales trends, 
regional performance, category-wise sales distribution, and customer purchasing behavior. The dashboard includes visualizations like line charts,
bar charts, heat maps, and pie charts for a comprehensive understanding of business performance. By making data accessible and interactive, Superstore Sales 
Interactive Insights empowers businesses to make data-driven decisions related to inventory planning, marketing strategies, and revenue growth, helping them stay
ahead in a competitive retail market.
    </div>
""", unsafe_allow_html=True)

st.subheader("Why It Matters")
st.markdown("""
    <div style="text-align: justify;">
        Good sales insights are essential for business growth. By monitoring sales trends, 
        you can take proactive steps to optimize inventory, improve marketing strategies, and boost revenue. 
        Stay informed and make data-driven decisions to maximize profitability and enhance customer satisfaction.
    </div>
""", unsafe_allow_html=True)

params = st.query_params

# Page routing
if params.get("page") == "homes":
    st.title("Welcome to the Home Page")
    st.write("Explore all insights here.")
else:
    st.title("Call to Action: Explore Insights")
    st.markdown(
        """
        <div style="text-align:center; margin-top:30px;">
            <a href="/Home" style="text-decoration:none;">
                <button style="padding:10px 20px; font-size:16px; background-color:#007BFF; color:white; border:none; border-radius:5px; cursor:pointer;">
                    Get Started
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True
    )
        
        
        
# Footer with additional resources and social media links
st.markdown(""" 
<div style="text-align:center; padding-top:30px;">
    <p><strong>Follow Us:</strong></p>
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
""", unsafe_allow_html=True)

# Footer with privacy and contact info
st.markdown(""" 
<div style="text-align:center; padding-top:30px; font-size:14px;">
    <p><a href="https://www.yourwebsite.com/privacy" target="_blank">Privacy Policy</a> | <a href="https://www.yourwebsite.com/contact" target="_blank">Contact Us</a></p>
</div>
""", unsafe_allow_html=True)
