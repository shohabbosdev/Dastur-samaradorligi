import time
from wikipedia import *
from streamlit import *
import json

set_lang("en")

markdown("# :rainbow[Inglizcha so'zlar ma'nosi]")
with open('dictionary.json', 'r') as file:
    data = json.load(file)

tanlov = selectbox("Tanlang...",data)

boshlash = time.time()
write(data[tanlov])
tugash = time.time()-boshlash

write(tugash*1_000)
try:
    write(summary(tanlov))
except Exception as e:
    warning(f"Xatolik: {e}")
# text_area(len(data)," ta so'z bor")