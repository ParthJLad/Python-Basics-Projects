# Photo album application

import tkinter as tk
import time
from PIL import Image, ImageTk

# Main application window
root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

# List of Image Paths
image_paths = [
    r"C:\Pictures\Di Marrige\DSC_5317.JPG",
    r"C:\Pictures\Di Marrige\DSC_5316.JPG",
    r"C:\Pictures\Di Marrige\DSC_5311.JPG",
    r"C:\Pictures\Di Marrige\DSC_5298.JPG",
    r"C:\Pictures\Di Marrige\DSC_5299.JPG",
    r"C:\Pictures\Di Marrige\DSC_5324.JPG",
]

# Image processing
image_size = (700, 700)
images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size)
    images.append(img)  # Adding each image in the list

# Convert PIL images into Tkinter Compatible Image
final_images = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)

# Label widgets to keep photos
image_label = tk.Label(root)
image_label.pack(pady=30)

# Slideshow Function
def start_sideshow():
    for photo in final_images:
        image_label.config(image=photo)
        image_label.image=photo
        root.update()
        time.sleep(2)

# Button
play_button = tk.Button(
    root,
    text="Play the SlideShow",
    font=("Times New Roman", 18),
    command=start_sideshow
)

play_button.pack(pady=40)

# Keep to open window
root.mainloop()