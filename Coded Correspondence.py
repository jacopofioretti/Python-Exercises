#Scrivo un dizionario contenente l'alfabeto
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#Scrivo il messaggio da criptare
messaggio = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

#Funzione per decodificare il messaggio con offset 10g
def lettera_corretta(messaggio):
  risultato = ""
  for m in messaggio:
    if m in alfabeto:
      letter_position = (alfabeto.index(m) + 10) % 26
      risultato += alfabeto[letter_position]
    else:
      risultato += m
  return risultato
#Stampo il messaggio decodificato  
print(lettera_corretta(messaggio))

messaggio_2 = "Ciao fenomeno, hai rotto la minchia con questi messaggi"

#Funzione per codificare il messaggio con offset 10
def lettera_decodificata(messaggio_2):
  risultato_2 = ""
  for l in messaggio_2:
    if l in alfabeto:
      letter_position = (alfabeto.index(l) - 10) % 26
      risultato_2 += alfabeto[letter_position]
    else:
      risultato_2 += l
  return risultato_2
#Stampo il messaggio codificato
print(lettera_decodificata(messaggio_2))

messaggio_3 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
messaggio_4 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
#Stampo il messaggio 3 con la funzione lettera_corretta
print(lettera_corretta(messaggio_3))

#Funzione per codificare il messaggio con offset 14
def lettera_corretta_2(messaggio_4):
  risultato = ""
  for m in messaggio_4:
    if m in alfabeto:
      letter_position = (alfabeto.index(m) + 14) % 26
      risultato += alfabeto[letter_position]
    else:
      risultato += m
  return risultato
#Stampo il messaggio decodificato  
print(lettera_corretta_2(messaggio_4))

messaggio_5 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."

#Funzione per codifcare il messaggio con un offset
def lettera_corretta_3(messaggio_5, offset):
  risultato = ""
  for m in messaggio_5:
    if m in alfabeto:
      letter_position = (alfabeto.index(m) + offset) % 26
      risultato += alfabeto[letter_position]
    else:
      risultato += m
  return risultato
#Ciclo per utilizzare l'offset da 1 a 26 e stampare i risultati
for offset in range(1, 26):
    #Stampo il messaggio decodificato
  print("Offset:", offset)
  print(lettera_corretta_3(messaggio_5, offset))

#Esercizio crittografia Vigenére Cipher
messaggio_6 = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"

#Parola chiave per decriptare il messaggio
keyword = "friends"

def lettura_chiper(messaggio_6, keyword):
  contatore = 0
  for m in messaggio_6:
    if m in alfabeto:
      contatore += 1
  chiave_estesa = (keyword * 10)[:contatore]
  for k in 
