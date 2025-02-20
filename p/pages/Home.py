import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Set page configuration
st.set_page_config(page_title="Home | AQI Monitoring Platform", layout="wide")

# CSS for custom styling with advanced animations
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f4f4f4;
    }
    /* Navbar Styles */
    nav ul {
        display: flex;
        justify-content: center;
        list-style: none;
        background-color: #004d99;
        margin: 0;
        padding: 10px 0;
    }
    nav ul li {
        margin: 0 15px;
    }
    nav ul li a {
        color: white;
        padding: 10px 20px;
        text-decoration: none;
        font-size: 16px;
        text-transform: uppercase;
        font-weight: 600;
        border-radius: 5px;
        transition: background-color 0.3s, transform 0.3s, letter-spacing 0.3s;
    }
    nav ul li a:hover {
        background-color: #0056b3;
        transform: scale(1.1);
        letter-spacing: 1px;
    }

    /* Hero Section */
    .hero {
        background: url('https://tse1.mm.bing.net/th?id=OIF.zC43iU4m8WTaz4GvZN%2fiYg&pid=Api&P=0&h=180') no-repeat center center/cover;
        height: 70vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        color: white;
        padding: 20px;
        background-size: cover;
        background-position: center;
        animation: fadeIn 1.5s ease-in;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .hero h1 {
        font-size: 60px;
        margin-bottom: 15px;
        font-weight: bold;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.6);
        animation: slideUp 1.5s ease-in-out;
    }
    @keyframes slideUp {
        0% { transform: translateY(30px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    .hero p {
        font-size: 22px;
        margin-bottom: 30px;
        font-weight: 400;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.6);
        animation: fadeIn 1.5s ease-in;
    }
    .cta-buttons a {
        padding: 15px 25px;
        margin: 10px;
        color: white;
        border-radius: 50px;
        text-align: center;
        display: inline-block;
        background-color: #007bff;
        font-size: 18px;
        font-weight: 600;
        text-decoration: none;
        transition: transform 0.3s, background-color 0.3s;
    }
    .cta-buttons a:hover {
        transform: scale(1.1);
        background-color: #0056b3;
    }
    .cta-buttons .btn-secondary {
        background-color: #6c757d;
    }
    .cta-buttons .btn-secondary:hover {
        background-color: #495057;
    }

    /* Features Section */
    .features {
        display: flex;
        justify-content: space-evenly;
        padding: 40px;
        background-color: #ffffff;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        animation: fadeIn 1.5s ease-out;
    }
    .feature {
        width: 30%;
        text-align: center;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .feature h3 {
        margin-bottom: 15px;
        font-size: 24px;
        font-weight: bold;
        color: #004d99;
    }
    .feature p {
        font-size: 16px;
        color: #555;
    }
    .feature:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }

    /* Call to Action Section */
    .cta-section {
        text-align: center;
        padding: 50px;
        background-color: #004d99;
        color: white;
        animation: slideUp 1s ease-in-out;
    }
    .cta-section p {
        font-size: 24px;
        margin-bottom: 25px;
        font-weight: 600;
    }
    .cta-section .btn-primary {
        padding: 15px 35px;
        font-size: 18px;
        font-weight: 600;
        border-radius: 50px;
        background-color: #007bff;
        transition: background-color 0.3s, transform 0.3s;
    }
    .cta-section .btn-primary:hover {
        background-color: #0056b3;
        transform: scale(1.1);
    }

    /* Testimonials Section */
    .testimonials {
        padding: 40px;
        text-align: center;
        background-color: #f9f9f9;
        margin-top: 20px;
        animation: fadeIn 1.5s ease-in;
    }
    .testimonials blockquote {
        font-size: 20px;
        font-style: italic;
        margin-bottom: 10px;
        color: #333;
        line-height: 1.8;
    }
    .testimonials cite {
        font-size: 18px;
        font-weight: 600;
        color: #007bff;
    }

    /* Footer Section */
    .footer {
        background-color: #333;
        color: white;
        padding: 20px;
        text-align: center;
        font-size: 14px;
    }
    .footer a {
        color: white;
        margin: 0 10px;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .social-media a img {
        width: 30px;
        margin: 0 10px;
        transition: transform 0.3s;
    }
    .social-media a:hover img {
        transform: scale(1.2);
    }

    /* Transparent Back Button */
    .back-btn {
        padding: 15px 25px;
        background-color: transparent;
        color: #007bff;
        font-size: 18px;
        font-weight: 600;
        border: 2px solid #007bff;
        border-radius: 50px;
        text-align: center;
        display: inline-block;
        text-decoration: none;
        transition: transform 0.3s, background-color 0.3s;
    }
    .back-btn:hover {
        background-color: rgba(0, 123, 255, 0.1); /* Slight blue background on hover */
        transform: scale(1.1);
    }

    /* Responsive Design */
    @media screen and (max-width: 768px) {
        .features {
            flex-direction: column;
            align-items: center;
        }
        .feature {
            width: 80%;
            margin-bottom: 30px;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <nav>
        <ul>
            <li><a href="/Homes" onclick="window.location.href='#Homes'">Home</a></li>
            <li><a href="/Dashboard1" onclick="window.location.href='#Dashboard1'">Dashboard</a></li>
            <li><a href="/your_app" onclick="window.location.href='#login_signup'">Login/Signup</a></li>
            <li><a href="/Conculsion" onclick="window.location.href='#conclusion'">Conclusion</a></li>
            <li><a href="/Contact" onclick="window.location.href='#contact_us'">Contact Us/Feedback</a></li>
        </ul>
    </nav>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>Welcome to the Superstore Sales Trend Monitoring Platform</h1>
    <p>Your go-to resource for tracking and analyzing sales trends.</p>
    <div class="cta-buttons">
        <a href="#get-started" class="btn-primary">Get Started</a>
        <a href="#learn-more" class="btn-secondary">Learn More</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Brief Introduction
st.markdown("""
<div class="introduction" id="learn-more">
    <p style="text-align: justify;">
  The Superstore Sales Trend Analytics Platform simplifies the complexity of retail data, 
  empowering businesses, analysts, and decision-makers with actionable insights. 
  Raw sales data can be difficult to interpret due to inconsistent formats, seasonal fluctuations, and varying consumer behavior. 
  To address this, our platform integrates ETL (Extract, Transform, Load), data cleansing, trend analysis, and predictive modeling 
  into an interactive Power BI dashboard. Users can track sales trends over time, monitor regional and product-wise performance, 
  analyze demand patterns, and forecast future sales. By providing data-driven insights, this platform helps businesses optimize inventory management, 
  pricing strategies, and marketing campaigns, enabling them to stay ahead in a competitive market. With real-time analytics and intuitive visualizations,
  decision-makers can make informed choices to enhance profitability and drive sustainable growth.
</p>

</div>
""", unsafe_allow_html=True)
st.image("C:\\Users\\DELL\\OneDrive\\Desktop\\p\\c.png", use_container_width=True)
# Highlight Features Section
st.markdown("""
<div class="features">
    <div class="feature">
        <h3>Real-time Data Visualization</h3>
        <p>Get access to real-time sales data and trends across multiple regions</p>
    </div>
    <div class="feature">
        <h3>State-wise and City-wise Sales Insights</h3>
        <p>Explore sales performance across different states and cities with detailed comparisons.</p>
    </div>
    <div class="feature">
        <h3>Historical Trends and Future Predictions</h3>
        <p>Analyze historical data and predict future trends to understand long-term impacts.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Call to Action Section
st.markdown("""
<div class="cta-section" id="get-started">
    <p>Ready to optimize your sales strategy? Start analyzing your store's performance now!</p>
    <a href="https://www.iqair.com/in-en/air-quality-map" class="btn-primary">Start Monitoring</a>
</div>
""", unsafe_allow_html=True)

# Conclusion Section
st.markdown("""
<div class="testimonials" id="conclusion">
    <blockquote>"This platform has helped me stay ahead of future sales trends, enabling me to make data-driven decisions and optimize business strategies."</blockquote>
    <cite>- User</cite>
</div>
""", unsafe_allow_html=True)

# Footer Section
st.markdown("""
<div class="footer">
    <p>&copy; 2025 Superstore Sales Analytics Platform. All rights reserved.</p>
    <div class="social-media">
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
""", unsafe_allow_html=True)


