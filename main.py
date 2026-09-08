from pathlib import Path
import shutil

img = {".jpg", ".jpeg", ".png"}
doc = {".pdf", ".docx", ".txt"}
audio = {".mp3", ".wav", ".flac"}
video = {".mp4", ".avi", ".aac", ".webm"}
code = {".py", ".js", ".html", ".css"}
compressed = {".zip", ".rar"}

ruteOrder = Path.home() / "AskepiosVault"
ruteImages = Path.home() / "AskepiosVault/Images"
ruteDocs = Path.home() / "AskepiosVault/Docs"
ruteMusic = Path.home() / "AskepiosVault/Music"
ruteOther = Path.home() / "AskepiosVault/Other"
ruteCompressed = Path.home() / "AskepiosVault/Compressed"
ruteVideos = Path.home() / "AskepiosVault/Videos"

print("FILES FOUNDED:")
print("______________________________")
for i in ruteOrder.iterdir():
    if i.is_file():
        print(f"File: {i.name}")
    else:
        print(f"Directory: {i.name} ")

for j in ruteOrder.iterdir():
    extencion = j.suffix.lower()
    if extencion in img:
        shutil.move(j, ruteImages)
    elif extencion in doc:
        shutil.move(j, ruteDocs)
    elif extencion in audio:
        shutil.move(j, ruteMusic)
    elif extencion in compressed:
        shutil.move(j, ruteCompressed)
    elif extencion in video: 
        shutil.move(j, ruteVideos)
    else:
        pass
        
print("______________________________")
print("Files moved succesfully...")
