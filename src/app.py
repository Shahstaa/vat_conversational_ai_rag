import streamlit as st

# Define a highly professional CSS design
css = """
    <style>
    /* Global Styles */
    body {
        font-family: 'Roboto', Arial, sans-serif;
        background-color: #f4f6f9;
        color: #333;
        margin: 0;
        padding: 0;
    }

    /* Title and Heading Styling */
    h1 {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 700;
        color: #1D2A4D;
        margin-top: 40px;
        padding-bottom: 10px;
        border-bottom: 3px solid #1D2A4D;
    }

    h2 {
        color: #333;
        font-size: 1.4rem;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Container Styling */
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        max-width: 1000px;
        margin: 0 auto;
        padding: 40px;
        background-color: #ffffff;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
    }

    /* Input Field Styling */
    .stTextInput>div>input {
        border: 2px solid #D1D5DB;
        border-radius: 12px;
        padding: 14px 20px;
        font-size: 16px;
        width: 80%;
        max-width: 600px;
        margin: 10px 0;
        background-color: #ffffff;
        transition: all 0.3s ease;
        box-sizing: border-box;
    }

    .stTextInput>div>input:focus {
        border-color: #1D2A4D;
        outline: none;
        box-shadow: 0 0 5px rgba(29, 42, 77, 0.2);
    }

    /* Button Styling */
    .stButton>button {
        background-color: #1D2A4D;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 15px 30px;
        font-size: 18px;
        font-weight: 600;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease;
        margin-top: 20px;
    }

    .stButton>button:hover {
        background-color: #16304e;
        transform: translateY(-2px);
    }

    /* Answer Text Styling */
    .stWrite>p {
        font-size: 18px;
        text-align: center;
        color: #4a4a4a;
        line-height: 1.7;
        font-weight: 400;
        margin-top: 20px;
    }

    /* Loading Spinner and Error Message Styling */
    .stSpinner {
        color: #1D2A4D;
    }

    .stError {
        color: #e74c3c;
        font-size: 16px;
        text-align: center;
        margin-top: 20px;
    }

    /* Smooth container transitions */
    .stContainer {
        transition: all 0.3s ease;
    }

    /* Footer Styling */
    footer {
        text-align: center;
        font-size: 14px;
        color: #999;
        margin-top: 40px;
        padding-top: 20px;
    }
    </style>
"""

# Inject the custom CSS into the Streamlit app
st.markdown(css, unsafe_allow_html=True)

# Main title and description
st.title("VAT Conversational AI")
st.write("Ask any VAT-related question based on Bahrain's VAT Guide.")

# Main content layout
with st.container():
    question = st.text_input("Enter your question:")
    
    # Ask button functionality
    if st.button("Ask"):
        if question.strip():
            # Replace this with actual answer logic (API call or DB query)
            answer = "Sample answer based on the VAT Guide."
            st.write("**Answer:**", answer)
        else:
            st.error("Please enter a valid question.")

# Footer
st.markdown("""
    <footer>
        <p>Powered by Streamlit | Developed for Bahrain's VAT Guide</p>
    </footer>
""", unsafe_allow_html=True)
