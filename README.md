# YouTube Video Downloader with Streamlit

This project is a **YouTube video downloader** built with **Streamlit** and **yt-dlp**. It allows users to download YouTube videos with combined audio and video streams at up to **480p** resolution. The app provides essential information about the video, such as the title, channel name, duration, file size, and thumbnail, making it easy for users to preview before downloading.

---

### Features:
- **Video Download**: Download YouTube videos with audio in MP4 format.
- **Video Information**: Displays video title, channel name, duration, file size, and thumbnail.
- **User-friendly Interface**: Built with Streamlit for a simple web interface.
- **Automatic File Cleanup**: Automatically deletes temporary files after the download is complete.

---

### Requirements:
- **Python 3.x** (Recommended version: 3.8+)
- **yt-dlp**: A command-line tool for downloading videos from YouTube and other platforms.
- **Streamlit**: A framework to create interactive web apps for Python.

You can install the required dependencies using the following:

```bash
pip install yt-dlp streamlit
```

---

### Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/theleeveshkumar/yt-video-downloader.git
   ```
2. Navigate into the project folder:
   ```bash
   cd yt-video-downloader
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

### Usage:
1. Open your browser and go to the address displayed by Streamlit (usually `http://localhost:8501`).
2. Paste a valid **YouTube video URL** in the input field.
3. Click the **Download Video** button.
4. The app will display:
   - Video title
   - Channel name
   - Video duration (in minutes and seconds)
   - File size (in MB)
   - Video thumbnail
5. Click the **Download Video** button to start downloading the video.

---

### Example Output:
Once you input the YouTube URL and click "Download Video", the app will show a preview with the following details:
- **Title**: Example Video Title
- **Channel Name**: Example Channel
- **Duration**: 3m 25s
- **Downloaded from**: [YouTube URL]
- **Size**: 25.23 MB
- **Thumbnail**: Displayed above the download button

---

### Screenshots:
![image](https://github.com/user-attachments/assets/925f0134-bf10-4aa0-ad4a-ea99465d830d)
![image](https://github.com/user-attachments/assets/a7a6a9ae-6cfa-4a7e-89c8-1a2f9943a9f7)

---

### Acknowledgments:
- [yt-dlp](https://github.com/yt-dlp/yt-dlp): A powerful YouTube video downloader and extractor.
- [Streamlit](https://streamlit.io/): For building the interactive web interface.
