import html
import subprocess

import pytesseract
from pathlib import Path
from PIL import Image

screenshot_path = Path("/tmp/mouse-ocr/tmp.png")
screenshot_path.parent.mkdir(parents=True, exist_ok=True)

if screenshot_path.exists():
    screenshot_path.unlink()

# 使用 scrot 工具進行區域截圖
# $ sudo apt install scrot
subprocess.run(["scrot", "-s", str(screenshot_path)])

# OCR 辨識，需要安裝以下套件：
# $ sudo apt install tesseract-ocr
# $ sudo apt install libtesseract-dev
# $ sudo apt install tesseract-ocr-chi-tra  # 繁體中文
# $ sudo apt install tesseract-ocr-chi-sim  # 簡體中文
# 根據需要，設定 lang 參數為 'chi_tra' 或 'chi_sim'
img = Image.open(screenshot_path)
text = pytesseract.image_to_string(img, lang="eng+chi_tra")
print(text)

text_file_path = Path("/tmp/mouse-ocr/text.txt")
text_file_path.parent.mkdir(parents=True, exist_ok=True)
with text_file_path.open("w", encoding="utf-8") as f:
    f.write(text)

# use zenity to show the text
# $ sudo apt install zenity
encoded_text = html.escape(text) # avoid special charactersthat zenity cannot handle
text_with_style = f"<span font='Monospace 20'>{encoded_text}</span>"
subprocess.run(["zenity", "--text-info", "--filename", text_file_path, "--font", "Monospace 16", "--width=800", "--height=800"])
