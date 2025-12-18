# 🎄 New Year Tree Widget 🎉

A festive, draggable desktop Christmas tree that wishes you a Happy New Year! Because who doesn't need a tiny animated tree sitting on their screen while they work? 🎅

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- **🌟 Glowing Star**: A golden star that twinkles on top (because every tree needs some bling)
- **🎨 Colorful Ornaments**: Random ornaments with shine effects (we went full Martha Stewart on this)
- **💡 Blinking Lights**: Christmas lights that actually blink (nostalgia included)
- **❄️ Falling Snow**: Because static trees are so last century
- **👆 Draggable**: Click and drag your tree anywhere on the screen
- **📏 Resizable**: Right-click to increase or decrease size (one size does NOT fit all)
- **🔝 Always On Top**: Your tree can photobomb your Zoom calls (toggle-able)
- **🪟 Frameless & Transparent**: Looks like magic floating on your desktop
- **🖥️ Cross-Platform**: Works on macOS, Windows, and Linux (spreading joy everywhere)

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- tkinter (usually comes with Python)

**Linux users**, you might need to install tkinter:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch
sudo pacman -S tk
```

### Run It!

```bash
git clone https://github.com/alikaan/ny-tree.git
cd ny-tree
python main.py
```

That's it! Your tree should appear at the bottom-left corner of your screen. 🎄

## 🎮 Usage

### Controls

- **Left Click + Drag**: Move your tree around (because location matters)
- **Right Click** (or **Control+Click** on macOS): Open the context menu
  - Toggle "Always on Top"
  - Increase/Decrease size
  - Close (goodbye, tree 😢)

### Tips

1. **Perfect for meetings**: Position it in the corner of your video calls
2. **Seasonal decoration**: Keep it running all December (and maybe January... and February...)
3. **Stress relief**: Watch the snow fall when your code doesn't compile
4. **Productivity boost**: 0% proven, 100% festive

## 🎨 Customization

Want to modify your tree? The code is organized in clear sections:

- **STAR**: The glowing golden star
- **TREE**: The main green polygons
- **TRUNK**: Brown base (gotta stay grounded)
- **ORNAMENTS**: Colorful balls with shine effects
- **LIGHTS**: Blinking yellow/orange/white lights
- **TEXT**: "Happy New Year" message
- **SNOW**: Falling snowflakes animation

Default scale factor is `1.0` (100% size). Change the `scale_factor` variable to start with a different size:
```python
scale_factor = 1.0  # Change this to 0.5 for tiny tree, 2.0 for giant tree
```

## 🐛 Known Issues

- **macOS**: Sometimes the transparency doesn't work perfectly with certain window managers (it's complicated)
- **The tree is TOO festive**: We're working on making it less awesome (just kidding, this is a feature)
- **Addictive**: You might find yourself staring at the snow instead of working (we warned you)

## 🤝 Contributing

Found a bug? Want to add more ornaments? PRs are welcome! Let's make this tree even more ridiculous... I mean, amazing! 🎁

## 📝 License

MIT License - Feel free to use this for your own holiday cheer spreading missions!

## 🎁 Credits

Made with ❤️ and too much hot chocolate by [@alikaan](https://github.com/alikaan)

Special thanks to:
- Santa's elves (for inspiration)
- The Python community (for tkinter)
- Coffee ☕ (for everything else)

## 🌟 Star This Repo!

If this tree brought a smile to your face, please star ⭐ this repo! It costs nothing and makes developers happy! 

---

**Happy New Year! 🎉🎊🥳**

