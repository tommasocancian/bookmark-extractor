from bs4 import BeautifulSoup
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from pathlib import Path

# Nascondi finestra Tk
Tk().withdraw()

# Scegli manualmente il file esportato da Chrome
file_path = askopenfilename(
    title="Seleziona il file bookmark HTML esportato da Chrome",
    filetypes=[("HTML files", "*.html")]
)

if not file_path:
    print("❌ Nessun file selezionato")
    exit()

folder_name = input("👉 Quale cartella bookmark vuoi estrarre? ").strip()

print("📂 Elaborazione file...")

documents_path = Path.home() / "Documents"

with open(file_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

for h3 in soup.find_all("h3"):
    if h3.text.strip() == folder_name:

        dl = h3.find_next("dl")

        output_file = documents_path / f"bookmarks_{folder_name}.html"

        with open(output_file, "w", encoding="utf-8") as out:
            out.write(f"""
            <html>
            <head><meta charset="utf-8"></head>
            <body>
            <h3>{folder_name}</h3>
            {str(dl)}
            </body>
            </html>
            """)

        print("✅ Esportato in Documents!")
        break