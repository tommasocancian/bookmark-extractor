# Bookmark Extractor

## 📌 Problema iniziale
Quando si esportano i preferiti da Chrome, il browser genera un file HTML contenente **tutti i bookmark**, senza possibilità di esportare una singola cartella.

Questo rende difficile condividere solo una parte dei preferiti con altre persone o organizzare i propri bookmark in modo selettivo.

---

## 💡 Soluzione sviluppata
Ho sviluppato uno script Python che permette di:

- Selezionare il file HTML esportato da Chrome  
- Inserire il nome della cartella di bookmark da estrarre  
- Analizzare la struttura HTML del file  
- Generare un nuovo file HTML contenente solo la cartella desiderata  

---

## ⚙️ Tecnologie utilizzate
- Python  
- BeautifulSoup4  
- Tkinter (per la selezione del file)

---

## 🚀 Come utilizzare il progetto

### 1. Clonare la repository
```bash
git clone https://github.com/tuonome/bookmark-extractor.git
cd bookmark-extractor
