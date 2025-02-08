![title](https://github.com/MN-company/yt-video-transcriber/blob/main/title.jpeg)
# Objective
This project was born out of a need I had to make Ai understand video. Since they could not take the video as input, I thought of this code to transcribe it. The goal then is to download a video from YouTube and transcribe it in as little time as possible (with a good amount of accuracy). The use cases are many, which is why I wanted to expand this code and make it public.

## Colab execution
For those who do not have a powerful machine, my advice is to run the code through Google Colab.
- You can download the Colab code from the repo or go to this [link](https://colab.research.google.com/drive/1HnjENO6ZjD2l5M782YvucylIdYT8UV2i?usp=sharing) and create a copy (or use the proposed code directly)

# Local Setup
Many people do not like having to rely on Google for their needs, and I understand that. However, I prefer to work on the cloud version with Colab because it is much more convenient for me and it is executable on all machines being a cloud solution. As the versions of Colab are released, I will update the repo code to run it locally.
- Download the repo locally 
```
git clone https://github.com/MN-company/yt-video-transcriber.git
```
- Run the requirments.txt
```
pip install -r /path/to/requirements.txt
```
- Run the file "main.py"
```
python3 /path/to/main.py
```
## If you have not already done so, install FFMPEG
### For Linux
```
sudo apt install ffmpeg
```
### For MacOS
```
brew install ffmpeg
```
### For Windows
Use the official guide on their [website](https://www.ffmpeg.org)

---
# List of the features
| Feature    | Will be implemented? | Working on it? | Release |
| -------- | ------- | -------- | -------- |
| GUI  | ⚠️ | ❌ | 5.0 |
| Other websites | ❌ | ❌ | ❌ |
| Video list as input    | ✅    | ✅ | 3.0 |
| Open source AI that summarizes videos    | ✅    | ❌ | 4.0 |
| Full CLI mode    | ✅    | ✅ | 3.0 |
| Diarization    | ✅    | ❌ | 4.0 |
| Universal transcription | ✅ | Done | 1.0 |
| Faster Whisper | ✅ | Done | 2.0 |
| Diarization | ✅ | ❌ | 4.0 |
