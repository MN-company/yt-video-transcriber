import os
import logging
import yt_dlp
import subprocess
import shlex
from typing import Optional, Callable
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv(".env")
r
class TranscriptionError(Exception):
    """Base exception for transcription errors"""
    pass

class DownloadError(TranscriptionError):
    """Raised when audio download fails"""
    pass

class WhisperError(TranscriptionError):
    """Raised when whisper transcription fails"""
    pass

@dataclass
class TranscriptionConfig:
    hf_token: Optional[str] = None
    whisper_model: Optional[str] = None
    diar_model: Optional[str] = None

class AudioDownloader:
    def __init__(self, progress_callback: Optional[Callable[[str], None]] = None):
        self.progress_callback = progress_callback

    def download(self, url: str, output_path: str = "audio.mp3") -> str:
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
            if self.progress_callback:
                self.progress_callback("Starting audio download...")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            if self.progress_callback:
                self.progress_callback(f"Download completed: {output_path}")
            return output_path
        except Exception as e:
            raise DownloadError(f"Failed to download audio: {str(e)}")

class WhisperTranscriber:
    def __init__(self, config: TranscriptionConfig, progress_callback: Optional[Callable[[str], None]] = None):
        self.config = config
        self.progress_callback = progress_callback

    def _build_command(self, file_path: str, do_diarization: bool) -> str:
        command_parts = ["insanely-fast-whisper", f"--file-name {shlex.quote(file_path)}"]

        if do_diarization and self.config.hf_token:
            command_parts.append(f"--hf-token {self.config.hf_token}")
        
        return " ".join(command_parts)

    def transcribe(self, file_path: str, do_diarization: bool = False) -> str:
        try:
            if self.progress_callback:
                self.progress_callback("Starting transcription...")

            command = self._build_command(file_path, do_diarization)
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                capture_output=True,
                text=True
            )

            if self.progress_callback:
                self.progress_callback("Transcription completed successfully!")

            return result.stdout
        except subprocess.CalledProcessError as e:
            raise WhisperError(f"Transcription failed: {e.stderr}")
        except Exception as e:
            raise WhisperError(f"Unexpected error during transcription: {str(e)}")

class TranscriptionService:
    def __init__(self, config: Optional[TranscriptionConfig] = None):
        self.config = config or TranscriptionConfig(
            hf_token=os.environ.get("HF_TOKEN"),
            whisper_model=os.environ.get("WHISPER_MODEL"),
            diar_model=os.environ.get("DIAR_MODEL")
        )
        self.progress_callback = None

    def set_progress_callback(self, callback: Callable[[str], None]) -> None:
        self.progress_callback = callback

    def cli_entry_point(self):
        """Command line interface entry point"""
        parser = argparse.ArgumentParser(description="Scarica e trascrivi.")
        parser.add_argument("url", nargs="?", default=None, help="URL del video YouTube")
        parser.add_argument("-d", "--diarization", action="store_true", help="Abilita la diarizzazione")
        parser.add_argument("-o", "--output", default="audio.mp3", help="Nome del file audio in output")

        args, unknown = parser.parse_known_args()

        if not args.url:
            args.url = input("Inserisci l'URL del video YouTube: ").strip()

        try:
            self.process(args.url, args.output, args.diarization)
        except TranscriptionError as e:
            logging.error(f"Processo interrotto: {str(e)}")
            exit(1)

    def process(self, url: str, output_path: str = "audio.mp3", do_diarization: bool = False) -> str:
        downloader = AudioDownloader(self.progress_callback)
        transcriber = WhisperTranscriber(self.config, self.progress_callback)

        try:
            audio_path = downloader.download(url, output_path)
            return transcriber.transcribe(audio_path, do_diarization)
        except (DownloadError, WhisperError) as e:
            raise TranscriptionError(str(e))