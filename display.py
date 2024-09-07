import tkinter as tk
import subprocess

def set_brightness(value):
    monitor_name = subprocess.check_output("xrandr | grep ' connected' | cut -f1 -d ' '", shell=True).decode().strip()
    brightness_level = float(value)
    subprocess.call(f"xrandr --output {monitor_name} --brightness {brightness_level}", shell=True)

root = tk.Tk()
root.title("Adjust Brightness")
root.geometry("400x150") 
root.config(bg="#2e3f4f")  

title_label = tk.Label(root, text="Brightness Control", font=("Helvetica", 16, "bold"), fg="white", bg="#2e3f4f")
title_label.pack(pady=10)

slider_label = tk.Label(root, text="Brightness Level", font=("Helvetica", 12), fg="white", bg="#2e3f4f")
slider_label.pack(pady=5)
slider = tk.Scale(root, from_=0.1, to=1.0, orient=tk.HORIZONTAL, resolution=0.01, command=set_brightness,
fg="#ffffff", bg="#3b4c5a", highlightbackground="#3b4c5a", troughcolor="#4e6270", length=250)
slider.set(0.75)  
slider.pack(pady=5)

root.mainloop()
