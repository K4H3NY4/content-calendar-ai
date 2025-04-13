
import os
import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(page_title="Socials Calendar AI Assistant", page_icon="🧑‍💻")
st.title('🧑‍💻 Socials Calendar AI Assistant')

def generate_content(prompt: str, client: Groq) -> str:
    """Generate content using Groq API"""
    system_prompt = """write a content calendar for social media for a month, Suggest the best tone to use in the communication, create sample copy matching the suggested tone. suggest a catchy and clever caption, suggest a theme and the visual assets style, from the copy generate keywords and campaigns, appropriate posting schedule and explain why, suggest the time the post should be scheduled, format this calendar for different platforms for facebook, twitter, instagram, tiktok and linkedin, include the perfect call to action based onthe social media platform. structure content in a table format. Suggest influencers to use in the campaigns, get their account link, average impressionsand number of followers. On top of the response outline a well detailed brand strategy to be used on the target audience, content direction in detail, target audience, age group, tone, theme, visual style and list of keywords. Close the response with: Feel free to reach out to us [ ID7 ] support@id7.co.ke for consulting services regarding social media and other needs."
."""

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
