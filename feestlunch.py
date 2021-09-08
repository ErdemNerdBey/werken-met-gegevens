croissant_kosten = 0.39
croissant_aantal = 17

stokbrood_kosten = 2.78
stokbrood_aantal = 2

kortingsbon_kosten = 0.50
kortingsbon_aantal = 3

bedrag = (croissant_kosten * croissant_aantal + stokbrood_kosten * stokbrood_aantal) - kortingsbon_kosten * kortingsbon_aantal

print("De feestlunch kost je bij de bakker " + str(bedrag) + " euro voor de" + str(croissant_aantal) + "croissantjes en de " + str(stokbrood_aantal) + "stokbroden als de " + str(kortingsbon_aantal) + "kortingsbonnen nog geldig zijn!")