from pathlib import Path

rutaOrden = Path("/home/askepios/AskepiosVault")

for i in rutaOrden.iterdir():
    print(i.name)


