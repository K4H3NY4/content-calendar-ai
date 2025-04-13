
import os
import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(page_title="Socials Calendar AI Assistant", page_icon="🧑‍💻")
st.title('🧑‍💻 Socials Calendar AI Assistant')

def generate_content(prompt: str, client: Groq) -> str:
    """Generate content using Groq API"""
    system_prompt = """Create a social media content calendar including:
    - Brand strategy and target audience analysis
    - Content direction and themes
    - Monthly content calendar for Facebook, Twitter, Instagram, TikTok, LinkedIn
    - Post scheduling recommendations
    - Influencer suggestions with metrics
    Format in clear sections with tables where appropriate."""

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=4096,
        top_p=0.95,
        stream=True
    )
    
    return completion

def main():
    # Initialize Groq client
    client = Groq(api_key=os.environ.get("API_KEY"))
    
    # User input
    prompt = st.text_area('Enter your social media brief:', height=100)
    
    if st.button("🚀 Generate Content Calendar") and prompt:
        with st.spinner("Generating your content calendar..."):
            completion = generate_content(prompt, client)
            
            # Display streaming response
            response_container = st.empty()
            full_response = ""
            
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    response_container.markdown(full_response)
            
            # Download button
            st.download_button(
                label="📥 Download Calendar",
                data=full_response,
                file_name="content_calendar.txt",
                mime="text/plain"
            )

if __name__ == "__main__":
    main()
