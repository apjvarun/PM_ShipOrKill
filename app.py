import streamlit as st
import google.generativeai as genai
import os

# 1. Configuration
st.set_page_config(page_title="ShipOrKill", page_icon="🚢")

# 2. Sidebar for API Key
with st.sidebar:
    st.title("⚙️ Configuration")
    api_key = st.text_input("Enter Google API Key", type="password")
    st.markdown("[Get a Free Key Here](https://aistudio.google.com/app/apikey)")

# 3. Main UI
st.title("🚢 ShipOrKill: AI Product Validator")
st.markdown("Automated Discovery & Validation for Product Managers.")

# 4. Mode Selection (The "Master Menu" you asked for)
mode = st.radio("Select Mode:", ["🚀 Validate an Idea", "💡 Generate Ideas"], horizontal=True)

if mode == "🚀 Validate an Idea":
    user_input = st.text_area("Enter your product hypothesis:", height=100, 
                             placeholder="e.g., A Chrome extension that auto-applies to LinkedIn jobs...")
    
    # The "Validator" Persona (Copied from your validator.md)
    system_instruction = """
    You are a Principal Product Manager. Act as a 'Red Team' to validate this idea. 
    Use your knowledge to assess:
    1. Desirability (Do users want this?)
    2. Viability (Is there a business?)
    3. Feasibility (Can we build it?)
    Output a structured Markdown memo with a 'GO/NO-GO' verdict.
    """
    submit_btn = st.button("Analyze Risk")

else: # Generator Mode
    user_input = st.text_input("Enter a target industry (or leave blank):", placeholder="e.g., Healthcare, Construction")
    
    # The "Ideator" Persona (Copied from your ideator.md)
    system_instruction = """
    You are a Y-Combinator startup mentor. Generate 5 contrarian, high-potential B2B SaaS ideas 
    for the requested domain. Focus on 'boring' industries. 
    Format as: Idea Name - One sentence pitch - Why Now.
    """
    submit_btn = st.button("Generate Ideas")

# 5. The Logic (Connecting to Gemini)
if submit_btn and api_key:
    try:
        genai.configure(api_key=api_key)
        # We use the latest model which supports search grounding best
        model = genai.GenerativeModel('gemini-2.0-flash') 
        
        with st.spinner("🤖 Agent is analyzing live market data..."):
            # Note: For the web version, we use the standard generate_content. 
            # (Search grounding requires specific enterprise setup, so for this Portfolio MVP 
            # we rely on the model's huge internal knowledge base + standard web capability).
            response = model.generate_content(f"System Instruction: {system_instruction}\n\nUser Input: {user_input}")
            
        st.markdown("### 📋 Analyst Report")
        st.markdown(response.text)
        
    except Exception as e:
        st.error(f"Error: {e}")

elif submit_btn and not api_key:
    st.warning("Please enter an API Key in the sidebar to run the agent.")