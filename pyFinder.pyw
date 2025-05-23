import os
import fitz  # PyMuPDF
import threading
import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import pyautogui
import time
import subprocess

stop_search_flag = threading.Event()
selected_folder = None
DEFAULT_FOLDER = os.path.dirname(os.path.abspath(__file__))

def is_valid_file(file):
    name = os.path.basename(file)
    return (
        file.lower().endswith(".pdf")
        and not name.startswith("~$")
        and not name.startswith(".")
        and not name.startswith("._")
    )

def search_pdf_files(base_folder, keywords, progress_callback=None, result_callback=None, finish_callback=None):
    all_files = []

    for root, dirs, files in os.walk(base_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if is_valid_file(file_path):
                all_files.append(file_path)

    all_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    total = len(all_files)

    current_index = 0

    for index, file_path in enumerate(all_files, start=1):
        if stop_search_flag.is_set():
            break

        current_index = index
        if progress_callback:
            progress_callback(index, total)

        try:
            doc = fitz.open(file_path)
            snippets = []
            for page in doc:
                lines = page.get_text("text").splitlines()
                for line in lines:
                    line_lower = line.lower()
                    if all(k in line_lower for k in keywords):
                        snippets.append(line.strip())
            if snippets and result_callback:
                result_callback(file_path, snippets)
        except Exception as e:
            print(f"❗ Error reading {file_path}: {e}")

    # Ensure final update after loop ends
    if finish_callback:
        finish_callback(stop_search_flag.is_set(), total)

def finish_ui_update(was_stopped, total):
    if was_stopped:
        progress_label.config(text="Search stopped.")
    else:
        progress_label.config(text=f"Scanned {total} files.")
        progress["value"] = 100
    root.update_idletasks()

def select_file_and_press_space(file_path):
    try:
        if not os.path.isfile(file_path):
            print(f"❗ File does not exist: {file_path}")
            return
        file_path = os.path.normpath(file_path)
        print(f"Running command: explorer /select,\"{file_path}\"")
        subprocess.Popen(f'explorer /select,"{file_path}"', shell=True)
        time.sleep(0.5)
        pyautogui.press('space')
    except Exception as e:
        print(f"❗ Failed to open file location: {e}")

def update_progress(current, total):
    progress["value"] = (current / total) * 100
    progress_label.config(text=f"Scanning {current}/{total} files...")
    root.update_idletasks()

def display_result(file_path, snippets):
    file_path = os.path.abspath(os.path.normpath(file_path))

    if not os.path.exists(file_path):
        print(f"⚠ File no longer exists: {file_path}")
        return

    file_label = tk.Label(
        result_frame,
        text=file_path,
        fg="white",
        bg="#444",
        font=("Helvetica", 12, "bold"),
        cursor="hand2",
        anchor="w",
        padx=10,
        pady=6
    )
    file_label.pack(fill=tk.X, pady=(6, 2))
    file_label.bind("<Button-1>", lambda e, path=file_path: select_file_and_press_space(path))

    for snippet in snippets:
        snippet_label = tk.Label(
            result_frame,
            text="  " + snippet,
            fg="#dddddd",
            bg="#2e2e2e",
            font=("Helvetica", 11),
            justify="left",
            anchor="w",
            wraplength=1100,
            padx=20
        )
        snippet_label.pack(fill=tk.X, pady=2)

    root.update_idletasks()

def start_search(event=None):
    stop_search_flag.clear()
    folder_path = selected_folder or DEFAULT_FOLDER
    raw_keywords = keyword_var.get().strip()

    if not raw_keywords:
        messagebox.showerror("Error", "Please enter keyword(s).")
        return

    keywords = [k.strip().lower() for k in raw_keywords.split(",") if k.strip()]

    clear_results(keep_keyword=True)
    progress["value"] = 0
    progress_label.config(text="Starting search...")

    thread = threading.Thread(target=search_pdf_files, args=(
        folder_path,
        keywords,
        update_progress,
        display_result,
        lambda stopped, total: root.after(0, finish_ui_update, stopped, total)
    ))
    thread.start()

def stop_search():
    stop_search_flag.set()
    progress_label.config(text="Search stopped.")

def clear_results(keep_keyword=False):
    for widget in result_frame.winfo_children():
        widget.destroy()
    progress["value"] = 0
    progress_label.config(text="Results cleared.")
    if not keep_keyword:
        keyword_var.set("")

def choose_folder():
    global selected_folder
    folder = filedialog.askdirectory(initialdir=DEFAULT_FOLDER)
    if folder:
        selected_folder = folder
        folder_label.config(text=f"📁 {folder}")
    else:
        selected_folder = None
        folder_label.config(text=f"📁 {DEFAULT_FOLDER}")

# --- GUI Setup ---
root = tk.Tk()
root.title("PDF Keyword Search")
root.geometry("1200x800")
root.configure(bg="#2e2e2e")

style = ttk.Style()
style.theme_use("default")
style.configure("TLabel", background="#2e2e2e", foreground="white")
style.configure("TButton", background="#444", foreground="white", font=("Helvetica", 12))
style.configure("TProgressbar", background="#5cb85c", troughcolor="#1e1e1e", bordercolor="#1e1e1e")
style.configure("Vertical.TScrollbar",
                background="#444", darkcolor="#333", lightcolor="#444",
                troughcolor="#2e2e2e", bordercolor="#2e2e2e", arrowcolor="white")

# --- Top Bar ---
top_bar = tk.Frame(root, bg="#2e2e2e")
top_bar.pack(fill=tk.X, padx=10, pady=5)

folder_button = tk.Button(top_bar, text="Select Folder", command=choose_folder, bg="#444", fg="white", font=("Helvetica", 12))
folder_button.pack(side=tk.LEFT)

folder_label = tk.Label(top_bar, text=f"📁 {DEFAULT_FOLDER}", bg="#2e2e2e", fg="white", font=("Helvetica", 12))
folder_label.pack(side=tk.LEFT, padx=10)

keyword_var = tk.StringVar()
keyword_entry = tk.Entry(
    top_bar,
    textvariable=keyword_var,
    font=("Helvetica", 12),
    width=40,
    bg="#444444",
    fg="white",
    insertbackground="white",
    highlightbackground="#555",
    highlightcolor="#888",
    relief=tk.FLAT
)
keyword_entry.pack(side=tk.LEFT, padx=10)
keyword_entry.bind("<Return>", start_search)

search_button = tk.Button(top_bar, text="Search", command=start_search, bg="#555", fg="white", font=("Helvetica", 12))
stop_button = tk.Button(top_bar, text="Stop", command=stop_search, bg="#800000", fg="white", font=("Helvetica", 12))
clear_button = tk.Button(top_bar, text="Clear", command=clear_results, bg="#444", fg="white", font=("Helvetica", 12))

search_button.pack(side=tk.LEFT, padx=5)
stop_button.pack(side=tk.LEFT, padx=5)
clear_button.pack(side=tk.LEFT, padx=5)

# --- Scrollable Results Area ---
result_container = tk.Frame(root, bg="#2e2e2e")
result_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(result_container, bg="#2e2e2e", highlightthickness=0)
scrollbar = ttk.Scrollbar(result_container, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

scrollable_frame = tk.Frame(canvas, bg="#2e2e2e")
window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

def on_canvas_resize(event):
    canvas.itemconfig(window_id, width=event.width)

scrollable_frame.bind("<Configure>", on_frame_configure)
canvas.bind("<Configure>", on_canvas_resize)

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)
canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))

result_frame = scrollable_frame

# --- Progress Bar ---
progress_label = tk.Label(root, text="", fg="white", bg="#2e2e2e", font=("Helvetica", 11))
progress_label.pack(pady=(2, 1))

progress = ttk.Progressbar(root, orient="horizontal", length=800, mode="determinate")
progress.pack(pady=(0, 8))

keyword_entry.focus_set()
root.mainloop()

# --- Working code V1.6 ---
