# Conversor de imagens .webp para .png

Recentemente, trabalhei em um projeto que envolveu a coleta de imagens no formato WEBP de diferentes fontes. No entanto, precisava enviar essas imagens para um servidor que só aceitava imagens no formato PNG. Como as imagens estavam espalhadas em diferentes locais, conforme eu as encontrava, as salvava em uma pasta específica para o projeto. Para converter as imagens de WEBP para PNG, utilizei uma biblioteca Python chamada Pillow. Este é um simples script Python que monitora um diretório e converte automaticamente qualquer arquivo .webp encontrado para .png.

## Como usar

1. Baixe o código do repositório para o seu computador.
2. Certifique-se de ter o Python 3.x e o módulo Pillow instalados.
3. Abra o terminal e navegue até o diretório onde o código está localizado.
4. Execute o script com o seguinte comando:

```Python
python webp_to_png_converter.py
```

5. O script agora monitorará o diretório "downloads" (ou outro diretório de sua escolha) em busca de novos arquivos .webp e os converterá automaticamente para .png.

## Configuração

Você pode configurar o diretório que o script monitora alterando o valor da variável **folder_to_watch** no código.
Por padrão, o script monitora o diretório atual.

## Dependências

Este script depende do módulo Pillow, que pode ser instalado com o seguinte comando:

```Python
pip install pillow
```
