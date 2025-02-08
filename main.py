import os
import yt_dlp
import torch

from transformers import pipeline
from transformers.utils import is_flash_attn_2_available

def download_youtube_audio(url, output_path="audio.mp3"):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            # Nel nome di output, togli .mp3 così `yt-dlp` non aggiunge doppio suffisso
            'outtmpl': output_path.replace('.mp3', '')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Download completato! Salvato come {output_path}")

        # Trascrizione dell'audio scaricato
        transcribe_audio(output_path)

    except Exception as e:
        print(f"Errore durante il download: {e}")

def transcribe_audio(audio_path):
    try:
        # Scegli l'implementazione dell'attenzione (Flash o SDPA)
        attn_impl = (
            "flash_attention_2" if is_flash_attn_2_available()
            else "sdpa"
        )

        # Inizializza la pipeline con il modello desiderato
        pipe = pipeline(
            "automatic-speech-recognition",
            model="openai/whisper-large-v3",  # o "openai/whisper-large-v2", ecc.
            torch_dtype=torch.float16,
            model_kwargs={"attn_implementation": attn_impl},
        )

        print("Trascrizione in corso...")
        outputs = pipe(
            audio_path,
            chunk_length_s=30,
            batch_size=24,
            return_timestamps=True,
        )

        # 'outputs' in genere è un dict o una list di segmenti (dipende dalla versione di Transformers).
        # Se vuoi il testo unito:
        # (in Transformers >=4.27 di solito outputs contiene "text" a top-level
        #  o una lista di "chunks" con testo e timestamps)
        if isinstance(outputs, dict) and "text" in outputs:
            text = outputs["text"]
        else:
            # Se outputs è una lista di segmenti con "text", uniscili
            text_segments = [seg["text"] for seg in outputs["chunks"]]
            text = " ".join(text_segments)

        # Salviamo il testo in un file
        transcript_path = audio_path.replace(".mp3", ".txt")
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Trascrizione completata! Salvata in {transcript_path}")

    except Exception as e:
        print(f"Errore nella trascrizione: {e}")

if __name__ == "__main__":
    video_url = input("Inserisci il link del video di YouTube: ")
    download_youtube_audio(video_url)
