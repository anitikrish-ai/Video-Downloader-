from flask import Flask, render_template, request
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():
    url = request.form.get("url")
    download_type = request.form.get(
        "download_type",
        "video"
    )
    quality = request.form.get(
        "quality",
        "best"
    )

    try:
        # MUSIC
        if download_type == "audio":
            ydl_opts = {
                "format": "bestaudio/best",
                "outtmpl":
                    f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
            }

        # VIDEO
        else:
            if quality == "best":
                fmt = "bestvideo+bestaudio/best"
            else:
                fmt = (
                    f"bestvideo[height<={quality}]"
                    "+bestaudio/best"
                )

            ydl_opts = {
                "format": fmt,
                "merge_output_format": "mp4",
                "outtmpl":
                    f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s",
            }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return "✅ Download completed!"

    except Exception as e:
        return f"❌ Error: {e}"


if __name__ == "__main__":
    app.run(debug=True)

import os

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
