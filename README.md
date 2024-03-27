## StudyBuddy: YouTube Notes Generator 

### Overview:
The YouTube Transcript Analyzer is a tool designed to aid students in studying through multiple YouTube videos. It collects transcripts from these videos, stores them as vectors, and generates detailed notes. Additionally, it provides Q&A support, helping students clear doubts while reviewing lecture material.

### Features:
1. **Transcript Collection**: The project collects transcripts from multiple YouTube videos.
2. **Transcript Vectorization**: Transcripts are stored as vectors, facilitating efficient processing and analysis.
3. **Note Generation**: Detailed notes are generated from the collected transcripts, aiding students in summarizing and reviewing lecture content.
4. **Q&A Support**: The tool provides Q&A support, allowing students to clarify doubts or ask questions related to the lecture material.

### Technologies Used:
- **Streamlit**: The user interface is built using Streamlit, a popular Python library for creating interactive web applications.
- **dotenv**: Used for loading environment variables from a .env file.
- **google.generativeai**: Utilized for generating detailed notes from transcript vectors.
- **youtube_transcript_api**: Used for fetching transcripts from YouTube videos.

### How to Run:
1. **Install Dependencies**: Install the required Python packages by running:
    ```
    pip install streamlit python-dotenv google google-generativeai youtube-transcript-api
    ```

2. **Set Up Environment Variables**: Create a .env file and set the required environment variables. For example:
    ```
    API_KEY=YOUR_YOUTUBE_API_KEY
    ```

3. **Run the Application**: Execute the following command in your terminal:
    ```
    streamlit run app.py
    ```

### Usage:
1. **Transcript Collection**: Enter the URLs of the YouTube videos from which you want to collect transcripts.
2. **Note Generation**: Once the transcripts are collected, click on the "Generate Notes" button to generate detailed notes.
3. **Q&A Support**: Use the provided interface to ask questions or clarify doubts related to the lecture material.

### Contributors:
- Shivam Bhardwaj
- bshivam.work@gmail.com

### License:
This project is licensed under the MIT License. (Specify the license used for your project)

### Acknowledgements:
- [Streamlit](https://streamlit.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [Google GenerativeAI](https://github.com/google-research/Google-research)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)

### Disclaimer:
This project is developed for educational purposes and is not affiliated with or endorsed by YouTube or any other third-party platforms mentioned.
