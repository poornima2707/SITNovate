import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from wordcloud import WordCloud
import shap
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
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to encode categorical columns using Label Encoding
def encode_categorical_columns(df):
    label_encoders = {}
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    return df, label_encoders

# Function to upload and display the dataset
def upload_data():
    uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.write("### Dataset Overview", df.head())
            return df
        except Exception as e:
            st.error(f"Error loading file: {e}")
            return None
    else:
        st.warning("Please upload a CSV file to continue.")
        return None

# Function to handle missing data
def handle_missing_data(df):
    if df is not None:
        st.write("### Handle Missing Data")
        missing_action = st.selectbox("Select an option to handle missing data:", ["Drop Rows", "Fill with Mean/Median/Mode", "Keep as is"])
        
        if missing_action == "Drop Rows":
            df = df.dropna()
            st.write("Rows with missing data have been dropped.")
        elif missing_action == "Fill with Mean/Median/Mode":
            fill_option = st.selectbox("Choose fill method:", ["Mean", "Median", "Mode"])
            if fill_option == "Mean":
                df = df.fillna(df.mean())
            elif fill_option == "Median":
                df = df.fillna(df.median())
            elif fill_option == "Mode":
                df = df.fillna(df.mode().iloc[0])
            st.write(f"Missing values have been filled with {fill_option}.")
        return df
    else:
        return df

# Function for data preprocessing
def preprocess_data(df):
    if df is not None:
        st.write("### Data Preprocessing Options")
        preprocessing_choice = st.selectbox("Choose a preprocessing option:", ["Normalization/Standardization", "Categorical Encoding", "None"])

        if preprocessing_choice == "Normalization/Standardization":
            cols_to_scale = st.multiselect("Select columns for scaling:", df.select_dtypes(include=["float64", "int64"]).columns)
            if cols_to_scale:
                scaler = StandardScaler()
                df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
                st.write(f"Normalized/Standardized columns: {cols_to_scale}")
        
        elif preprocessing_choice == "Categorical Encoding":
            df, label_encoders = encode_categorical_columns(df)
            st.write("Categorical columns have been encoded.")
        
        return df
    else:
        return df

# Function for visualization with dynamic filtering and customization


def generate_visualizations(df):
    if df is not None:
        st.write("### Visualizations")

        # Scatter Plot
        if st.checkbox("Show Scatter Plot"):
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
            x_col = st.selectbox("Select X-axis column for Scatter Plot:", numeric_cols, key="scatter_x")
            y_col = st.selectbox("Select Y-axis column for Scatter Plot:", numeric_cols, key="scatter_y")
            color = st.color_picker("Pick color for scatter plot", "#ff7f0e")
            title = st.text_input("Enter title for scatter plot", "Scatter Plot")
            font_size = st.slider("Select font size for the plot", 8, 20, 12)
            font_color = st.color_picker("Pick font color", "#000000")
            font_family = st.selectbox("Select font family", ["sans-serif", "serif", "monospace"], index=0)
            
            # Top-n filtering for Scatter Plot
            top_n = st.number_input("Filter top N rows (0 for all):", min_value=0, max_value=len(df), value=0)
            if top_n > 0:
                filtered_df = df.nlargest(top_n, y_col)
            else:
                filtered_df = df
            
            fig, ax = plt.subplots()
            ax.scatter(filtered_df[x_col], filtered_df[y_col], color=color, edgecolor='black')
            ax.set_title(title, fontsize=font_size, color=font_color, family=font_family)
            ax.set_xlabel(x_col, fontsize=font_size, color=font_color, family=font_family)
            ax.set_ylabel(y_col, fontsize=font_size, color=font_color, family=font_family)
            st.pyplot(fig)

        # Bar Plot
        if st.checkbox("Show Bar Plot"):
            categorical_cols = df.select_dtypes(include=["object"]).columns
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
            x_col = st.selectbox("Select X-axis column for Bar Plot:", categorical_cols, key="bar_x")
            y_col = st.selectbox("Select Y-axis column for Bar Plot:", numeric_cols, key="bar_y")
            color = st.color_picker("Pick color for bar plot", "#1f77b4")
            title = st.text_input("Enter title for bar plot", "Bar Plot")
            font_size = st.slider("Select font size for the plot", 8, 20, 12)
            font_color = st.color_picker("Pick font color", "#000000")
            font_family = st.selectbox("Select font family", ["sans-serif", "serif", "monospace"], index=0)
            
            # Top-n filtering for Bar Plot
            top_n = st.number_input("Filter top N rows (0 for all):", min_value=0, max_value=len(df), value=0)
            if top_n > 0:
                filtered_df = df.nlargest(top_n, y_col)
            else:
                filtered_df = df
            
            fig, ax = plt.subplots()
            sns.barplot(x=x_col, y=y_col, data=filtered_df, ax=ax, color=color)
            ax.set_title(title, fontsize=font_size, color=font_color, family=font_family)
            ax.set_xlabel(x_col, fontsize=font_size, color=font_color, family=font_family)
            ax.set_ylabel(y_col, fontsize=font_size, color=font_color, family=font_family)
            st.pyplot(fig)

        # Line Plot
        if st.checkbox("Show Line Plot"):
            x_col = st.selectbox("Select X-axis column for Line Plot:", df.columns, key="line_x")
            y_col = st.selectbox("Select Y-axis column for Line Plot:", df.columns, key="line_y")
            color = st.color_picker("Pick color for line plot", "#2ca02c")
            title = st.text_input("Enter title for line plot", "Line Plot")
            font_size = st.slider("Select font size for the plot", 8, 20, 12)
            font_color = st.color_picker("Pick font color", "#000000")
            font_family = st.selectbox("Select font family", ["sans-serif", "serif", "monospace"], index=0)
            
            fig, ax = plt.subplots()
            ax.plot(df[x_col], df[y_col], color=color)
            ax.set_title(title, fontsize=font_size, color=font_color, family=font_family)
            ax.set_xlabel(x_col, fontsize=font_size, color=font_color, family=font_family)
            ax.set_ylabel(y_col, fontsize=font_size, color=font_color, family=font_family)
            st.pyplot(fig)

        # Pie Chart
        if st.checkbox("Show Pie Chart"):
            categorical_cols = df.select_dtypes(include=["object"]).columns
            col = st.selectbox("Select a categorical column for Pie Chart:", categorical_cols)
            title = st.text_input("Enter title for pie chart", "Pie Chart")
            font_size = st.slider("Select font size for the plot", 8, 20, 12)
            font_color = st.color_picker("Pick font color", "#000000")
            font_family = st.selectbox("Select font family", ["sans-serif", "serif", "monospace"], index=0)
            
            pie_data = df[col].value_counts()
            fig, ax = plt.subplots()
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("Set3", len(pie_data)))
            ax.axis('equal')
            ax.set_title(title, fontsize=font_size, color=font_color, family=font_family)
            st.pyplot(fig)

        # Histogram
        if st.checkbox("Show Histogram"):
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
            col = st.selectbox("Select a numeric column for Histogram:", numeric_cols)
            bins = st.slider("Select number of bins:", 5, 50, 20)
            color = st.color_picker("Pick color for histogram", "#ff6347")
            title = st.text_input("Enter title for histogram", "Histogram")
            font_size = st.slider("Select font size for the plot", 8, 20, 12)
            font_color = st.color_picker("Pick font color", "#000000")
            font_family = st.selectbox("Select font family", ["sans-serif", "serif", "monospace"], index=0)

            fig, ax = plt.subplots()
            ax.hist(df[col], bins=bins, color=color, edgecolor='black')
            ax.set_title(title, fontsize=font_size, color=font_color, family=font_family)
            ax.set_xlabel(col, fontsize=font_size, color=font_color, family=font_family)
            ax.set_ylabel("Frequency", fontsize=font_size, color=font_color, family=font_family)
            st.pyplot(fig)

        # Box Plot
        if st.checkbox("Show Box Plot"):
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
            col = st.selectbox("Select a numeric column for Box Plot:", numeric_cols)
            title = st.text_input("Enter title for box plot", "Box Plot")
            font_size = st.slider("Select font size for the plot", 8, 20, 12)
            font_color = st.color_picker("Pick font color", "#000000")
            font_family = st.selectbox("Select font family", ["sans-serif", "serif", "monospace"], index=0)

            fig, ax = plt.subplots()
            sns.boxplot(x=df[col], ax=ax)
            ax.set_title(title, fontsize=font_size, color=font_color, family=font_family)
            ax.set_xlabel(col, fontsize=font_size, color=font_color, family=font_family)
            st.pyplot(fig)

        # Heatmap
        if st.checkbox("Show Heatmap"):
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
            corr_matrix = df[numeric_cols].corr()
            title = st.text_input("Enter title for heatmap", "Heatmap")
            font_size = st.slider("Select font size for the plot", 8, 20, 12)
            font_color = st.color_picker("Pick font color", "#000000")
            font_family = st.selectbox("Select font family", ["sans-serif", "serif", "monospace"], index=0)

            fig, ax = plt.subplots()
            sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
            ax.set_title(title, fontsize=font_size, color=font_color, family=font_family)
            st.pyplot(fig)

        # Violin Plot
        if st.checkbox("Show Violin Plot"):
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
            categorical_cols = df.select_dtypes(include=["object"]).columns
            x_col = st.selectbox("Select X-axis column for Violin Plot:", categorical_cols)
            y_col = st.selectbox("Select Y-axis column for Violin Plot:", numeric_cols)

            fig, ax = plt.subplots()
            sns.violinplot(x=df[x_col], y=df[y_col], ax=ax)
            ax.set_title("Violin Plot")
            st.pyplot(fig)

        # Area Chart
        if st.checkbox("Show Area Chart"):
            x_col = st.selectbox("Select X-axis column for Area Chart:", df.columns)
            y_col = st.selectbox("Select Y-axis column for Area Chart:", df.columns)
            title = st.text_input("Enter title for area chart", "Area Chart")
            font_size = st.slider("Select font size for the plot", 8, 20, 12)

            fig, ax = plt.subplots()
            ax.fill_between(df[x_col], df[y_col], color="skyblue", alpha=0.5)
            ax.set_title(title, fontsize=font_size)
            st.pyplot(fig)

        # Bubble Chart
        if st.checkbox("Show Bubble Chart"):
            numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns
            x_col = st.selectbox("Select X-axis column for Bubble Chart:", numeric_cols)
            y_col = st.selectbox("Select Y-axis column for Bubble Chart:", numeric_cols)
            size_col = st.selectbox("Select Size column for Bubble Chart:", numeric_cols)

            fig, ax = plt.subplots()
            ax.scatter(df[x_col], df[y_col], s=df[size_col]*10, alpha=0.5)
            ax.set_title("Bubble Chart")
            st.pyplot(fig)

        # Radar Chart
        if st.checkbox("Show Radar Chart"):
            categorical_cols = df.select_dtypes(include=["object"]).columns
            col = st.selectbox("Select categorical column for Radar Chart:", categorical_cols)

            categories = df[col].unique()
            values = df[col].value_counts()

            fig, ax = plt.subplots(subplot_kw=dict(polar=True))
            ax.bar(categories, values, width=0.3, bottom=0.2)
            ax.set_title("Radar Chart")
            st.pyplot(fig)
        if st.checkbox("Show Word Cloud"):
            text_column = st.selectbox("Select a column for Word Cloud", df.select_dtypes(include=["object"]).columns)
            title = st.text_input("Enter title for word cloud", "Word Cloud")
            font_size = st.slider("Select font size for the word cloud", 8, 50, 30)
            max_words = st.slider("Select the maximum number of words", 10, 200, 100)

            text_data = ' '.join(df[text_column].dropna().astype(str).values)
            wordcloud = WordCloud(width=800, height=400, max_words=max_words, background_color="white").generate(text_data)

            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis('off')
            ax.set_title(title, fontsize=font_size)
            st.pyplot(fig)

# Main Streamlit app
def main():
    st.title("Data Analysis and Machine Learning App")
    st.sidebar.title("Navigation")
    # Step 1: Upload CSV
    df = upload_data()

    if df is not None:
        # Step 2: Handle Missing Data
        df = handle_missing_data(df)
        
        # Step 3: Data Preprocessing
        df = preprocess_data(df)

        # Step 4: Visualizations
        generate_visualizations(df)

if __name__ == "__main__":
    main()
