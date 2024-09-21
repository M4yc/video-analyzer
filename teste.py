import openai
import ffmpeg
import pytubefix
import sys
import os

# Configure a chave de API do OpenAI
api_key = "sk-b-EchWWZZTXC_JdpDo1NhTzE0eL3fZT_i_i8S8dn3oT3BlbkFJtynFmyDF1T4qzrFfmOUI2frHLVgS8rv-_sj5m81usA"
openai.api_key = api_key

# Função para baixar o áudio do YouTube
def download_audio(url, output_file):
    yt = pytubefix.YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    audio_path = stream.download(filename=output_file)
    return audio_path

# Função para converter o áudio baixado para WAV
def convert_to_wav(input_file, output_file):
    ffmpeg.input(input_file).output(output_file, format='wav', loglevel="error").run()

# Função para transcrever o áudio usando o modelo Whisper da OpenAI
def transcribe_audio(audio_file):
    with open(audio_file, "rb") as file:
        transcript = openai.Audio.transcribe("whisper-1", file)["text"]
    return transcript

# Função para gerar um resumo usando o GPT-4
def generate_summary(transcript):
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um assistente que resume vídeos detalhadamente. Responda com a formatação markdown."},
            {"role": "user", "content": f"Descreva o seguinte vídeo: {transcript}"}
        ]
    )
    return completion.choices[0].message["content"]

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

    # 3. Transcrever o áudio usando Whisper
    print("Transcrevendo o áudio...")
    transcript = transcribe_audio(wav_filename)
    print("Transcrição concluída.")

    # 4. Gerar o resumo do vídeo com GPT-4
    print("Gerando o resumo...")
    summary = generate_summary(transcript)
    print("Resumo gerado com sucesso.")

    # 5. Salvar o resumo em um arquivo markdown
    with open("resumo.md", "w", encoding="utf-8") as md_file:
        md_file.write(summary)

    print("Resumo salvo no arquivo resumo.md")
