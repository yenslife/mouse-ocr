# Mouse OCR

A simple OCR tool that allows you to select an area of the screen and get the text from it. Only on Ubuntu.

## Installation

```bash
sudo apt install scrot
```

OCR 辨識，需要安裝以下套件：
```bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
```

下載 Tesseract OCR 的語言包：
```bash
sudo apt install tesseract-ocr-chi-tra  # 繁體中文
sudo apt install tesseract-ocr-chi-sim  # 簡體中文
```

根據需要，設定 lang 參數為 'chi_tra' 或 'chi_sim'

## TODOs

- [ ] Demo video
- [ ] Use ubuntu shortcut key to activate mouse ocr
- [ ] Installation script
