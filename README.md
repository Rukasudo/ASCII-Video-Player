🖥️ ASCII Video Player – Reproduza vídeos diretamente no terminal em arte ASCII

Este projeto é um player de vídeo em ASCII, desenvolvido em Python, que converte cada frame de um vídeo em caracteres ASCII e o exibe diretamente no terminal em tempo real.
A aplicação utiliza OpenCV para leitura do vídeo, normaliza a luminosidade dos pixels e mapeia cada valor para um conjunto de caracteres que simulam níveis de brilho.

🔧 Principais funcionalidades

🎞️ Conversão de frames para ASCII em tempo real

📏 Ajuste personalizável da largura da arte ASCII

⏱️ FPS automático baseado no vídeo original (ou definido pelo usuário)

🧹 Atualização contínua da tela para exibir a animação

🐍 Execução simples via terminal com entrada interativa

🧩 Compatível com Windows, Linux e macOS

🧠 Como funciona

O script lê o vídeo frame a frame através do OpenCV.

Cada frame é redimensionado proporcionalmente à largura escolhida pelo usuário.

A imagem é convertida para tons de cinza.

Cada pixel é associado a um caractere da paleta ASCII " .:-=+*#%@".

O terminal é limpo a cada atualização para simular movimento contínuo.

🚀 Tecnologias usadas

Python

OpenCV (cv2)

NumPy

Manipulação de terminal (cls/clear)

📌 Objetivo do projeto

Explorar manipulação de vídeo, conversão gráfica para caracteres, processamento de imagem em tempo real e técnicas de visualização alternativa no terminal.
Um experimento divertido para quem gosta de programação criativa, retro-computing e ASCII art.
