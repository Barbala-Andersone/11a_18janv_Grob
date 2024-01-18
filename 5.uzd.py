t=input("Ievadi savu vārdu: ")

try: 
    with open("lietotajs.txt", "w", encoding="utf8") as vard:
        vard.write(t)

        print("Veiksmīgi tika izveidots fails.")
except FileNotFoundError:
    print("Nav atrasts fails.")
except Exception as e:
    print(f"Failam ir error: {e}")