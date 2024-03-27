import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = '''You are a youtube video summarizer. You will be given the transcript 
text and provide a detailed summary pointwise within 300 words. 
Here is the transcript text:'''

def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt+transcript_text)
    return response.text


def fetch_transcript(yt_url):
    try:
        video_id = yt_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    

st.title("Detailed Youtube Notes Generator")
youtube_link = st.text_input("Enter your Youtube video link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text = fetch_transcript(youtube_link)
    with open('transcript.txt', 'w') as f:
        f.write(transcript_text)
    if transcript_text:
        summary = generate_gemini_content(transcript_text,prompt)
        
        st.markdown("## Here's your detailed Notes:")
        st.write(summary)

