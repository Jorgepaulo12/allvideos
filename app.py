import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pytube import YouTube
import instaloader
import yt_dlp as youtube_dl

app = FastAPI()

# Create downloads directory and subdirectories
DOWNLOAD_DIR = Path('downloads')
DOWNLOAD_DIR.mkdir(exist_ok=True)
(DOWNLOAD_DIR / 'instagram').mkdir(exist_ok=True)
(DOWNLOAD_DIR / 'facebook').mkdir(exist_ok=True)
(DOWNLOAD_DIR / 'x').mkdir(exist_ok=True)
(DOWNLOAD_DIR / 'tiktok').mkdir(exist_ok=True)

@app.get('/download/tiktok')
def download_tiktok(url: str):
    try:
        ydl_opts = {'outtmpl': str(DOWNLOAD_DIR / 'tiktok' / 'tiktok_video.%(ext)s')}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
        return {'message': 'Downloaded successfully', 'file': info['title']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/download/instagram')
def download_instagram(url: str):
    try:
        L = instaloader.Instaloader(dirname_pattern=str(DOWNLOAD_DIR / 'instagram'))
        post = instaloader.Post.from_shortcode(L.context, url.split('/')[-2])
        L.download_post(post, target=str(DOWNLOAD_DIR / 'instagram'))
        return {'message': 'Downloaded successfully', 'file': post.caption}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/download/facebook')
def download_facebook(url: str):
    try:
        ydl_opts = {'outtmpl': str(DOWNLOAD_DIR / 'facebook' / 'facebook_video.%(ext)s')}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
        return {'message': 'Downloaded successfully', 'file': info['title']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/download/x')
def download_x(url: str):
    try:
        ydl_opts = {'outtmpl': str(DOWNLOAD_DIR / 'x' / 'x_video.%(ext)s')}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
        return {'message': 'Downloaded successfully', 'file': info['title']}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
