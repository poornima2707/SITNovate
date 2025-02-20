import streamlit as st
import base64
import os

# Set page configuration
st.set_page_config(page_title="Welcome Back!", layout="wide")

# Function to encode image to Base64 (with relative path handling)
def encode_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return encoded_string
    else:
        return None

# Encode background image (use relative path for portability)
background_image_path = "b.jpg"  # Update this with a relative path
background_base64 = encode_image(background_image_path)

# Add custom CSS for background image, layout, and styling
st.markdown(
    f"""
    <style>
        body {{
            background-image: url("data:image/png;base64,{background_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
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
        .content {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .text-content {{
            width: 60%;
        }}
        .image-content {{
            width: 35%;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .image-content img {{
            max-width: 100%;
            height: 650px;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Conclusion content with an image
image_path = "e.png"  # Replace with your image path
image_base64 = encode_image(image_path)

conclusion_content = f"""
<div class="content">
    <div class="text-content">
        <h2>📑 Conclusion:</h2>
        <ul>
            <li><strong>Key Findings:</strong>
                <ul>
                    <li>Sales trends show seasonal fluctuations, with peak sales during certain months.</li>
                    <li>Profit margins vary across categories; some products have high revenue but low profitability.</li>
                    <li>Region-wise sales distribution highlights top-performing and underperforming areas.</li>
                </ul>
            </li>
            <li><strong>Regional Comparison:</strong>
                <ul>
                    <li>Major differences in sales and profit among regions, with certain states leading.</li>
                    <li>Regional performance influenced by customer demand, product availability, and discount strategies.</li>
                </ul>
            </li>
            <li><strong>Customer and Product Insights:</strong>
                <ul>
                    <li>Top customers contribute significantly to overall revenue.</li>
                    <li>High-selling categories include Technology and Office Supplies, while some categories underperform.</li>
                </ul>
            </li>
            <li><strong>Trend Analysis:</strong>
                <ul>
                    <li>Yearly and monthly sales trends indicate seasonality and promotional impacts.</li>
                    <li>Discount strategies impact profit; excessive discounts can reduce profitability.</li>
                </ul>
            </li>
            <li><strong>Recommendations:</strong>
                <ul>
                    <li>Optimize inventory for high-demand products to avoid stockouts.</li>
                    <li>Adjust pricing and discount strategies to maximize profit.</li>
                    <li>Target high-revenue customer segments for marketing and retention.</li>
                </ul>
            </li>
            <li><strong>Future Scope:</strong>
                <ul>
                    <li>Enhance data analytics by integrating customer feedback and market trends.</li>
                    <li>Use predictive analytics for demand forecasting and better stock management.</li>
                </ul>
            </li>
        </ul>
    </div>
    <div class="image-content">
        <img src="data:image/png;base64,{image_base64}" alt="Conclusion Image">
    </div>
</div>
"""


# Add the Conclusion content to your Streamlit app
st.markdown(conclusion_content, unsafe_allow_html=True)
