import youtube_dl
from PyQt5.QtWidgets import QTableWidgetItem
import sys

proxy = ''
ydl_opts = {}
file_count = 0
format_code, extension, resolution, format_note, file_size = [], [], [], [], []
ydl = youtube_dl.YoutubeDL(ydl_opts)
video = {}

# 'https://www.youtube.com/watch?v=gOLlY7SV6gE'
def RetrieveInfo(w):
    global video, ydl, proxy
    proxy = w.PxyEdit.text()
    url = w.AddrEdit.text()
    if proxy is None or proxy == '':
        sys.stderr.write('[error] 请填写代理\n')
        return
    if url is None or url == '':
        sys.stderr.write('[error] 请填写资源地址\n')
        return
    ydl_opts = {'outtmpl': '%(title)s%(ext)s',
                'proxy': proxy,
                'socket_timeout': 20,
                'prefer_ffmpeg': True,
                # 'logger': MyLogger()
                }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    try:
        video = ydl.extract_info(url, download=False)
    except Exception as e:
        pass

    # sort information
    global file_count, format_code, extension, resolution, format_note, file_size
    formats = video.get('formats')
    if formats is not None:
        file_count = len(formats)
        for f in formats:
            format_code.append(f.get('format_id'))
            extension.append(f.get('ext'))
            resolution.append(ydl.format_resolution(f))
            format_note.append(f.get('format_note'))
            file_size.append(f.get('filesize'))


def FillInfo(w): 
    for i in range(0, file_count):
        w.tableWidget.setItem(i, 0, QTableWidgetItem(format_code[i]))
        w.tableWidget.setItem(i, 1, QTableWidgetItem(extension[i]))
        w.tableWidget.setItem(i, 2, QTableWidgetItem(resolution[i]))
        w.tableWidget.setItem(i, 3, QTableWidgetItem(format_note[i]))
        w.tableWidget.setItem(i, 4, QTableWidgetItem(str(file_size[i])))
