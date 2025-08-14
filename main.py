import subprocess
from pathlib import Path
from PIL import Image
import pytesseract
import pyperclip

# 設定截圖儲存路徑
screenshot_path = Path("/tmp/mouse-ocr/tmp.png")
screenshot_path.parent.mkdir(parents=True, exist_ok=True)  # 確保資料夾存在

# 移除舊的截圖檔（如果存在）
if screenshot_path.exists():
    screenshot_path.unlink()

# 使用 scrot 工具進行區域截圖
# sudo apt install scrot
subprocess.run(["scrot", "-s", str(screenshot_path)])

# OCR 辨識，需要安裝以下套件：
# sudo apt update
# sudo apt install tesseract-ocr
# sudo apt install libtesseract-dev
# sudo apt install tesseract-ocr-chi-tra  # 繁體中文
# sudo apt install tesseract-ocr-chi-sim  # 簡體中文
# 根據需要，設定 lang 參數為 'chi_tra' 或 'chi_sim'
img = Image.open(screenshot_path)
text = pytesseract.image_to_string(img, lang="chi_tra")
print(text)

# 複製到剪貼簿
pyperclip.copy(text)

