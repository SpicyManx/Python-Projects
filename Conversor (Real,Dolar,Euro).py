def conversor(moneda, quantitat):
  match moneda:
    case "euro,dolar":
      return f"{round(quantitat * 1.07705, 2)}$", "Euro", "Dolar", "€"
    case "dolar,euro":
      return f"{round(quantitat / 1.07705, 2)}€", "Dolar", "Euro", "$"
    case "brasilreal,dolar":
      return f"{round(quantitat / 4.95392, 2)}$", "Brasil Real", "Dolar", "R$"
    case "dolar,brasilreal":
      return f"{round(quantitat * 4.95392, 2)}R$", "Dolar", "Brasil Real", "$"
    case "brasilreal,euro":
      return f"{round(quantitat / 5.33302, 2)}€", "Brasil Real", "Euro", "R$"
    case "euro,brasilreal":
      return f"{round(quantitat * 5.33302, 2)}R$", "Euro", "Brasil Real", "€"

mf, m1, m2 = "", "", ""
print("Monedes disponibles per convertir:\n Brasil Real, Dolar, Euro")
mon = ["brasilreal","dolar","euro"]
while True:
  if(not(m1 in mon)):
    m1 = input("Quina moneda és la que estas fent servir? ").lower().replace(" ","")
    mf = m1+","
  elif(not(m2 in mon)):
    m2 = input("Quina moneda vols convertir a?: ").lower().replace(" ","")
    mf = mf+m2
  else:
    break
while True:
  q = input("Quantitat que vols convertir?: ").replace(",",".")
  if(q.isdigit()):
    q = float(q)
    break
  else:
    print("Dona-me Un número!!!!!")

LV = conversor(mf,q)
print(f"En {LV[2]}, {q}{LV[3]} serien {LV[0]}".replace(".",",")+".")