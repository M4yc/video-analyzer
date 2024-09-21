# Analisador de Vídeos do YouTube

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffffff)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Whisper](https://img.shields.io/badge/whisper-000000?style=for-the-badge&logo=whisper&logoColor=white)

![GIF_analysis](link-para-imagem-ou-video)

## 📕 Descrição

Este projeto é um analisador de vídeos do YouTube que utiliza o modelo Whisper para transcrever o áudio dos vídeos e, em seguida, gerar um resumo da transcrição. É uma ferramenta útil para quem deseja extrair informações de vídeos de forma rápida e eficiente.

## ⚙️ Funcionalidades

- **Transcrição de Áudio**: Converte o áudio dos vídeos do YouTube em texto utilizando o Whisper.
- **Geração de Resumo**: Cria um resumo conciso a partir da transcrição do vídeo.
- **Suporte a Vários Idiomas**: Funciona com vídeos em diferentes idiomas, dependendo do suporte do Whisper.

## 🛠️ Como Funciona o Script

O analisador de vídeos do YouTube opera em duas etapas principais:

1. **Transcrição**:
   - O script faz o download do vídeo do YouTube e extrai o áudio.
   - Utiliza o modelo Whisper para transcrever o áudio em texto, resultando em uma transcrição completa do vídeo.

2. **Geração de Resumo**:
   - A partir da transcrição, o script analisa o texto e gera um resumo, destacando os principais pontos abordados no vídeo.

Esse fluxo de trabalho permite que usuários extraiam informações valiosas de vídeos longos de forma rápida e prática.

## 💻 Pré-requisitos

Certifique-se de ter o Python instalado em seu ambiente de desenvolvimento. Além disso, você precisará da biblioteca `whisper` e `pytube`. Você pode instalar as bibliotecas usando os seguintes comandos:
> [!TIP]
> Instale as bibliotecas necessárias
> Abra o terminal ou o cmd e digite:
> ~~~
> pip install whisper pytube
> ~~~

## 🎮 Como Usar

- Clone o repositório para o seu ambiente local.
- Navegue até o diretório do projeto.
- Execute o script Python utilizando o seguinte comando:
~~~ 
python analisador_youtube.py <URL_do_Vídeo>
~~~
- O script fará a transcrição e gerará o resumo do vídeo especificado.

## 📫 Contribuições

Contribuições são bem-vindas! Se você quiser melhorar este analisador de vídeos, sinta-se à vontade para enviar um pull request.

## 🤝 Autor

<img loading="lazy" src="https://avatars.githubusercontent.com/u/62727540?v=4" width=115 style="border-radius: 50%;">

- Maycon Vinicius B. Araújo - ``M4ycosoft``
  
<a href="https://www.linkedin.com/in/mayconaraujo-tech/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
<a href="https://instagram.com/mayconaraujo.tech" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
<a href = "mailto:mayconvbatista84@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"></a>

## 🧾 Licença

Este projeto está licenciado sob a Licença MIT.
