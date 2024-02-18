from random import randint
import sqlite3, os
from pathlib import Path
def ri(min:int,max:int):
  return randint(min,max)


path=Path('./')
#Creates a table or a file to put the passwords inside
if(not(os.path.isfile("pws.db"))):
  open('pws.db', 'w')
db1 = sqlite3.connect('pws.db')
table = db1.execute('''CREATE TABLE IF NOT EXISTS pass_clau (paraules_clau TEXT PRIMARY KEY, password TEXT NOT NULL);''')

class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

islstr = 0
while True:
  if(islstr == 0):
    hstr = input('Escribe dos palabras o más como palavra llave:\n')
    tstr = hstr
    lstr = hstr.split(' ')
    if len(lstr) > 1:
      islstr = 1
    else:
      print(c.WARNING+'Dame dos o más palabras!'+c.ENDC)
  else:
    length = input('Quantos carácteres?\n')
    if(length.isdigit()):
      break
    else:
      print(c.WARNING+'Dame un número!'+c.ENDC)
      print(c.OKGREEN+'Si estas recordando una contraseña pon cualquier número'+c.ENDC)

passexists = list(db1.execute(f"SELECT EXISTS (SELECT 1 FROM pass_clau WHERE paraules_clau = '{tstr}')"))[0][0]
if(passexists == 0):
  password = ''
  hstr = hstr.replace(' ','')
  for r in range(int(length)):
    wn = ri(0, len(hstr)-1)
    password += hstr[wn]
  db1.execute(f'INSERT INTO pass_clau (paraules_clau, password) VALUES ("{tstr}", "{password}")')
  db1.commit()
  print('La contraseña generada es "'+ password+ '" si quieres recordarla pon la llave "'+ tstr+'"!')
elif(passexists == 1):
  print('Tu contraseña guardada es: '+ list(db1.execute(f'SELECT password FROM pass_clau WHERE paraules_clau = "{tstr}"'))[0][0])
