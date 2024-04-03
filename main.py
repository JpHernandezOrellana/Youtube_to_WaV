from pytube import YouTube
import os
import moviepy.editor as mp

# URL del video de YouTube
url = "https://www.youtube.com/watch?v=hnbBppSN1cY&list=LL&index=2"

# Descargar el video con la mejor calidad de audio
yt = YouTube(url)
video = yt.streams.filter(only_audio=True).order_by('abr').last()
print("Descargando...")
output_file = video.download(output_path=".", filename="audio")

# Verificar si el archivo se descargó correctamente
if not os.path.exists(output_file):
    print("Error: No se pudo descargar el archivo de audio.")
    exit()

# Convertir el video a formato WAV
print("Convirtiendo a WAV...")
clip = mp.AudioFileClip(output_file)
clip.write_audiofile("audio.wav")

# Eliminar el archivo de audio original
os.remove(output_file)

print("¡Descarga y conversión completadas!")
print("¡Descarga y conversión completadas!")