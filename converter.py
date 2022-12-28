import os
import sys
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image

def select_folder():
  global directory
  root = tk.Tk()
  root.withdraw()
  directory = filedialog.askdirectory()
  label['text'] = f'Selected directory: {directory}'

def convert_images():
  fmt = custom_format.get()
  if not fmt:
    fmt = output_format.get()

  new_folder = os.path.join(directory, 'converted images')
  if not os.path.exists(new_folder):
    os.makedirs(new_folder)

  num_files = len(os.listdir(directory))
  progress_bar['maximum'] = num_files
  progress_bar['value'] = 0

  for i, filename in enumerate(os.listdir(directory)):
    try:
      img = Image.open(os.path.join(directory, filename))
      img.save(os.path.join(new_folder, os.path.splitext(filename)[0] + '.' + fmt))
    except OSError:
      continue

    progress_bar['value'] = i + 1
    progress_bar.update()

  final_msg['text'] = f'All images converted to {fmt} format and saved in the "converted images" folder!'

def exit_program(root):
  root.destroy()
  sys.exit()

root = tk.Tk()
root.wm_iconbitmap('icon.ico')
root.title('Image Converter')
root.geometry('600x400')

main_frame = tk.Frame(root)
main_frame.pack()

intro = tk.Label(main_frame, text='Welcome to NAGF Image Converter\n This program will convert all the images contained within the selected folder to the desired format')
intro.pack(pady=(0, 25))

label = tk.Label(main_frame, text='No directory selected. Please select a root directory')
label.pack(pady=(0, 5))

select_button = tk.Button(main_frame, text='Select folder', command=select_folder)
select_button.pack(pady=(0, 15))

choose_msg = tk.Label(main_frame, text='Choose an output format')
choose_msg.pack(pady=(0, 5))

formats = ['jpg', 'jpeg', 'gif', 'png', 'bmp', 'tiff', 'webp']

output_format = tk.StringVar(main_frame)
output_format.set(formats[0])

format_menu = ttk.Combobox(main_frame, textvariable=output_format, values=formats)
format_menu.pack(pady=(0, 15))

type_msg = tk.Label(main_frame, text='Optional: Type a custom output format (without the "." dot)')
type_msg.pack(pady=(0, 5))

custom_format = tk.StringVar(main_frame)
custom_entry = tk.Entry(main_frame, textvariable=custom_format)
custom_entry.pack(pady=(0, 15))

convert_button = tk.Button(main_frame, text='Convert images', command=convert_images)
convert_button.pack(pady=(0, 5))

progress_bar = ttk.Progressbar(main_frame, orient='horizontal', length=200, mode='determinate')
progress_bar.pack(pady=(0, 5))

final_msg = tk.Label(main_frame, text='')
final_msg.pack(pady=(0, 15))

exit_button = tk.Button(main_frame, text='Exit', command=lambda: exit_program(main_frame))
exit_button.pack()

root.protocol("WM_DELETE_WINDOW", lambda: exit_program(root))

main_frame.mainloop()