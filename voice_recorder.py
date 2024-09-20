from tkinter import *
import sounddevice as sd
import soundfile as sf

root = Tk()


def start():
    fs = 4800
    duration = 5
    recording = sd.rec(int(fs*duration), channels=2, samplerate=fs)
    sd.wait()
    return sf.write("my_audio_file.flac", recording, fs)


lbl = Label(root, text="Record your Voice : ")
lbl.grid(row=0, rowspan=5)
btn = Button(root, text="Start",  command=start).grid(
    row=0, column=2, columnspan=2, rowspan=2)

root.mainloop()
