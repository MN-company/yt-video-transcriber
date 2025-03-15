r![title](https://github.com/MN-company/yt-video-transcriber/blob/main/title.jpeg)  

# 🎯 Objective  
This project was born from a **personal need**: enabling AI to process videos seamlessly. Inspired by **Gemini’s** ability to analyze YouTube videos, I created this tool to make the process **universal**.  

The **key principle**? **Automation**. I wanted to make it as **simple and efficient** as possible. 🚀  

---

# 🎬 Requirements  
- **FFMPEG**: Download and install it from the official [FFMPEG website](https://www.ffmpeg.org).  
- **Diarization Model Access**: Unlock the diarization model by accepting the terms and conditions on Hugging Face before use.  

---

# ⚡ Colab Execution  
For those who don’t have a powerful machine, I recommend running the code on Google Colab.  

- You can download the Colab script from the repo or go directly to this [link](https://colab.research.google.com/drive/1HnjENO6ZjD2l5M782YvucylIdYT8UV2i?usp=sharing) to create a copy (or use the provided code directly).  

# 🏠 Local Setup  
### 📥 1. Clone the repository  
```bash
git clone https://github.com/MN-company/yt-video-transcriber.git && cd yt-video-transcriber
```
### 🔧 2. Install dependencies  
```bash
pip install -r requirements.txt
```
### ▶️ 3. Run the script with flags  
```bash
python3 main.py 
```

## Uso del modello
```
[link] -[FLAG] "value"
```
- `-h`, `--help` → print this message
- `-d`, `--diarization`→ Enables diarization 
- `-t`, `-token` → Replaces the default env setting for the Hugging Face token  
- `-f,`  `--format`→ Replaces the default env setting for the format of the downloaded video
- `-a`,  `--whisper_model`→ Replaces the default env setting fot the Whisper model (need to be compatible with Insane Faster Whisper) 
- `-b`,  `--diarization_model`→ Replaces the default env setting fot the diarization model (need to be compatible with Insane Faster Whisper)
- `--num_speaker` → Sets the number of speakers  
- `-p`,  `--path` → Specifies the output path
- `--task` → Specifies the task the model needs to do

# Features
- [Support for other websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) ⚠️ I haven't tested other websites yet
- CLI mode
- GUI mode (it's basic and it really sucks, but it's a start)
- Transcription with [Insanly faster Whisper](https://github.com/Vaibhavs10/insanely-fast-whisper)
- Diarization
- Youtube Playlist and batch download
- Translating videos

## 🚀 Roadmap  

| Feature    | Status | Notes |
|------------|--------|----------------------------|
| **GUI** | 📅 Planned | Expected in **6.0** |
| **Open-source AI for video summarization** | 📅 Planned |
| **File management improvements** | 🔄 Work in progress |
| **Parallel download for long videos** | 🔄 Work in progress |
| **Parallel transcription** | 🔄 Work in progress |
| **Improved playlist handling** | 🔄 Work in progress | **YT-DLP usage** |
| **Output file named after video** | 🔄 Work in progress |
| **Custom formats & Whisper settings** | 🔄 Work in progress |

---
