# from app import db, Petition
#
# db.create_all()  # sukurs mūsų lentelę DB
#
# # Iš karto inicijuosime testams keletą įrašų:
# jonas = Petition('Jonas', 'Jonaitis', 'Kažkoks labai rimtas atsiliepimas.')
# antanas = Petition('Antanas', 'Antanaitis', 'Antano nuomonė labai svarbi.')
# juozas = Petition('Juozas', 'Juozaitis', 'Aš labai piktas, nes blogai.')
# bronius = Petition('Bronius', 'Bronaitis', 'Aš tai linksmas esu, man patinka.')
#
# # Pridėsime šiuos veikėjus į mūsų DB
# db.session.add_all([jonas, antanas, juozas, bronius])
# # .commit išsaugo pakeitimus
# db.session.commit()
#
# print(jonas.id)
# print(antanas.id)
# print(bronius.id)
# print(juozas.id)