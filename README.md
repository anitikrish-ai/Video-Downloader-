# 🎬 MiniTube Downloader

A modern YouTube downloader built with **Flask + yt-dlp + Glassmorphism UI**.  
Supports downloading videos or extracting audio in high quality with a clean, responsive interface.

---

## ✨ Features

- 🎥 Download YouTube videos
- 🎵 Extract audio (music mode)
- 🎚 Select quality (Best / 1080p / 720p / 480p)
- 💎 Modern glassmorphism UI
- 📱 Fully responsive design (mobile + desktop)
- ⚡ Fast download using `yt-dlp`
- 🌙 Dark futuristic UI theme with smooth animations

---

## 🖥️ UI Preview

A sleek glass-style downloader interface with animated background blobs and modern controls.

---

## 🚀 Tech Stack

### Frontend
- HTML5
- CSS3 (Glassmorphism UI)
- Responsive Design

### Backend
- Python 3
- Flask
- yt-dlp (YouTube downloader engine)

---

## 📁 Project Structure

```
MiniTube/
│
├── app.py               # Flask backend
├── templates/
│   └── index.html       # Main UI page
├── static/
│   └── styles.css       # Optional external CSS (if separated)
├── downloads/           # Downloaded files storage
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/minitube-downloader.git
cd minitube-downloader
```

---

### 2. Install dependencies
```bash
pip install flask yt-dlp
```

---

### 3. Run the app
```bash
python app.py
```

---

### 4. Open in browser
```
http://127.0.0.1:5000
```

---

## 📌 How It Works

1. User pastes a YouTube URL
2. Selects:
   - 🎥 Video OR 🎵 Audio
   - Quality (Best / 1080p / 720p / 480p)
3. Flask backend processes request
4. `yt-dlp` downloads media
5. File is saved in `/downloads`

---

## 🧠 Backend Logic

- Uses `yt-dlp` for extracting video/audio streams
- Dynamically builds format string based on user input
- Supports:
  - Best audio extraction
  - Merged video + audio download
  - Quality filtering (height limit)

---

## ⚠️ Important Notes

- This project is for **educational purposes only**
- YouTube terms of service may restrict downloading content
- Some videos may not be downloadable due to restrictions
- Flask backend must be run locally or on Python-supported hosting

---

## 🌐 Deployment Info

### ❌ InfinityFree Hosting Limitation
- InfinityFree does **NOT support Flask (Python backend)**
- Only HTML/CSS frontend works there

### ✅ Recommended Hosting Options
- Render.com
- Railway.app
- PythonAnywhere

---

## 💡 Suggested Project Improvements

- 📊 Download progress bar (real-time)
- 🎞 Thumbnail preview before download
- 📁 Download history panel
- 🔐 User authentication system
- ☁ Cloud storage integration
- 🎨 Dark/Light theme toggle

---

## 🧑‍💻 Author

Built with ❤️ using Flask and modern UI design principles.

---

## ⭐ Project Status

✔ Working backend  
✔ Responsive UI  
✔ Video + Audio support  
✔ Quality selector system  
🚧 Advanced features can be added next

---

## 📜 License

This project is open-source for learning purposes.
