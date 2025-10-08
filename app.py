import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="AI Study Buddy 🤖",
    page_icon="📚",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .response-box {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin: 1rem 0;
        color: #000000;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🤖 AI Study Buddy</div>', unsafe_allow_html=True)
st.markdown("### Powered by Google Gemini")

# Sidebar for API key input
with st.sidebar:
    st.header("🔑 Setup")
    api_key = st.text_input("Enter Google Gemini API Key:", 
                           type="password",
                           help="Get free API key from https://aistudio.google.com/")
    
    st.markdown("---")
    st.markdown("**Get FREE API Key:**")
    st.markdown("1. Go to [Google AI Studio](https://aistudio.google.com/)")
    st.markdown("2. Sign in with Google account")
    st.markdown("3. Click 'Get API Key'")
    st.markdown("4. Paste it here")
    st.markdown("✅ **Completely FREE!**")

# Configure Gemini
if api_key:
    try:
        genai.configure(api_key=api_key)
        st.sidebar.success("✅ Gemini API configured!")
    except Exception as e:
        st.sidebar.error(f"❌ Error: {e}")
else:
    st.sidebar.warning("⚠️ Please enter API key to continue")

# AI Functions
def get_gemini_response(prompt):
    try:
        if not api_key:
            return "Please enter your Google Gemini API key in the sidebar first"
        
        model = genai.GenerativeModel('models/gemini-flash-latest')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def explain_concept(topic):
    prompt = f"Explain '{topic}' in simple terms for students. Use examples and break it into key points."
    return get_gemini_response(prompt)

def generate_quiz(topic):
    prompt = f"Create a 5-question multiple choice quiz about '{topic}' with answers."
    return get_gemini_response(prompt)

def create_flashcards(topic):
    prompt = f"Create 5 flashcard pairs (question-answer) for studying '{topic}'."
    return get_gemini_response(prompt)

# Main app
tab1, tab2, tab3 = st.tabs(["📖 Explain Concept", "❓ Generate Quiz", "🎴 Create Flashcards"])

with tab1:
    st.header("Explain Any Concept")
    concept = st.text_input("Enter topic:", key="concept")
    
    if st.button("Explain Concept"):
        if concept:
            with st.spinner("Generating explanation..."):
                explanation = explain_concept(concept)
                st.markdown(f'<div class="response-box">{explanation}</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter a topic")

with tab2:
    st.header("Generate Quiz")
    topic = st.text_input("Enter quiz topic:", key="quiz_topic")
    
    if st.button("Generate Quiz"):
        if topic:
            with st.spinner("Creating quiz..."):
                quiz = generate_quiz(topic)
                st.markdown(f'<div class="response-box">{quiz}</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter a topic")

with tab3:
    st.header("Create Flashcards")
    flashcard_topic = st.text_input("Enter topic for flashcards:", key="flashcards")
    
    if st.button("Create Flashcards"):
        if flashcard_topic:
            with st.spinner("Generating flashcards..."):
                flashcards = create_flashcards(flashcard_topic)
                st.markdown(f'<div class="response-box">{flashcards}</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter a topic")

st.markdown("---")
st.markdown("**AI Study Buddy** | 🔒 Secure API Key Handling")
