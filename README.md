![title](https://github.com/MN-company/yt-video-transcriber/blob/main/title.jpeg)
# Objective
This project was born out of a need I had to make Ai understand video. Since they could not take the video as input, I thought of this code to transcribe it. The goal then is to download a video from YouTube and transcribe it in as little time as possible (with a good amount of accuracy). The use cases are many, which is why I wanted to expand this code and make it public.

## Colab execution
For those who do not have a powerful machine, my advice is to run the code through Google Colab.
- You can download the Colab code from the repo or go to this [link](https://colab.research.google.com/drive/1HnjENO6ZjD2l5M782YvucylIdYT8UV2i?usp=sharing) and create a copy (or use the proposed code directly)

### Local execution (We will release the local version when we have a completed Colab version)
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
# New future features
| Feature    | Will be implemented? | Working on it? |
| -------- | ------- | -------- |
| GUI  | ⚠️ (We are deciding on it)   | ❌ |
| Other websites | ❌ | ❌ |
| Video list as input    | ✅    | ✅ |
| Open source AI that summarizes videos    | ✅    | ❌ |
| Full CLI mode    | ✅    | ✅ |
| Diarization    | ✅    | ❌ |

# Implemented features
| Feature    | Release |
| -------- | ------- |
| Universal transcription | 1.0 |
| Faster Whisper | 2.0 |
| Video list as input | 3.0 |
| CLI Mode | 3.0 |
| AI that summarizes videos | 4.0 |
| Diarization | 4.0 |
| GUI | 5.0 |

