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

#funzione per decifrare messaggio criptato con il Vigenère Ciphere
def decifra_vigenere(messaggio, keyword):
    risultato = ""
    indice_chiave = 0
    #trasformo le lettere in minuscolo
    keyword = keyword.lower()
  #scorre ogni carattere del messaggio
    for char in messaggio:
        #controlla se il carattere è una lettera (ignora spazi e punteggiatura)
        if char.isalpha():
            #converte la lettera in minuscolo per lavorare sempre con l'alfabeto in minuscolo
            minuscola = char.lower()
            #prende la lettera giusta dalla parola chiave, ripetendola se serve (grazie al modulo %)
            lettera_chiave = keyword[indice_chiave % len(keyword)]
            #creo una variabile dove trova la lettera "minuscola all'interno dell'alfabeto"
            pos_messaggio = alfabeto.index(minuscola)
            #creo una variabile dove trova la lettera chiave all'interno dell'alfabeto
            pos_chiave = alfabeto.index(lettera_chiave)
            #calcola la posizione della lettera cofirata (per codificare)
            nuova_pos = (pos_messaggio + pos_chiave) % 26
            #prende la lettera cifrata dall'alfabeto
            nuova_lettera = alfabeto[nuova_pos]
            #se la lettera originale era maiuscola, la trasforma in maiuscolo anche nel risultato
            if char.isupper():
                nuova_lettera = nuova_lettera.upper()
            #aggiunge la lettera cifrata al risultato
            risultato += nuova_lettera
            #passa alla lettera successiva della chiave
            indice_chiave += 1
        else:
            #se il carattere non è una lettera, lo aggiunge così com'è
            risultato += char
    return risultato

print(decifra_vigenere(messaggio_6, keyword))

#messaggio da cifrare con sistema cifratura Vigenere
messaggio_7 = "Forza Juventus"
#keyword per cifrare/decifrare il messaggio
keyword_2 = "Dybala"

def cifrato_vigenere(messaggio_7, keyword_2):
    risultato = ""
    indice_chiave = 0
    #trasformo le lettere in minuscolo
    keyword_2 = keyword_2.lower()
  #scorre ogni carattere del messaggio
    for m in messaggio_7:
        #controlla se il carattere è una lettera (ignora spazi e punteggiatura)
        if m.isalpha():
            #converte la lettera in minuscolo per lavorare sempre con l'alfabeto in minuscolo
            minuscola = m.lower()
            #prende la lettera giusta dalla parola chiave, ripetendola se serve (grazie al modulo %)
            lettera_chiave = keyword_2[indice_chiave % len(keyword_2)]
            #creo una variabile dove trova la lettera "minuscola all'interno dell'alfabeto"
            pos_messaggio = alfabeto.index(minuscola)
            #creo una variabile dove trova la lettera chiave all'interno dell'alfabeto
            pos_chiave = alfabeto.index(lettera_chiave)
            #calcola la posizione della lettera cofirata (per codificare)
            nuova_pos = (pos_messaggio - pos_chiave) % 26
            #prende la lettera cifrata dall'alfabeto
            nuova_lettera = alfabeto[nuova_pos]
            #se la lettera originale era maiuscola, la trasforma in maiuscolo anche nel risultato
            if m.isupper():
                nuova_lettera = nuova_lettera.upper()
            #aggiunge la lettera cifrata al risultato
            risultato += nuova_lettera
            #passa alla lettera successiva della chiave
            indice_chiave += 1
        else:
            #se il carattere non è una lettera, lo aggiunge così com'è
            risultato += m
    return risultato
print(cifrato_vigenere(messaggio_7, keyword_2))
