# Mouse OCR

A simple OCR tool that allows you to select an area of the screen and get the text from it. Only on Ubuntu.

![demo.gif](demo.gif)

## Installation

Make sure you have uv installed. If not, you can install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

1. Using the install script (recommended)

```bash
git clone https://github.com/yourusername/mouse-ocr.git
cd mouse-ocr
sudo chmod +x install.sh
./install.sh
```

After installation, you can run `mouse-ocr` from the terminal or bind it to a key combination in your window manager.
And you can delete the `mouse-ocr` directory after installation. The script will install the neccessary dependencies in `$HOME/.local/bin` and `$HOME/.local/share/mouse-ocr`

In my case, binding to `Mod+Shift+o` in i3wm.

```bash
echo "bindsym \$mod+Shift+o exec --no-startup-id mouse-ocr" >> ~/.config/i3/config
```

2. Manual installation

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

## Setup key binding

### i3wm
在 `~/.config/i3/config` 中加入以下行：

```bash
bindsym $mod+Shift+o exec --no-startup-id mouse-ocr
```

Reload i3wm with `Mod+Shift+r` or restart i3wm.

## TODOs

- [x] Demo video
- [x] Use ubuntu shortcut key to activate mouse ocr (Ubuntu system api)
- [x] Installation script
- [ ] Use Python GUI tool to replace scrot (because scrot will be interrupted by some other programs)
