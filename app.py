import streamlit as st
import yt_dlp
import tempfile
import os

# Download video with combined video and audio stream up to 480p
def download_video(url):
    ydl_opts = {
        'format': 'best[height<=480][ext=mp4]',  # Prioritize best video up to 480p with audio combined
        'quiet': True,
        'outtmpl': tempfile.mktemp(suffix='.mp4'),  # Save as temp file
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_file_path = ydl.prepare_filename(info_dict)

        # Calculate the size of the video file (in MB) before removing the temp file
        video_size = os.path.getsize(video_file_path) / (1024 * 1024)  # Size in MB

        # Load the downloaded video file into memory for browser download
        with open(video_file_path, "rb") as f:
            video_data = f.read()

        # Clean up the temporary file
        os.remove(video_file_path)

        # Extract video details
        title = info_dict.get("title", "video")
        thumbnail_url = info_dict.get("thumbnail", "")
        channel_name = info_dict.get("uploader", "Unknown Channel")
        duration = info_dict.get("duration", 0)  # Duration in seconds
        duration_str = f"{duration // 60}m {duration % 60}s"  # Convert duration to minutes and seconds
        
        return video_data, title, thumbnail_url, video_size, url, channel_name, duration_str
    except yt_dlp.utils.DownloadError as e:
        st.error(f"Error during download: {e}")
        return None, None, None, None, None, None, None

# Streamlit interface
st.title("Video Grabber")
st.write("Enter a YouTube link to download the video with audio at 480p (if available).")

url = st.text_input("Enter YouTube Video URL")
if url:
    if st.button("Download Video"):
        video_data, video_title, thumbnail_url, video_size, source_url, channel_name, video_duration = download_video(url)
        
        if video_data:
            # Display video details
            st.subheader("Video Details")
            st.write(f"**Title**: {video_title}")
            st.write(f"**Channel Name**: {channel_name}")
            st.write(f"**Duration**: {video_duration}")
            st.write(f"**Downloaded from**: {source_url}")
            st.write(f"**Size**: {video_size:.2f} MB")
            
            # Display thumbnail if available
            if thumbnail_url:
                st.image(thumbnail_url, caption="Video Thumbnail", use_column_width=True)

            # Add a download button
            st.download_button(
                label="Download Video",
                data=video_data,
                file_name=f"{video_title}.mp4",
                mime="video/mp4"
            )