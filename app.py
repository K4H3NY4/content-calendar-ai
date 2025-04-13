import os
import time
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def simulate_processing():
    time.sleep(3)
    return "Brainstorm Completed 🥳"

st.title('🧑‍💻 Socials Calendar AI Assistant V3 👩‍💻')

# Text input for social media brief
prompt = st.text_input('Enter social media brief here')

# Add button
if st.button("🚀 Start Brainstorming") and prompt:
    with st.spinner("Generating your content calendar..."):
        client = Groq(api_key=os.environ.get('API_KEY'))

        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "write a content calendar for social media for a month, Suggest the best tone to use in the communication, "
                        "create sample copy matching the suggested tone. suggest a catchy and clever caption, suggest a theme and the visual assets style, "
                        "from the copy generate keywords and campaigns, appropriate posting schedule and explain why, suggest the time the post should be scheduled, "
                        "format this calendar for different platforms for facebook, twitter, instagram, tiktok and linkedin, include the perfect call to action based on "
                        "the social media platform. structure content in a table format. Suggest influencers to use in the campaigns, get their account link, average impressions "
                        "and number of followers. On top of the response outline a well detailed brand strategy to be used on the target audience, content direction in detail, "
                        "target audience, age group, tone, theme, visual style and list of keywords. Close the response with: Feel free to reach out to us at +254 700 419 377 or "
                        "sasa@rnd.co.ke for consulting services regarding social media and other needs."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.6,
            max_completion_tokens=4096,
            top_p=0.95,
            stream=True,
            stop=None,
        )

        # Accumulate and render the full response
        full_response = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                full_response += chunk.choices[0].delta.content

        st.markdown(full_response, unsafe_allow_html=True)
        st.success("Brainstorming completed!")