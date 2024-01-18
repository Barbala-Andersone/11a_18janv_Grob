with open("teksts.txt", "r", encoding="utf8") as file:
    teksts=file.read()
    
with open("faila_teksts.txt", "w", encoding="utf8") as tfails:
    tfails.write(teksts)
