slowka={
"Temprano": "Wcześnie",
"Tarde": "Późno",
"Hoy": "Dzisiaj",
"Manana": "Jutro",
"Ayer": "Wczoraj",
"Anteayer": "przedwczoraj",
"Proximamente": "Wkrótce",
"Antes": "Przedtem",
"Anoche": "Wczoraj wieczorem",
"En esta semana":"w tym tygodniu",
"En este ano": "w tym roku",
"Aun": "Jeszcze",
"Cuando": "Kiedy, Gdy",
"Despues": "Potem",
"Entonces": "wtedy",
"jamas": "nigdy",
"Luego": "później",
"Mientras": "tymczasem",
"Ya": "już",
"La semana que viene": "w następnym tygodniu",
"el ano que viene": "w przyszłym roku",
"venir": "przybywać",
"Tanto... como...": "tyle … ile",
"Asi": "Tak, w ten sposób",
"Bien": "Dobrze",
"Mal": "źle",
"Como": "Jak",
"Casi": "Prawie",
"Despacio": "Powoli",
"Rapido": "Szybko",
"Lento": "Wolno",
"Deprisa": "Pośpiesznie",
"Mejor": "Lepiej",
"Rapido": "Szybki",
"Facil": "Łatwy",
"Siempre": "zawsze",
"Casi siempre": "prawie zawsze",
"Normalmente": "Zwyczajnie",
"A Menudo": "Często",
"A Veces": "Czasami",
"Casi nunca": "Prawie Nigdy",
"Nunca": "Nigdy",
"Ahora": "teraz",
"Ahora Misimo": "w tym momencie",
"Nunca": "nigdy",
"Tampoco": "Także"
}

czasowniki={
"abrir":"otwierać",
#Ella abre la puerta - ona otwiera drzwi
"andar":"iśćnapiechotę",
"beber":"pić",
#ella bebe agua
"buscar":"szukać",
#nosotros buscamos nueva casa
"caerse":"przewracaćsię",
"caminar":"iśćnapiechotę",
"cerrar":"zamykać",
#wy zamykacie drzwi - vosotros cierrais la puerta
"comenzar(empezar)":"zaczynać",
#el futbolista comienza el partido - piłkarz rozpoczyna mecz
"comer":"jeść",
"comprar":"kupować",
#la abuela compra un regalo
}

#print(slowka["Hola"])
#x = input("Podaj znaczenie słowa")

#for slowo, znaczenie in slowka.items():
 #   print(slowo)
 #   x = input("Podaj znaczenie słowa: ")
  #  if x == znaczenie:
   #     print("Dobrze")
   # else:
  #      print("źle")
   #     continue

for slowo, znaczenie in czasowniki.items():
    print(slowo)
    x= ""
    while znaczenie != x:
        x = input("Podaj znaczenie tego słowa: ")
        







#for p in slowka:
  #  print(p)
  #  x = input("Podaj znaczenie słowa")
  #  if x == p:
  #      print("Dobrze")
  #  else:
   #     print("źle")

#if x == (slowka["Hola"]):
 #   print("Dobrze")
#else:
#    print("źle")

