from transformers import pipeline

# Função para gerar um resumo usando o modelo BART
def generate_summary(transcript):
    summarizer = pipeline("summarization")
    summary = summarizer(transcript, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Função para ler o arquivo de transcrição
def read_transcription(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Função para salvar o resumo em um arquivo
def save_summary(summary, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(summary)

# Main
if __name__ == "__main__":
    transcription_file = "transcricao.md"
    summary_file = "resumo.md"

    # 1. Ler a transcrição do arquivo
    print("Lendo a transcrição...")
    transcript = read_transcription(transcription_file)

    # 2. Gerar o resumo
    print("Gerando o resumo...")
    summary = generate_summary(transcript)
    print("Resumo gerado com sucesso.")

    # 3. Salvar o resumo em um arquivo
    save_summary(summary, summary_file)
    print(f"Resumo salvo no arquivo {summary_file}")
