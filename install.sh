#!/bin/bash
set -e

INSTALL_DIR="$HOME/.local/share/mouse-ocr"
BIN_DIR="$HOME/.local/bin"
RUN_SCRIPT="$INSTALL_DIR/run.sh"

echo "Starting Mouse-OCR installation for Ubuntu..."

# 1. Update package lists
echo "--> Updating apt package lists..."
sudo apt update

# 2. Install system dependencies
echo "--> Installing system dependencies: scrot, tesseract-ocr, and zenity..."
sudo apt install -y \
    scrot \
    tesseract-ocr \
    libtesseract-dev \
    tesseract-ocr-chi-tra \
    tesseract-ocr-chi-sim \
    zenity

# 3. Prepare installation directory
echo "--> Creating installation directory at $INSTALL_DIR..."
mkdir -p "$INSTALL_DIR"

# 4. Copy project files to installation directory
echo "--> Copying project files..."
cp -r ./* "$INSTALL_DIR"

# 5. Install Python dependencies using uv
echo "--> Installing Python dependencies with uv..."
cd "$INSTALL_DIR"
uv sync

# 6. Make run script executable
echo "--> Making run.sh executable..."
chmod +x "$RUN_SCRIPT"

# 7. Create symlink for easy access
echo "--> Creating symlink in $BIN_DIR..."
mkdir -p "$BIN_DIR"
ln -sf "$RUN_SCRIPT" "$BIN_DIR/mouse-ocr"

echo ""
echo "✅ Installation complete!"
echo ""
echo "You can now run the tool in two ways:"
echo "1. From your terminal: mouse-ocr"
echo "2. From your i3wm keybinding (after you've set it up in your i3 config):"
echo "   bindsym \$mod+Shift+o exec --no-startup-id mouse-ocr"
echo ""
echo "Note: Ensure $BIN_DIR is in your shell's \$PATH."
