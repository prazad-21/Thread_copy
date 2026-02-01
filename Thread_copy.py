import os
import shutil
import tkinter as tk
from tkinter import ttk, messagebox
from concurrent.futures import ThreadPoolExecutor

# Global flag -
is_cancelled = False 

def copy_file():
    global is_cancelled
    is_cancelled = False 

    source = entry_src.get().strip()
    desti = entry_des.get().strip()

    if not os.path.exists(source):
        root_window.after(0, lambda: messagebox.showwarning("Error", "Source path is not valid"))
        return

    files = []
    for root, dirs, filename in os.walk(source):
        for f in filename:
            files.append(os.path.join(root, f))

    total_files = len(files)
    if total_files == 0:
        root_window.after(0, lambda: messagebox.showwarning("Error", "Folder is empty"))
        return

    root_window.after(0, lambda: progress.config(maximum=total_files, value=0))

    for index, file_path in enumerate(files):
        if is_cancelled:
            root_window.after(0, lambda: label_status.config(text="Status: Stopped!", fg="red"))
            return
        
        try:
            rel_path = os.path.relpath(file_path, source)
            dest_path = os.path.join(desti, rel_path)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(file_path, dest_path)

            current_val = index + 1
            root_window.after(0, update_ui, current_val, total_files)

        except Exception as e:
            print(f'Error while copying {file_path}: {e}')

    if not is_cancelled:
        root_window.after(0, lambda: messagebox.showinfo("Success", "All files copied!"))

def stop_copy():
    global is_cancelled
    is_cancelled = True 
    label_status.config(text="Stopping... please wait", fg="orange")

def update_ui(current_val, total_files):
    progress['value'] = current_val
    label_status.config(text=f"Copying: {current_val}/{total_files}")

def start_thread():
    executor.submit(copy_file)

# --- UI Setup ---
root_window = tk.Tk()
root_window.title("Multi-thread Copying")
root_window.geometry("450x450")
root_window.config(padx=30, pady=30)

executor = ThreadPoolExecutor(max_workers=1)

tk.Label(root_window, text="Source Path", font=("Lato", 10, "bold")).pack(pady=5)
entry_src = tk.Entry(root_window, width=50, bg="#4E3C3C") 
entry_src.pack()

tk.Label(root_window, text="Destination Path", font=("Lato", 10, "bold")).pack(pady=5)
entry_des = tk.Entry(root_window, width=50, bg="#4E3C3C")
entry_des.pack()

progress = ttk.Progressbar(root_window, orient="horizontal", length=350, mode="determinate")
progress.pack(pady=30)

label_status = tk.Label(root_window, text="Status: Waiting for input...", font=('Arial', 9, 'italic'))
label_status.pack()

btn_start = tk.Button(root_window, text="Start Copying", command=start_thread, 
                      bg="#2196F3", fg="white", width=20, height=2, font=('Arial', 10, 'bold'))
btn_start.pack(pady=10)

btn_stop = tk.Button(root_window, text="STOP COPYING", command=stop_copy, 
                     bg="#f44336", fg="white", font=('Arial', 10, 'bold'))
btn_stop.pack(pady=10)

root_window.mainloop()
