from time import *
from streamlit import *
import json

markdown("# :rainbow[Inglizcha so'zlar ma'nosi]")
with open('dictionary.json', 'r') as file:
    data = json.load(file)

boshlash = time()
tanlov = selectbox("Tanlang...",data)

write(data[tanlov])
tugash = time()-boshlash
write(tugash*1_000)
write(len(data)," ta so'z bor")