import json
import csv

file=input("Ievadiet faila nosaukumu: ")
paplasinajums=input("Ievadiet faila paplašinājumu (piemēram '.json'): ")

try:  
    if paplasinajums==".json":
        with open(file, "r", encoding="utf8") as jfile:
            dati=json.load(file)
        
            print(dati)
    elif paplasinajums==".csv":
        with open(file, "r", encoding="utf8") as cfile:
            dati=cfile.read()
            print(dati)
    else:
        with open(file, "r", encoding="utf8") as i:
            dati=i.read()
            print(dati)
except FileNotFoundError:
    print("Fails nav atrasts.")
except json.JSONDecodeError:
    print("Nav pareizs JSON formāts failam.")
except Exception as e:
    print(f"Failam ir error: {e}")