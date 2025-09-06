import tkinter as tk
import sounddevice as sd
import soundfile as sf

# Global variables
recording = None
fs = 44100
is_recording = False

def start_recording():
    global recording, is_recording
    is_recording = True
    status_label.config(text="Recording... 🎙️")
    recording = sd.rec(int(600 * fs), samplerate=fs, channels=2)  
    # 600 sec (10 min) max buffer, can stop earlier

def stop_recording():
    global recording, is_recording
    if is_recording:
        sd.stop()
        sf.write("output.flac", recording, fs)
        status_label.config(text="Recording saved as output.flac")
        is_recording = False
    else:
        status_label.config(text="No recording in progress")

# Create main window
root = tk.Tk()
root.title("Voice Recorder")

# Title Label
label = tk.Label(root, text="🎙️ Voice Recorder", font=("Arial", 16))
label.pack(pady=10)

# Buttons
start_btn = tk.Button(root, text="Start Recording", command=start_recording)
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop Recording", command=stop_recording)
stop_btn.pack(pady=5)

# Status Label
status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=5)

# Run App
root.mainloop()
