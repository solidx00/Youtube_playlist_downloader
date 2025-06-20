# 🎵 YouTube Playlist Audio Downloader

Uno script Python per scaricare una playlist da YouTube e convertire i brani in formato audio di alta qualità (FLAC, WAV o MP3). Ogni file viene salvato in una cartella dedicata con il titolo della playlist.

## 📦 Funzionalità

- Estrazione automatica del titolo della playlist
- Creazione automatica della cartella di destinazione
- Conversione audio in:
  - **FLAC**
  - **WAV** 
  - **MP3 a 320 kbps**
- Frequenza di campionamento forzata a 44100 Hz
- Compatibilità con YouTube e altri provider supportati da `yt_dlp`

---

## 🧩 Dipendenze

Assicurati di avere Python 3.7+ installato. Poi installa i seguenti pacchetti:

```bash
pip install yt-dlp
```

Inoltre, è necessario avere ffmpeg installato e accessibile nel PATH di sistema:

- Windows:
  Scarica da: https://ffmpeg.org/download.html
  Aggiungi la cartella bin/ al PATH di sistema.
  
- macOS (con Homebrew):
  ```bash
  brew install ffmpeg
  ```
  
- Linux (Debian/Ubuntu):
  sudo apt update && sudo apt install ffmpeg

## 📦 Come usarlo

- Clona o scarica questo repository.

- Apri un terminale nella cartella del progetto.

-Esegui lo script:

```bash
python downloader.py
```

-  Inserisci il link della playlist/traccia YouTube quando richiesto.

- I file audio verranno salvati in:
 
```lua
C:\Users\franc\Documents\Youtube_Playlist_Converter\output\<TitoloPlaylist>
```

## 🛠 Struttura del Progetto

```lua
📁 Youtube_Playlist_Converter/
├── downloader.py
├── utils.py
├── README.md
└── output/
    └── <TitoloPlaylist>/
        └── 01 - Nome brano.flac
```

## 🧑‍💻 Autore

Francesco Citeroni

🗓️ 2025

📧 francescociteroni.97@gmail.com
