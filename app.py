import streamlit as st
import yt_dlp
import tempfile
import os
import re

# Validate YouTube URL
def is_youtube_url(url):
    youtube_regex = re.compile(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    return youtube_regex.match(url)

# Download video function with dynamic quality suggestion based on device
def download_video(url, quality="480p"):
    temp_file = tempfile.mktemp(suffix='.mp4')
    ydl_opts = {
        'format': f'best[height<={quality}][ext=mp4]',  # Quality suggestion handling
        'quiet': True,
        'outtmpl': temp_file,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_file_path = ydl.prepare_filename(info_dict)

        # Load video data
        with open(video_file_path, "rb") as f:
            video_data = f.read()

        # Calculate file size
        video_size = os.path.getsize(video_file_path) / (1024 * 1024)  # size in MB
        title = info_dict.get("title", "video")
        thumbnail_url = info_dict.get("thumbnail", "")
        description = info_dict.get("description", "")
        return video_data, title, video_size, thumbnail_url, description, info_dict

    except Exception as e:
        st.error(f"An error occurred during download: {e}")
        return None, None, None, None, None, None
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

# Streamlit interface setup
st.title("Video Grabber")
st.write("Enter a YouTube link to download the video with audio at 480p (if available).")

url = st.text_input("Enter YouTube Video URL")

# Dynamic quality recommendation based on user preference
quality_options = ["240p", "360p", "480p", "720p"]
quality = st.selectbox("Select Preferred Quality", quality_options, index=2)

if url:
    if is_youtube_url(url):
        if st.button("Download Video"):
            with st.spinner("Downloading..."):
                video_data, title, video_size, thumbnail_url, description, info_dict = download_video(url, quality)

                if video_data:
                    # Display thumbnail above the title
                    if thumbnail_url:
                        st.image(thumbnail_url, caption="Video Thumbnail", use_column_width=True)
                    
                    # Display download button just below the video details
                    st.download_button(
                        label="Download Video",
                        data=video_data,
                        file_name=f"{title}.mp4",
                        mime="video/mp4"
                    )
                    # Display video details
                    st.subheader("Video Details")
                    st.write(f"**Title**: {title}")
                    st.write(f"**Channel Name**: {info_dict.get('uploader', 'Unknown')}")
                    st.write(f"**Duration**: {info_dict.get('duration', 0)} seconds")
                    st.write(f"**Size**: {video_size:.2f} MB")

                    # Display video description
                    if description:
                        st.subheader("Video Description")
                        st.write(description)
                else:
                    st.warning("Download failed. Please check the URL or try a different quality setting.")
    else:
        st.error("Please enter a valid YouTube URL.")
