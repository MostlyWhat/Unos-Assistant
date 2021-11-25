# HOOK FILE FOR SPACY
from PyInstaller.utils.hooks import collect_all
from PyInstaller.utils.hooks import collect_data_files

# ----------------------------- SPACY -----------------------------
data = collect_all('spacy')

datas = data[0]
binaries = data[1]
hiddenimports = data[2]

datas = collect_data_files("en_core_web_sm")