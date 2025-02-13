import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytubefix import YouTube
from yt_dlp import YoutubeDL
import instaloader

# caminho da pasta de downloads do Windows
DOWNLOADS_PATH = os.path.join(os.path.expanduser("~"), "Downloads")

def download_video(url, output_path=DOWNLOADS_PATH): 
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        messagebox.showinfo("Sucesso", f"Download do vídeo do Youtube concluído: {yt.title}")
        progress.stop()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo: {e}")

def download_audio(url, output_path=DOWNLOADS_PATH): 
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        file_path = stream.download(output_path)
        base, ext = os.path.splitext(file_path)
        new_file = base + ".mp3"
        os.rename(file_path, new_file)
        messagebox.showinfo("Sucesso", f"Download do áudio concluído: {yt.title}")
        progress.stop()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o áudio: {e}")

def download_facebook(url, output_path=DOWNLOADS_PATH):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Download do vídeo do Facebook concluído")
        progress.stop()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo do Facebook: {e}")

def download_twitter(url, output_path=DOWNLOADS_PATH):
    try:
        ydl_opts = {
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Sucesso", "Download do vídeo do Twitter concluído")
        progress.stop()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo do Twitter: {e}")

def download_instagram(url, output_path=DOWNLOADS_PATH):
    try:
        L = instaloader.Instaloader(dirname_pattern=output_path)
        post = instaloader.Post.from_shortcode(L.context, url.split("/")[-2])
        L.download_post(post, target=output_path)
        messagebox.showinfo("Sucesso", "Download do vídeo do Instagram concluído")
        progress.stop()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao baixar o vídeo do Instagram: {e}")

def start_download():
    url = url_entry.get()
    platform = platform_var.get()
    progress.start()
    if not url:
        messagebox.showwarning("Aviso", "Digite uma URL válida!")
        return
    
    if platform == "youtube":
        if var.get() == "video":
            download_video(url)
        elif var.get() == "audio":
            download_audio(url)
        else:
            messagebox.showwarning("Aviso", "Escolha um formato para o download!")
    elif platform == "facebook":
        download_facebook(url)
    elif platform == "twitter":
        download_twitter(url)
    elif platform == "instagram":
        download_instagram(url)
    else:
        messagebox.showwarning("Aviso", "Escolha uma plataforma válida!")

# estilo
root = tk.Tk()
tk.Label(root, text="URL do vídeo:", font=("Arial", 12, "bold"), fg="blue").pack(pady=5)
root.title("Media Downloader")
root.geometry("500x400")

frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
frame.pack(pady=10)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="indeterminate")
progress.pack(pady=10)
progress.step(10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

platform_var = tk.StringVar(value="youtube")
tk.Radiobutton(root, text="YouTube", variable=platform_var, value="youtube").pack()
tk.Radiobutton(root, text="Facebook", variable=platform_var, value="facebook").pack()
tk.Radiobutton(root, text="Twitter", variable=platform_var, value="twitter").pack()
tk.Radiobutton(root, text="Instagram", variable=platform_var, value="instagram").pack()

var = tk.StringVar(value="video")
tk.Radiobutton(root, text="Vídeo", variable=var, value="video").pack()
tk.Radiobutton(root, text="Áudio", variable=var, value="audio").pack()

tk.Button(root, text="Baixar", command=start_download, bg="green", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

root.mainloop()