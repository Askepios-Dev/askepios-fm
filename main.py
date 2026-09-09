from pathlib import Path
import shutil

extenciones = {
    "img" : [".jpg", ".jpeg", ".png"],
    "doc" : [".pdf", ".docx", ".txt"],
    "audio" : [".mp3", ".wav", ".flac"],
    "video" : [".mp4", ".avi", ".aac", ".webm"],
    "code" : [".py", ".js", ".html", ".css"],
    "compressed" : [".zip", ".rar"],
    "exes" : [".exe"]
}

ruteOrder = Path.home() / "AskepiosVault"
ruteImages = Path.home() / "AskepiosVault/Images"
ruteDocs = Path.home() / "AskepiosVault/Docs"
ruteMusic = Path.home() / "AskepiosVault/Music"
ruteOther = Path.home() / "AskepiosVault/Other"
ruteCompressed = Path.home() / "AskepiosVault/Compressed"
ruteVideos = Path.home() / "AskepiosVault/Videos"
ruteExe = Path.home() / "AskepiosVault/Exes"

def showFiles():
    print("FILES FOUNDED:")
    print("______________________________")
    for i in ruteOrder.iterdir():
        if i.is_file():
            print(f"File: {i.name}")
        else:
            print(f"Directory: {i.name} ")

def order():
    for j in ruteOrder.iterdir():
        extencion = j.suffix.lower()
        if extencion in extenciones["img"]:
            shutil.move(j, ruteImages)
        elif extencion in extenciones["doc"]:
            shutil.move(j, ruteDocs)
        elif extencion in extenciones["audio"]:
            shutil.move(j, ruteMusic)
        elif extencion in extenciones["compressed"]:
            shutil.move(j, ruteCompressed)
        elif extencion in extenciones["video"]: 
            shutil.move(j, ruteVideos)
        elif extencion in extenciones["exes"]:
            shutil.move(j, ruteExe)
        else:
            pass

while True:
    print("1. show files\n2. order files\n3. exit")
    option = int(input("Que desea hacer: "))

    if option == 1:
        showFiles()
    elif option == 2:
        order()
        print("Files order sucesfully")
    elif option == 3:
        break
    else:
        print("Error")




