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

rutes = {
    "img": ruteOrder / "Images",
    "doc": ruteOrder / "Docs",
    "audio": ruteOrder / "Music",
    "compressed": ruteOrder / "Compressed",
    "video": ruteOrder / "Videos",
    "exes": ruteOrder / "Exes",
    "code": ruteOrder / "Codes",
    "other": ruteOrder / "Other"
}

def makeDirs():
    for rute in rutes.values():
       rute.mkdir(parents=True, exist_ok=True)

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
        if j.is_file():
            extencion = j.suffix.lower()
            moved = False
            
            for category, lista_ext in extenciones.items():
                if extencion in lista_ext:
                    shutil.move(str(j), str(rutes[category]))
                    moved = True
                    break

            if not moved:
                shutil.move(str(j), str(rutes["other"]))

while True:
    print("1. show files\n2. order files\n3. exit")
    try:
        option = int(input("What you wanna do: "))
    except ValueError:
        print("Please enter a number")
        continue

    if option == 1:
        showFiles()
    elif option == 2:
        makeDirs()
        order()
        print("Files order sucesfully")
    elif option == 3:
        print("Bye Askepios...")
        break
    else:
        print("Invalid option")



