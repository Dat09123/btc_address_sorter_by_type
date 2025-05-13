# Bitcoin Address Sorter

BitMorphX is a high-performance, multiprocessing-based BTC address sorter built for extreme-scale datasets. It efficiently classifies legacy, SegWit, and Bech32 addresses from massive address dumps using CPU threading and low-memory streaming.

---

## ✨ Overview

**Bitcoin Address Sorter** is a Bitcoin address classification tool designed for extremely large datasets. The program uses multiprocessing and handles input with minimal RAM usage while displaying real-time progress. Ideal for research, analytics, and forensic investigation.

---

## 🔧 Features

- ✅ Supports 50+ million address files  
- ✅ Legacy, P2SH, and Bech32 detection  
- ✅ True multiprocessing (Process + Queue)  
- ✅ Low memory usage (streaming input)  
- ✅ Real-time `tqdm` progress bar  
- ✅ Colorized CLI output (`colorama`)  
- ✅ ASCII banner (`pyfiglet`)  

---

## 🚀 Installation

```bash
pip install -r requirements.txt
```

Dependencies:
```
colorama
tqdm
pyfiglet
```

---

## 📂 Usage

1. Place your addresses in a `.txt` file (e.g., `btc_address.txt`)  
2. Run the sorter:

```bash
python btc_address_sorter_by_type.py
```

➡️ **Windows users:** You can also run the program using the included launcher:  
```bash
start_btc_address_sorter_by_type.bat
```

3. Follow the terminal prompts:
- Enter file name or press Enter for default  
- Enter number of CPU threads (e.g., 12)

---

## 📤 Output

After processing, Bitcoin Address Sorter will create:

- `1xxxx.txt` → Legacy P2PKH addresses (start with `1`)  
- `3xxxx.txt` → P2SH (SegWit wrapped, start with `3`)  
- `bcxxxx.txt` → Native SegWit Bech32 (start with `bc1`)  

---

## 📈 Example Input

```
1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy
bc1qw508d6qe...
```

---

## ⚡ Performance Tips

- Use all available threads for maximum speed  
- Works with 8GB RAM and up, optimized for SSD  
- Designed for CLI use (headless environments, servers)  

---

## 🚫 Disclaimer

- ❌ This software is for **educational and research use only**  
- ⚠️ Do not use with private keys or real wallets  
- ❗ The author assumes no liability for misuse or data loss  

---

## 🎁 Support Development

If you value free open-source tools for blockchain research, you can donate:

### ✨ BTC  
`1MorphXyhHpgmYSfvwUpWojphfLTjrNXc7`

### ✨ XMR  
`86VAmEogaZF5WDwR3SKtEC6HSEUh6JPA1gVGcny68XmSJ1pYBbGLmdzEB1ZzGModLBXkG3WbRv12mSKv4KnD8i9w7VTg2uu`

### ✨ DASH  
`XtNuNfgaEXFKhtfxAKuDkdysxUqaZm7TDX`

### ✨ Bytecoin (BCN)  
`bcnZNMyrDrweQgoKH6zpWaE2kW1VZRsX3aDEqnxBVEQfjNnPK6vvNMNRPA4S7YxfhsStzyJeP16woK6G7cRBydZm2TvLFB2eeR`

---

Made with dedication to education, blockchain analysis, and ethical technology.  
*“I morph bits, not to break, but to understand.” — BitMorphX*