import tkinter as tk
from tkinter import filedialog
import sounddevice as sd
import numpy as np
import wave

class AudioRecorderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Audio Recorder")

        self.record_button = tk.Button(self.master, text="Record", command=self.start_recording)
        self.record_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_recording, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.save_button = tk.Button(self.master, text="Save As", command=self.save_as, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.audio_display = tk.Label(self.master, text="Ready", font=("Helvetica", 16))
        self.audio_display.pack(pady=20)

        self.audio_stream = None
        self.audio_data = []

    def start_recording(self):
        self.record_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.DISABLED)
        self.audio_display.config(text="Recording...")

        self.audio_stream = sd.InputStream(callback=self.audio_callback, channels=2, dtype='int16')
        self.audio_stream.start()

    def pause_recording(self):
        if self.audio_stream:
            self.audio_stream.stop()
            self.record_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.save_button.config(state=tk.NORMAL)
            self.audio_display.config(text="Recording paused.")

    def stop_recording(self):
        if self.audio_stream:
            self.audio_stream.stop()
            self.audio_stream.close()
            self.record_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.DISABLED)
            self.save_button.config(state=tk.NORMAL)
            self.audio_display.config(text="Recording stopped.")

    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
        if file_path:
            self.save_audio(file_path)

    def save_audio(self, filename):
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(44100)
            wf.writeframes(np.concatenate(self.audio_data))
        self.audio_display.config(text=f"Audio saved as {filename}")

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(f"Error in audio stream: {status}")
        else:
            self.audio_data.append(indata.copy())


if __name__ == "__main__":
    root = tk.Tk()
    app = AudioRecorderApp(root)
    root.mainloop()
