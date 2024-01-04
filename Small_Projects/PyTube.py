from pytube import YouTube

def descargar_video(url):
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()

# Uso de la función
descargar_video('https://www.youtube.com/shorts/mRTkS66Aous')
