import tkinter as tk
import sounddevice as sd
import soundfile as sf
import numpy as np

# Globals
recording = None
fs = 44100
is_recording = False
start_frame = 0

def start_recording():
    global recording, is_recording, start_frame
    is_recording = True
    status_label.config(text="Recording... 🎙️")
    # Start recording with a large buffer
    recording = sd.rec(int(600 * fs), samplerate=fs, channels=2)
    start_frame = sd.get_stream().time * fs  # mark start time

def stop_recording():
    global recording, is_recording
    if is_recording:
        sd.stop()
        end_frame = int(sd.get_stream().time * fs)  # mark stop time
        # Slice only actual recorded frames
        audio_data = recording[:end_frame]
        sf.write("output.flac", audio_data, fs)
        status_label.config(text="Recording saved ✅")
        is_recording = False
    else:
        status_label.config(text="No recording in progress ❌")

# Tkinter GUI
root = tk.Tk()
root.title("Voice Recorder")

label = tk.Label(root, text="🎙️ Voice Recorder", font=("Arial", 16))
label.pack(pady=10)

start_btn = tk.Button(root, text="Start Recording", command=start_recording)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop Recording", command=stop_recording)
stop_btn.pack(pady=5)

status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=5)

root.mainloop()
