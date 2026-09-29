import streamlit as st
import google.generativeai as genai

# Page settings
st.set_page_config(
    page_title="GenAI Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 GenAI Assistant")
st.write("Ask a question and get an AI-generated answer.")

# API key
api_key = st.text_input(
    "Enter your Gemini API Key",
    type="password"
)

# User question
question = st.text_area(
    "Enter your question",
    placeholder="Example: Explain Artificial Intelligence in simple words."
)

# Generate button
if st.button("✨ Generate Answer"):

    if not api_key:
        st.error("Please enter your Gemini API key.")

    elif not question:
        st.warning("Please enter a question.")

    else:
        try:
            # Configure Gemini
            genai.configure(api_key=api_key)

            # Create Gemini model
            model = genai.GenerativeModel("gemini-2.0-flash")

            # Generate response
            response = model.generate_content(question)

            # Display result
            st.subheader("🤖 AI Answer")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
