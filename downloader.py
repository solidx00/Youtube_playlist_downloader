import os
import yt_dlp
import sys

from utils import *

def scarica_playlist(link_playlist, cartella_base, formato_audio):
    try:
        print("🔍 Recupero info playlist...")
        with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
            info = ydl.extract_info(link_playlist, download=False)
            titolo_playlist = info.get('title', 'Playlist_Sconosciuta')
            titolo_playlist = sanitize_nome(titolo_playlist)
    except Exception as e:
        print(f"❌ Errore nel recupero info playlist: {e}")
        return

    cartella_output = os.path.join(cartella_base, f"{titolo_playlist}")
    os.makedirs(cartella_output, exist_ok=True)
    print(f"📁 Cartella di destinazione: {cartella_output}")

    try:
        opzioni = get_opzioni_output(cartella_output, formato_audio.lower())
        with yt_dlp.YoutubeDL(opzioni) as ydl:
            print("⬇️ Inizio download...")
            ydl.download([link_playlist])
            print(f"✅ Download della playlist in {formato_audio} completato!")
    except ValueError as ve:
        print(f"❗ {ve}")
    except Exception as e:
        print(f"❌ Errore durante il download: {e}")

# ESEMPIO DI USO:
if __name__ == "__main__":
    link = input("🔗 Inserisci il link della playlist YouTube: ").strip()
    if not link:
        print("❗ Link della playlist non valido.")
        sys.exit(1)
    formato_input = input("🎧 In quale formato vuoi scaricare? (mp3 / wav / flac) [default: mp3]: ").lower()
    if formato_input == "":
        formato = "mp3"
    elif formato_input in {"mp3", "wav", "flac"}:
        formato = formato_input
    else:
        print("❌ Formato non valido. Puoi scegliere solo tra: mp3, wav o flac.")
        sys.exit(1)

    #base_dir = r"C:\Users\franc\Documents\Youtube_Playlist_Converter\output"
     # 📁 Directory 'output' creata automaticamente nella cartella del progetto
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(base_dir, exist_ok=True)
    
    scarica_playlist(link, base_dir, formato)