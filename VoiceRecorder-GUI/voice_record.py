import tkinter as tk
import sounddevice as sd
import soundfile as sf

# Function to record audio
def record_voice():
    fs = 44100       # Sample rate
    duration = 5     # Record for 5 seconds
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()        # Wait until recording is finished
    sf.write("output.flac", recording, fs)  # Save as audio file
    status_label.config(text="Recording saved as output.flac")

# Create main window
root = tk.Tk()
root.title("Simple Voice Recorder")

# Label
label = tk.Label(root, text="🎙️ Voice Recorder", font=("Arial", 16))
label.pack(pady=10)

# Button
record_button = tk.Button(root, text="Start Recording", command=record_voice)
record_button.pack(pady=10)

# Status message
status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=5)

# Run app
root.mainloop()
