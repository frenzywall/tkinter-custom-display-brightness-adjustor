import tkinter as tk
import subprocess

def set_brightness(value):
    monitor_name = subprocess.check_output("xrandr | grep ' connected' | cut -f1 -d ' '", shell=True).decode().strip()
    brightness_level = float(value)
    subprocess.call(f"xrandr --output {monitor_name} --brightness {brightness_level}", shell=True)

root = tk.Tk()
root.title("Adjust Brightness")


tk.Label(root, text="Brightness Level").pack()


slider = tk.Scale(root, from_=0.5, to=1.0, orient=tk.HORIZONTAL, resolution=0.01, command=set_brightness)
slider.set(0.75)  
slider.pack()

root.mainloop()

