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
    model="llama3-70b-8192",
    messages=[
        {
            "role": "system",
            "content": "write a content calendar for social media for a month, come up with copy and caption, suggest a theme and the visual assets style, from the copy generate keywords and campaigns, appropriate posting schedule and explain why, format this calendar for different platforms for facebook,twitter,instagram,tiktok and linkedin. structure content in a table format. Close the response with: Feel free to reach out to us at +254 700 419 377 or sasa@rnd.co.ke for consulting services regarding social media and other needs."
        },
        {
            "role": "user",
            "content": "pembe millers kenya"
        },
        {
            "role": "assistant",
            "content": "Here is a sample content calendar for Pembe Millers Kenya, a leading miller of wheat and maize in Kenya, for a month:\n\n**Theme:** \"Nourishing Kenya, One Loaf at a Time\"\n\n**Visual Assets Style:** Warm and inviting images of Pembe Millers' products, kenkey, and mandazi, with a mix of modern and traditional Kenyan settings.\n\n**Content Calendar:**\n\n| Platform | Date | Post Type | Copy and Caption | Keywords | Campaign | Posting Schedule |\n| --- | --- | --- | --- | --- | --- | --- |\n| Facebook | 1st | Educational | \"Did you know that whole wheat bread can help lower cholesterol levels? Eat healthy with our whole wheat flour! #WholeWheat #HealthyEating\" | whole wheat, healthy eating | #NourishingKenya | 10:00 AM |\n| Twitter | 3rd | Promotional | \"Get 10% off on our premium wheat flour this week! Use code PEMBE10 at checkout #PembeDeals #WheatFlour\" | wheat flour, discount | #PembeDeals | 2:00 PM |\n| Instagram | 5th | Visual | Image of a delicious loaf of bread with the caption \"Fresh from our mill to your table! #BreadLovers #PembeMillers\" | bread, fresh bread | #PembeFresh | 11:00 AM |\n| TikTok | 7th | Entertainment | Short video of a Kenyan family enjoying a meal together with Pembe Millers' products, captioned \"Family time is the best time! #PembeMoments #FamilyLove\" | family, kenyan culture | #PembeVibes | 4:00 PM |\n| LinkedIn | 10th | Thought Leadership | \"The importance of locally sourced ingredients in Kenyan baking\" article, highlighting Pembe Millers' commitment to local sourcing. | locally sourced, kenyan baking | #PembeThoughts | 10:00 AM |\n| Facebook | 12th | User-Generated Content | \"Share a photo of your favorite recipe using Pembe Millers' flour and tag us! We'll feature the best ones on our page! #PembeRecipes #BakingCommunity\" | user-generated, recipes | #PembeRecipes | 2:00 PM |\n| Twitter | 14th | Promotional | \"Free delivery on all orders above KES 1,000! Use code PEMBEDEL at checkout #PembeDeals #FreeDelivery\" | free delivery, online shopping | #PembeDeals | 11:00 AM |\n| Instagram | 17th | Educational | Infographic highlighting the benefits of whole wheat bread, captioned \"Did you know? #WholeWheat #HealthyEating\" | whole wheat, healthy eating | #PembeTips | 10:00 AM |\n| TikTok | 19th | Entertainment | Short video of a fun recipe using Pembe Millers' products, captioned \"Get creative with Pembe Millers! #PembeRecipes #BakingInspiration\" | recipe, baking inspiration | #PembeVibes | 4:00 PM |\n| LinkedIn | 22nd | Thought Leadership | \"Sustainability in the Kenyan milling industry\" article, highlighting Pembe Millers' efforts towards a more sustainable future. | sustainability, kenyan milling industry | #PembeThoughts | 10:00 AM |\n| Facebook | 24th | Promotional | \"Flash sale! Get 20% off on all products for the next 24 hours! Use code PEMBEFLASH at checkout #PembeDeals #FlashSale\" | flash sale, discount | #PembeDeals | 2:00 PM |\n| Twitter | 26th | Educational | \"Did you know that our wheat flour is milled from 100% Kenyan wheat? Support local with Pembe Millers! #KenyanWheat #SupportLocal\" | kenyan wheat, support local | #PembePride | 11:00 AM |\n| Instagram | 28th | Visual | Image of a Pembe Millers' product with the caption \"Quality you can trust, every time! #PembeQuality #TrustTheBrand\" | quality, trust the brand | #PembeFresh | 10:00 AM |\n| TikTok | 30th | Entertainment | Short video of a fun challenge using Pembe Millers' products, captioned \"Take the Pembe Challenge! #PembeChallenge #BakingFun\" | challenge, baking fun | #PembeVibes | 4:00 PM |\n\n**Posting Schedule:**\n\n* Facebook: 10:00 AM and 2:00 PM on weekdays\n* Twitter: 11:00 AM and 2:00 PM on weekdays\n* Instagram: 10:00 AM and 4:00 PM on weekdays\n* TikTok: 4:00 PM on weekdays\n* LinkedIn: 10:00 AM on weekdays\n\n**Why:**\n\n* Posting at peak hours (10:00 AM and 2:00 PM) to maximize engagement\n* Mixing up the types of posts to keep the audience engaged\n* Using relevant hashtags to increase visibility and attract new followers\n* Creating a consistent visual style across all platforms\n* Posting at least once a day on each platform to maintain a strong online presence\n\nFeel free to reach out to us at +254 700 419 377 or sasa@rnd.co.ke for consulting services regarding social media and other needs."
        }
    ],
    temperature=1,
    max_tokens=8000,
    top_p=1,
    stream=True,
    stop=None,
)
  # Display the generated response
    st.write(chat_completion.choices[0].message.content)
else:
    st.write("Socials Calendar AI.")
