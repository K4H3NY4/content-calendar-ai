import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import time

load_dotenv()

client = Groq(
       api_key=os.environ.get('API_KEY')
)

def simulate_processing():
    # Simulate some time-consuming task
    time.sleep(3)
    return "Brisnstorming completed."

st.title('Socials Calendar AI Assistant')

prompt = st.text_input('Enter your question here')


if prompt:  # Check if prompt is not empty
    # Generate response from the AI model
    completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "write a content calendar for social media for a month, Suggest the best tone to use in the communication, create sample copy matching the suggested tone. suggest a catchy and clever caption, suggest a theme and the visual assets style, from the copy generate keywords and campaigns,appropriate posting schedule and explain why,suggest the time the post should be scheduled, format this calendar for different platforms for facebook,twitter,instagram,tiktok and linkedin, include the perfect call to action based on the social media platform. structure content in a table format.Suggest influencers to use in the campaigns,get their account link,average impressions and number of followers. On top of the response outline a well detailed brand strategy to be used on the target audience,content direction in detail,target audience,age group, tone, theme, visual style and list of keywords.  Close the response with: Feel free to reach out to us at +254 700 419 377 or sasa@rnd.co.ke for consulting services regarding social media and other needs.",
        },{
            "role": "user",
            "content":prompt,
        }
    ],
     model="llama3-70b-8192",
     max_tokens=8192,
     top_p=1,
     #stream=True,
     #stop=None,
)
    # Display the generated response
    if st.button("Brainstorm"):
        with st.spinner("Brainstorming ..."):
             result = simulate_processing()
             st.success(result)
             st.write(completion.choices[0].message.content)
else:
    st.write("Socials Calendar AI.")
