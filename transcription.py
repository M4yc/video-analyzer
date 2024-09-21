import whisper

# Função para transcrever o áudio
def transcribe_audio(audio_file):
    model = whisper.load_model("base")  # Use o modelo desejado
    result = model.transcribe(audio_file)
    return result['text']

# Função para salvar a transcrição em formato Markdown
def save_transcription_as_markdown(transcript, filename):
    with open(filename, "w", encoding="utf-8") as md_file:
        md_file.write("# Transcrição\n\n")
        md_file.write(transcript)

if __name__ == "__main__":
    audio_path = "audio.wav"  # Substitua pelo caminho do seu arquivo de áudio
    transcript = transcribe_audio(audio_path)
    print("Transcrição concluída.")

    # Salvar a transcrição em um arquivo Markdown
    markdown_filename = "transcricao.md"
    save_transcription_as_markdown(transcript, markdown_filename)
    print(f"Transcrição salva no arquivo {markdown_filename}")

