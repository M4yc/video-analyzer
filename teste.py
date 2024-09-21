import openai
import ffmpeg
import pytubefix
import sys
import os


# Função para baixar o áudio do YouTube
def download_audio(url, output_file):
    yt = pytubefix.YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    audio_path = stream.download(filename=output_file)
    return audio_path

# Função para converter o áudio baixado para WAV
def convert_to_wav(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, format='wav', loglevel="error").run()

# Main
if __name__ == "__main__":
    # Pegar a URL do vídeo do YouTube a partir dos argumentos da linha de comando
    if len(sys.argv) < 2:
        print("Por favor, forneça a URL do vídeo do YouTube.")
        sys.exit(1)

    url = sys.argv[1]
    audio_filename = "audio.mp4"  # Arquivo baixado
    wav_filename = "audio.wav"  # Arquivo convertido

    # 1. Baixar o áudio do vídeo do YouTube
    print("Baixando o áudio do vídeo...")
    audio_path = download_audio(url, audio_filename)
    print(f"Áudio baixado: {audio_path}")

    # 2. Converter o áudio para formato WAV
    print("Convertendo o áudio para WAV...")
    convert_to_wav(audio_path, wav_filename)
    print(f"Áudio convertido para WAV: {wav_filename}")

