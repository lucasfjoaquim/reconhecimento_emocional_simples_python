import cv2
from fer import FER
emotion_detector = FER(mtcnn=True)
detector = FER()

def escanear_foto(foto):
    try:
        input_image = cv2.imread(foto)
        emocoes = emotion_detector.detect_emotions(input_image)


    except Exception as e:
        texto_erro = "--Rosto-Nao-indentificado--"
        emocoes = [{'box': [0, 0, 0, 0], 'emotions': {"--Rosto-Nao-indentificado--"}}]
        print(e)
    return emocoes[0]["emotions"]


# Exemplo de uso
caminho_da_imagem = "imagens/pessoa1.jpg"
print(escanear_foto(caminho_da_imagem))