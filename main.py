from pytube import YouTube
import os
import moviepy.editor as mp

# URL del video de YouTube
url = "https://www.youtube.com/watch?v=hnbBppSN1cY&list=LL&index=1"

# Descargar el video
yt = YouTube(url)
video = yt.streams.filter(only_audio=True).first()
print("Descargando...")
output_file = video.download(output_path=".", filename="audio.mp4")

# Verificar si el archivo se descargó correctamente
if not os.path.exists(output_file):
    print("Error: No se pudo descargar el archivo de audio.")
    exit()

# Convertir el video a formato WAV
print("Convirtiendo a WAV...")
clip = mp.AudioFileClip("audio.mp4")
clip.write_audiofile("audio.wav")

# Eliminar el archivo de audio original
os.remove("audio.mp4")

print("¡Descarga y conversión completadas!")