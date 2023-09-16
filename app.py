import streamlit as st
import openai
import re
from youtubesearchpython import VideosSearch

 

# Set your OpenAI API key
openai.api_key = "YOUR-API-KEY"

 

# Set the background image

st.markdown(

 

    """

 

    <style>

    .stApp {

    background-image: url("https://img.freepik.com/free-photo/colorful-smoky-watercolor-textured-background_53876-101802.jpg?w=996&t=st=1694777373~exp=1694777973~hmac=74e3fc519ef9400ac4f274675febfff01ea690aafc3b087dbfa1ee771781404d");

    background-size: cover;

    }

    </style>

 

    """,

 

    unsafe_allow_html=True

 

)

 

# Streamlit UI

st.title("The Soundwave Surfer 🎵")

st.write("Hello! I'm Soundwave Surfer, your friendly rhythm alchemist. I can help you find the perfect music to match your mood. Just tell me how you're feeling today, and I'll do my best to find you a song that will put a smile on your face.")

st.write("")
st.write("")
# User input

#user_input = st.text_input("Tell us how you are feeling today:", "")
user_input = st.text_input("**Tell us how you are feeling today:**", "")

if st.button("Get Song Recommendations"):

   messages = [

       {"role": "system", "content": "You are a helpful and friendly language model. Your job is to analyze user input and recommend music based on their input. If a message is not music-related, find a way to relate it to a song and recommend that song to the user."}

   ]

 

   model = "gpt-3.5-turbo"

 

   messages.append({"role": "user", "content": user_input})

 

   response = openai.ChatCompletion.create(

       model=model,

       messages=messages

   )

 

   bot_response = response.choices[0]["message"]["content"]

   messages.append({"role": "assistant", "content": bot_response})

 

   # Print the bot's response

   st.write(f"Soundwave Surfer: {bot_response}")

 

   # Extract the song names using regex

#    song_name_matches = re.findall(r'"([^"]*)"', bot_response)

   song_name_matches = re.findall(r'"([^"]*)"', bot_response)

 

   if song_name_matches:

       for song_name in song_name_matches:

           # Search for each song on YouTube using the YouTube API

           videosSearch = VideosSearch(song_name, limit=1)

           results = videosSearch.result()

 

           if results:

               # Get the link to the first search result (assuming it's the official video)

               youtube_link = results['result'][0]['link']

 

               # Display the song name and YouTube link

               st.write(f"YouTube Link for {song_name}: {youtube_link}")

 

               # Display the YouTube video frame

               st.video(youtube_link)

           else:

               st.write(f"Sorry, I couldn't find {song_name} on YouTube.")
