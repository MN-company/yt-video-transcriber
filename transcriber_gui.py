import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QCheckBox, QTextEdit, QProgressBar, QFileDialog)
from PyQt6.QtCore import Qt, QThread, pyqtSignal
import os
from core import TranscriptionService, TranscriptionError
import logging

class TranscriptionWorker(QThread):
    progress = pyqtSignal(str)
    error = pyqtSignal(str)
    finished = pyqtSignal(str)  # Now emits the transcription result

    def __init__(self, url, output_path, do_diarization):
        super().__init__()
        self.url = url
        self.output_path = output_path
        self.do_diarization = do_diarization
        self.service = TranscriptionService()

    def run(self):
        try:
            self.service.set_progress_callback(lambda msg: self.progress.emit(msg))
            result = self.service.process(self.url, self.output_path, self.do_diarization)
            self.finished.emit(result)
        except TranscriptionError as e:
            self.error.emit(str(e))

class TranscriberGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Video Transcriber")
        self.setMinimumWidth(600)
        self.initUI()

    def initUI(self):
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # URL input
        url_layout = QHBoxLayout()
        url_label = QLabel("YouTube URL:")
        self.url_input = QLineEdit()
        url_layout.addWidget(url_label)
        url_layout.addWidget(self.url_input)
        layout.addLayout(url_layout)

        # Output file selection
        file_layout = QHBoxLayout()
        self.file_path = QLineEdit("audio.mp3")
        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_output)
        file_layout.addWidget(QLabel("Output File:"))
        file_layout.addWidget(self.file_path)
        file_layout.addWidget(browse_button)
        layout.addLayout(file_layout)

        # Diarization checkbox
        self.diarization = QCheckBox("Enable Speaker Diarization")
        layout.addWidget(self.diarization)

        # Progress bar and status
        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.progress_bar)

        # Status text area
        self.status_text = QTextEdit()
        self.status_text.setReadOnly(True)
        self.status_text.setMinimumHeight(100)
        layout.addWidget(self.status_text)

        # Transcribe button
        self.transcribe_button = QPushButton("Transcribe")
        self.transcribe_button.clicked.connect(self.start_transcription)
        layout.addWidget(self.transcribe_button)

    def browse_output(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save Audio File",
            "",
            "Audio Files (*.mp3);;All Files (*)"
        )
        if file_name:
            self.file_path.setText(file_name)

    def update_status(self, message):
        self.status_text.append(message)

    def handle_error(self, error_message):
        self.status_text.append(f"Error: {error_message}")
        self.progress_bar.setValue(0)
        self.transcribe_button.setEnabled(True)

    def start_transcription(self):
        url = self.url_input.text().strip()
        if not url:
            self.update_status("Please enter a YouTube URL")
            return

        self.transcribe_button.setEnabled(False)
        self.progress_bar.setMaximum(0)
        self.status_text.clear()

        self.worker = TranscriptionWorker(
            url,
            self.file_path.text(),
            self.diarization.isChecked()
        )
        self.worker.progress.connect(self.update_status)
        self.worker.error.connect(self.handle_error)
        self.worker.finished.connect(self.on_transcription_complete)
        self.worker.start()

    def on_transcription_complete(self, result):
        self.status_text.append("\nTranscription Result:\n" + result)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(100)
        self.transcribe_button.setEnabled(True)

def main():
    app = QApplication(sys.argv)
    window = TranscriberGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()