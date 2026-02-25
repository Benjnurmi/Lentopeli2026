import textwrap
# fix yo shit
lore =  ("Tervetuloa TXK26K1-B ohjelmisto 1 python peli-projektiin tämän pelin ovat tehneet: nimi 1,2,3,4,? "
         "Tässä pelissä pelaat humaloituneena joulupukkina hänen korkeakoulu opiskelija aikana Metropoliassa."
         "Tehtäväsi on simppeli: Matkusta ympäri suomea keräämässä kaikenlaisia merkkejä joita voit kiinitää haalareihisi."
         "Keräämäsi merkit näkyvät joulupukki hahmossasi joka näkyy nurkassa."
         "Jotta voit liikua ympäri suomea tarvitset tietysti polttoainetta, polttoaine on tietystikkin alkoholi.")

wrapper = textwrap.TextWrapper(width=100, break_long_words=False, replace_whitespace=False)

word_list = wrapper.wrap(text=lore)

def Paheelore():
    return word_list