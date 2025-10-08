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
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🤖 AI Study Buddy</div>', unsafe_allow_html=True)
st.markdown("### Powered by Google Gemini - Now Working! 🎉")

# Your API key
API_KEY = "AIzaSyCWUqpxqGdDRv_7JyxQk_ftRUeuD6VsyoE"

# Configure Gemini with correct model
try:
    genai.configure(api_key=API_KEY)
    st.markdown('<div class="success-box">✅ Gemini API configured successfully!</div>', unsafe_allow_html=True)
except Exception as e:
    st.error(f"❌ API configuration failed: {e}")

# AI Functions with CORRECT model
def get_gemini_response(prompt):
    try:
        # Use the correct model that works
        model = genai.GenerativeModel('models/gemini-flash-latest')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def explain_concept(topic):
    prompt = f"""Explain '{topic}' in simple terms for students. Follow this format:

**What is {topic}?**
[Simple definition]

**Key Points:**
• [Point 1]
• [Point 2] 
• [Point 3]

**Real-life Example:**
[Practical example]

**Why it matters:**
[Importance and applications]

Make it engaging and easy to understand!"""
    return get_gemini_response(prompt)

def generate_quiz(topic):
    prompt = f"""Create a 5-question multiple choice quiz about '{topic}'. Format:

**Quiz: {topic}**

1. [Question 1]
   A) [Option A]
   B) [Option B]
   C) [Option C]
   D) [Option D]

2. [Question 2]
   A) [Option A]
   B) [Option B]
   C) [Option C]
   D) [Option D]

[Continue for 5 questions]

**Answers:**
1. [Correct letter] - [Brief explanation]
2. [Correct letter] - [Brief explanation]
3. [Correct letter] - [Brief explanation]
4. [Correct letter] - [Brief explanation]
5. [Correct letter] - [Brief explanation]"""
    return get_gemini_response(prompt)

def create_flashcards(topic):
    prompt = f"""Create 5 educational flashcard pairs for studying '{topic}'. Format each as:

Q: [Clear question]
A: [Concise answer]

Make them useful for revision and cover the main concepts."""
    return get_gemini_response(prompt)

def summarize_text(text):
    prompt = f"""Summarize the following text into clear study notes:

{text}

Format as:
**Summary**
• [Main point 1]
• [Main point 2]
• [Main point 3]

**Key Concepts:**
- [Concept 1]
- [Concept 2]

**Important Details:**
[Key details to remember]"""
    return get_gemini_response(prompt)

# Main app
tab1, tab2, tab3, tab4 = st.tabs(["📖 Explain Concept", "📝 Summarize Text", "❓ Generate Quiz", "🎴 Create Flashcards"])

with tab1:
    st.header("Explain ANY Concept")
    concept = st.text_input("Enter any topic:", placeholder="e.g., Quantum Physics, French Revolution, Machine Learning...", key="concept")
    
    if st.button("Explain Concept", key="explain"):
        if concept:
            with st.spinner("🤔 Generating AI explanation..."):
                explanation = explain_concept(concept)
                st.markdown(f'<div class="response-box">{explanation}</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter a topic")

with tab2:
    st.header("Summarize ANY Text")
    text = st.text_area("Paste any text to summarize:", height=150, placeholder="Paste your notes, articles, or textbook content here...", key="text")
    
    if st.button("Summarize Text", key="summarize"):
        if text:
            with st.spinner("📊 AI is summarizing..."):
                summary = summarize_text(text)
                st.markdown(f'<div class="response-box">{summary}</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter some text")

with tab3:
    st.header("Generate Quiz for ANY Topic")
    topic = st.text_input("Enter any topic for quiz:", placeholder="e.g., World War II, Python Programming, Biology...", key="topic")
    
    if st.button("Generate Quiz", key="quiz"):
        if topic:
            with st.spinner("🎯 Creating AI-powered quiz..."):
                quiz = generate_quiz(topic)
                st.markdown(f'<div class="response-box">{quiz}</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter a topic")

with tab4:
    st.header("Create Flashcards for ANY Topic")
    flashcard_topic = st.text_input("Enter any topic for flashcards:", placeholder="e.g., Calculus, Chemistry, History...", key="flashcards")
    
    if st.button("Create Flashcards", key="flashcards_btn"):
        if flashcard_topic:
            with st.spinner("🎴 Generating AI flashcards..."):
                flashcards = create_flashcards(flashcard_topic)
                st.markdown(f'<div class="response-box">{flashcards}</div>', unsafe_allow_html=True)
        else:
            st.error("Please enter a topic")

# Quick test buttons
st.markdown("---")
st.header("🎯 Test These Examples")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌿 Photosynthesis", use_container_width=True):
        with st.spinner("Explaining..."):
            result = explain_concept("Photosynthesis")
            st.markdown(f'<div class="response-box">{result}</div>', unsafe_allow_html=True)

with col2:
    if st.button("🐍 Python Basics", use_container_width=True):
        with st.spinner("Creating quiz..."):
            result = generate_quiz("Python programming basics")
            st.markdown(f'<div class="response-box">{result}</div>', unsafe_allow_html=True)

with col3:
    if st.button("⚛️ Atomic Theory", use_container_width=True):
        with st.spinner("Making flashcards..."):
            result = create_flashcards("Atomic Theory")
            st.markdown(f'<div class="response-box">{result}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("**AI Study Buddy v6.0** | 🚀 Powered by Gemini Flash Latest")
st.markdown("*Now with real AI that answers any question!*")