import os
import subprocess
import yt_dlp
from dotenv import load_dotenv
import argparse
import logging

load_dotenv(".env")

HF_TOKEN      = os.environ.get("HF_TOKEN")
WHISPER_MODEL = os.environ.get("WHISPER_MODEL")
DIAR_MODEL    = os.environ.get("DIAR_MODEL")

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def download_audio(url, output_path="audio.mp3"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path.replace('.mp3', '')
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        logger.info(f"Download completato! Salvato come {output_path}")
    except Exception as e:
        logger.error(f"Errore durante il download: {e}")
        raise

def build_command(output_path, do_diarization):
    command_parts = [f"insanely-fast-whisper", f"--file-name '{output_path}'"]

    if do_diarization and HF_TOKEN:
        command_parts.append(f"--hf-token {HF_TOKEN}")

    if WHISPER_MODEL:
        command_parts.append(f"--model {WHISPER_MODEL}")

    if do_diarization and DIAR_MODEL:
        command_parts.append(f"--diarization_model {DIAR_MODEL}")

    return " ".join(command_parts)

def transcribe_audio(output_path, do_diarization):
    command = build_command(output_path, do_diarization)
    logger.info("Eseguo il comando:")
    logger.info(command)
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        logger.info("Trascrizione completata con successo!")
        logger.info("Output:\n" + result.stdout)
    except subprocess.CalledProcessError as e:
        logger.error("Errore durante l'esecuzione di insanely-fast-whisper:")
        logger.error(e.stderr)
        raise

def main():
    parser = argparse.ArgumentParser(description="Scarica e trascrivi.")
    parser.add_argument("url", nargs="?", default=None, help="URL del video YouTube")
    parser.add_argument("-d", "--diarization", action="store_true", help="Abilita la diarizzazione")
    parser.add_argument("-o", "--output", default="audio.mp3", help="Nome del file audio in output (default: audio.mp3)")

    args, unknown = parser.parse_known_args()

    invalid_kernel_prefix = "/root/.local/share/jupyter/runtime/"

    if not args.url or args.url.startswith(invalid_kernel_prefix):
        args.url = input("Inserisci l'URL del video YouTube: ").strip()

    try:
        download_audio(args.url, args.output)
        transcribe_audio(args.output, args.diarization)
    except Exception as e:
        logger.error("Processo interrotto a causa di un errore.")
        exit(1)

if __name__ == "__main__":
    main()

