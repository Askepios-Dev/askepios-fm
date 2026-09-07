from pathlib import Path
import shutil

ruteOrder = Path.home() / "AskepiosVault"
ruteImages = Path.home() / "AskepiosVault/Images"
ruteDocs = Path.home() / "AskepiosVault/Docs"
ruteMusic = Path.home() / "AskepiosVault/Music"

print("FILES FOUNDED:")
print("______________________________")
for i in ruteOrder.iterdir():
    if i.is_file():
        print(f"File: {i.name}")
    else:
        print(f"Directory: {i.name} ")

for j in ruteOrder.iterdir():
    if j.suffix.lower() == ".jpg" or j.suffix.lower() == ".png":
        shutil.move(j, ruteImages)
    elif j.suffix.lower() == ".pdf" or j.suffix.lower() == ".docx":
        shutil.move(j, ruteDocs)
    elif j.suffix.lower() == ".mp3":
        shutil.move(j, ruteMusic)
    else:
        pass

print("______________________________")
print("Files moved succesfully...")
