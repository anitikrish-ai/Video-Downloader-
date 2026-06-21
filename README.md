# 🎬 MiniTube Downloader

<p align="center">
  <img src="https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif" width="180">
</p>

<p align="center">
  <b>A modern YouTube Video & Audio Downloader built with Flask, yt-dlp, and a futuristic Glassmorphism UI.</b>
</p>

<p align="center">
  🎥 Download Videos • 🎵 Extract Audio • 💎 Glass UI • 📱 Responsive Design • ⚡ Fast Downloads
</p>

---

## ✨ Features

* 🎥 Download YouTube videos
* 🎵 Extract audio (music mode)
* 🎚️ Multiple quality options

  * ⭐ Best
  * 📺 1080p
  * 📺 720p
  * 📺 480p
* 💎 Modern Glassmorphism Interface
* 📱 Fully Responsive (Mobile + Desktop)
* ⚡ Fast downloads powered by `yt-dlp`
* 🌙 Dark futuristic UI
* ✨ Smooth CSS animations
* 🧩 Lightweight and beginner-friendly project structure
* ☁️ Deployable on Python hosting platforms

---

## 🖼️ UI Highlights

MiniTube includes:

✨ Animated glowing blobs
✨ Glassmorphism cards
✨ Smooth transitions and hover effects
✨ Mobile-friendly layout
✨ Video and Audio mode switch
✨ Quality selector buttons
✨ Clean, modern dark theme

---

## 🚀 Tech Stack

### Frontend

* HTML5
* CSS3
* Glassmorphism Design
* Responsive Layout
* CSS Animations

### Backend

* Python 3
* Flask
* yt-dlp
* Gunicorn

---

## 📁 Project Structure

```text
Video-Downloader-/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
│
├── templates/
│   └── index.html
│
└── downloads/
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/anitikrish-ai/Video-Downloader-.git
cd Video-Downloader-
```

---

### 2️⃣ Create Virtual Environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Application

```bash
python app.py
```

---

### 5️⃣ Open Browser

```text
http://127.0.0.1:5000
```

---

## 📌 How It Works

1. Paste a YouTube URL 🔗
2. Choose:

   * 🎥 Video
   * 🎵 Audio
3. Select preferred quality:

   * ⭐ Best
   * 📺 1080p
   * 📺 720p
   * 📺 480p
4. Click Download ⬇️
5. Flask processes the request
6. `yt-dlp` downloads the media
7. File is saved inside:

```text
downloads/
```

---

## 🧠 Backend Logic

### Audio Download

```python
format = "bestaudio/best"
```

Downloads the highest quality audio available.

---

### Video Download

```python
bestvideo[height<=QUALITY]+bestaudio/best
```

Downloads:

✔️ Selected video quality
✔️ Best available audio
✔️ Automatically merges streams

---

## 📦 Dependencies

```text
Flask
yt-dlp
gunicorn
```

---

## 📄 requirements.txt

```text
flask
yt-dlp
gunicorn
```

---

## 🌐 Deployment

### Recommended Platforms

* 🚀 Render
* 🚀 Railway
* 🚀 PythonAnywhere

---

## 🚀 Deploy on Render

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

---

### Render Port Configuration

```python
import os

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
```

---

## ⚠️ InfinityFree Limitation

InfinityFree does **NOT** support:

❌ Python
❌ Flask
❌ Gunicorn
❌ yt-dlp execution

Only frontend files can run there:

✅ HTML
✅ CSS
✅ JavaScript

For the complete application, use:

* Render
* Railway
* PythonAnywhere

---

## 🔒 Security Notes

* ✅ URL input validation
* ✅ Flask POST request handling
* ✅ Downloads separated from application files
* ✅ No database required
* ✅ No user credentials stored
* ✅ Beginner-friendly and lightweight architecture

---

## 💡 Future Improvements

* 📊 Real-time download progress bar
* 🎞️ Video thumbnail preview
* 📁 Download history
* 🔐 Authentication system
* ☁️ Cloud storage integration
* 🌙 Dark / Light mode switch
* 🌍 Multi-language support
* 📱 Progressive Web App (PWA)
* 🔄 Download queue system
* 🧩 REST API endpoints
* 📈 Download analytics dashboard

---

## ⭐ Project Status

```text
✅ Flask Backend
✅ yt-dlp Integration
✅ Video Downloads
✅ Audio Downloads
✅ Quality Selection
✅ Responsive Glass UI
✅ Mobile Friendly
✅ Render Deployment Ready
🚧 More Features Planned
```

---

## 🧑‍💻 Author

**Krish**

💻 Computer Engineering Student
🎨 UI Design Enthusiast
🎌 Anime & Sketch Artist
🚀 Passionate about Development and Creative Projects

GitHub:
https://github.com/anitikrish-ai

---

## 🎌 Fun Corner

<p align="center">
  <img src="https://media.giphy.com/media/GRSnxyhJnPsaQy9YLn/giphy.gif" width="250">
</p>

> "Keep building. Every project is one step closer to mastery." ⚡

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzVja2N4OW9qN2ttOHQ2dTZ3eTVmbG80dDJtbTNhbTlmZm05bTF6MSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7TKsQ8UQ3G7Xk7Pq/giphy.gif" width="220">
</p>

---

## 📜 License

This project is licensed under the MIT License.

Please respect YouTube's Terms of Service and applicable copyright laws when downloading content.

---

<p align="center">
Made with ❤️, ☕, Python 🐍, Flask ⚗️, yt-dlp 🎬 and lots of anime energy ⚡🎌
</p>
