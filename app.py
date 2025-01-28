import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Retrieve API key and validate
api_key = os.environ.get('API_KEY')
if not api_key:
    raise ValueError("API_KEY is missing. Please set it in the .env file.")

# Initialize the Groq client
try:
    client = Groq(api_key=api_key)
except Exception as e:
    st.error(f"Failed to initialize Groq client: {e}")
    raise

def simulate_processing():
    """Simulate a time-consuming task."""
    time.sleep(3)
    return "Brainstorm Completed 🥳"

# Streamlit app UI
st.title('🧑‍💻 Socials Calendar AI Assistant 👩‍💻')

# Input for social media brief
prompt = st.text_input('Enter social media brief here')

# Define button outside the condition for better UX
if st.button("Brainstorm 🤯"):
    if prompt:  # Check if prompt is not empty
        # Show spinner while processing
        with st.spinner("Brainstorming 🤯🤯🤯"):
            try:
                # Generate response from the AI model
                completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "write a content calendar for social media for a month, "
                                "Suggest the best tone to use in the communication, create sample copy matching the suggested tone. "
                                "suggest a catchy and clever caption, suggest a theme and the visual assets style, "
                                "from the copy generate keywords and campaigns, appropriate posting schedule and explain why, "
                                "suggest the time the post should be scheduled, format this calendar for different platforms "
                                "for Facebook, Twitter, Instagram, TikTok, and LinkedIn. Include the perfect call to action "
                                "based on the social media platform. Structure content in a table format. "
                                "Suggest influencers to use in the campaigns, get their account link, average impressions, and number of followers. "
                                "On top of the response, outline a well-detailed brand strategy to be used on the target audience, content direction "
                                "in detail, target audience, age group, tone, theme, visual style, and list of keywords. "
                                "Close the response with: Feel free to reach out to us at +254 700 419 377 or sasa@rnd.co.ke for consulting services "
                                "regarding social media and other needs."
                            ),
                        },
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model="deepseek-r1-distill-llama-70b",  # Ensure this model exists in your Groq instance
                    max_tokens=8192,
                    top_p=1,
                )
                # Simulate a delay for a more realistic experience
                result = simulate_processing()

                # Display results
                st.success(result)
                st.write(completion.choices[0].message.content)  # Display the generated content

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt before brainstorming!")
