import pyttsx3
import PyPDF2
from reportlab.pdfgen import canvas

def escrever(file_path, msg: str):
    try:
        c = canvas.Canvas(file_path)  
        c.drawString(100, 750, msg)  # Escreve o texto no PDF em uma posição (x, y)
        c.save()  
        print("Arquivo criado com sucesso")
    except Exception as e:
        print("Erro ao criar o PDF: " + str(e))

# Função para falar o texto com pyttsx3
def speaker(msg: str):
    speaker = pyttsx3.init()
    speaker.say(msg)
    speaker.runAndWait()

def main():
    file_path = "teste.pdf"
    text_file = "texto.txt"
    text = "fazendo o trabalho da faculdade"
    if text_file:
        text = open(text_file, "r", encoding="utf-8").read().strip()


    escrever(file_path, text)

    with open(file_path, "rb") as file_reader:
        pdf_reader = PyPDF2.PdfReader(file_reader)
        
        for page in range(len(pdf_reader.pages)):
            text = pdf_reader.pages[page].extract_text()
            if text:  
                print(f"Texto da página {page + 1}: {text}")
                speaker(text)
                return
            print("Nenhum texto encontrado na página")

if __name__ == "__main__":
    main()
