import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
       api_key=os.environ.get('API_KEY')
)

st.title('Socials Calendar AI Assistant')

prompt = st.text_input('Enter your question here')


if prompt:  # Check if prompt is not empty
    # Generate response from the AI model
    completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "A content calendar for social media for a month, come up with copy and caption, suggest a theme and the visual assets style, from the copy generate keywords and campaigns, appropriate posting schedule and explain why, format this calendar for different platforms for facebook,twitter,instagram,tiktok and linkedin. structure content in a table format. Close the response with: Feel free to reach out to us at +254 700 419 377 or sasa@rnd.co.ke for consulting services regarding social media and other needs.",
        },{
            "role": "user",
            "content":prompt,
        }
    ],
    model="mixtral-8x7b-32768",
)
    # Display the generated response
    st.write(chat_completion.choices[0].message.content)
else:
    st.write("Socials Calendar AI.")
