import os
import re

def sanitize_nome(nome):
    # Rimuove caratteri non validi per nomi di cartella su Windows
    return re.sub(r'[\\/*?:"<>|]', '', nome)

def get_opzioni_output(cartella_output, formato):
    if formato == 'mp3':
        return {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(cartella_output, '%(playlist_index)02d - %(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'postprocessor_args': ['-ar', '44100'],
            'prefer_ffmpeg': True,
            'quiet': False,
            'nocheckcertificate': True,
        }
    elif formato == 'wav':
        return {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(cartella_output, '%(playlist_index)02d - %(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
            }],
            'postprocessor_args': ['-ar', '44100'],
            'prefer_ffmpeg': True,
            'quiet': False,
            'nocheckcertificate': True,
        }
    elif formato == 'flac':
        return {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(cartella_output, '%(playlist_index)02d - %(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'flac',
            }],
            'postprocessor_args': ['-ar', '44100'],
            'prefer_ffmpeg': True,
            'quiet': False,
            'nocheckcertificate': True,
        }
    else:
        raise ValueError("Formato audio non supportato. Usa mp3, wav o flac.")