import os
import time
from PIL import Image
from datetime import datetime

# diretório para monitorar
folder_to_watch = os.getcwd()
# variável de sinalização para controlar se a mensagem "Aguardando arquivos..." já foi impressa ou não
waiting_for_files = False
print(f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] Aguardando arquivos...")
while True:
    if waiting_for_files:
        print(
            f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] Aguardando arquivos...")
        waiting_for_files = False
    # espera por novos arquivos .webp
    for filename in os.listdir(folder_to_watch):
        if filename.endswith(".webp"):
            # carrega a imagem .webp
            print(
                f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] Arquivo encontrado: {filename}")
            img = Image.open(os.path.join(folder_to_watch, filename))
            # salva a imagem como .png
            img.save(os.path.join(folder_to_watch,
                     os.path.splitext(filename)[0] + ".png"))
            # remove o arquivo .webp original
            os.remove(os.path.join(folder_to_watch, filename))
            print(
                f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] Arquivo convertido: {os.path.splitext(filename)[0] + '.png'}")
            waiting_for_files = True
    # espera por mais arquivos
    time.sleep(1)
