import tkinter as tk
from tkinter import ttk
import subprocess


# Functions of each codec button
def convert_to_vp8():
    input_video = box_input_video_name.get()
    output_video = box_output_video_name.get()
    subprocess.run('ffmpeg -i '+input_video+' -c:v libvpx -b:v 1M -c:a libvorbis '+output_video, shell=True)


def convert_to_vp9():
    input_video = box_input_video_name.get()
    output_video = box_output_video_name.get()
    subprocess.run('ffmpeg -i ' + input_video + ' -c:v libvpx-vp9 ' + output_video, shell=True)


def convert_to_av1():
    input_video = box_input_video_name.get()
    output_video = box_output_video_name.get()
    subprocess.run('ffmpeg -i '+input_video+' -c:v libaom-av1 '+output_video, shell=True)


def convert_to_h265():
    input_video = box_input_video_name.get()
    output_video = box_output_video_name.get()
    subprocess.run('ffmpeg -i '+input_video+' -c:v libx265 '+output_video, shell=True)


# Create the window with the corresponding labels, boxes and buttons
window = tk.Tk()
window.title("Video converter")
window.config(width=400, height=300)

# control_input_video_name = ttk.Label(text="Insert input video path:")
label_input_video_name = ttk.Label(text="Insert video path to convert:")
label_input_video_name.place(x=20, y=20)

label_output_video_name = ttk.Label(text="Insert output video path:")
label_output_video_name.place(x=20, y=60)

box_input_video_name = ttk.Entry()
box_input_video_name.place(x=213, y=20, width=140)

box_output_video_name = ttk.Entry()
box_output_video_name.place(x=190, y=60, width=140)

converter_button = ttk.Button(text="Convert to VP8", command=convert_to_vp8)
converter_button.place(x=20, y=110)

converter_button = ttk.Button(text="Convert to VP9", command=convert_to_vp9)
converter_button.place(x=20, y=150)

converter_button = ttk.Button(text="Convert to AV1", command=convert_to_av1)
converter_button.place(x=20, y=190)

converter_button = ttk.Button(text="Convert to H265", command=convert_to_h265)
converter_button.place(x=20, y=230)

window.mainloop()
