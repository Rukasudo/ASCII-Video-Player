import cv2
import os
import time
import numpy as np

def convert_frame_to_ascii(frame, width=80):
    """
    Convert a frame to ASCII art using a character set based on brightness
    """
    ascii_chars = " .:-=+*#%@"
    
    height = int(frame.shape[0] * width / frame.shape[1] / 2) 
    if height == 0:
        height = 1
        
    resized_frame = cv2.resize(frame, (width, height))

    if len(resized_frame.shape) > 2:
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    else:
        gray_frame = resized_frame
    
    normalized = gray_frame / 255.0
    ascii_frame = ""
    
    for row in normalized:
        for pixel in row:
            index = int(pixel * (len(ascii_chars) - 1)) 
            ascii_frame += ascii_chars[index]
        ascii_frame += "\n"
    
    return ascii_frame

def play_video_in_terminal(video_path, width=80, fps=30):
    """
    Play a video in the terminal using ASCII characters
    """
    if not os.path.exists(video_path):
        print(f"Erro: Arquivo de vídeo '{video_path}' não encontrado.")
        return
    
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Erro: Não foi possível abrir o arquivo de vídeo '{video_path}'.")
        return

    video_fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = 1.0 / video_fps if video_fps > 0 else 1.0 / fps
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Reproduzindo vídeo: {video_path}")
    print(f"FPS: {video_fps:.2f} | Total de frames: {total_frames}")
    print("Pressione Ctrl+C para parar\n")
    time.sleep(2)
    
    try:
        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            ascii_art = convert_frame_to_ascii(frame, width)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Frame {frame_count}/{total_frames}")
            print(ascii_art)
            
            time.sleep(frame_delay)
            frame_count += 1
            
    except KeyboardInterrupt:
        print("\nReprodução de vídeo interrompida.")
    
    finally:
        cap.release()
        print("Player de vídeo fechado.")

if __name__ == "__main__":
    print("=== Player de Vídeo ASCII ===\n")
    
    video_path = input("Digite o caminho do arquivo de vídeo: ").strip()
    
    # Remove quotes if user copied path with quotes
    video_path = video_path.strip('"').strip("'")
    
    try:
        width = int(input("Digite a largura do terminal (padrão 80): ") or "80")
    except ValueError:
        width = 80
        print(f"Usando largura padrão: {width}")

    try:
        fps = int(input("Digite o FPS (padrão: usar FPS do vídeo): ") or "0")
    except ValueError:
        fps = 0
        print("Usando FPS original do vídeo")
    
    play_video_in_terminal(video_path, width, fps)