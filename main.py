meme_dict = {
            "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
            "LOL": "Częsta reakcja na coś zabawnego",
            }


word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Nie ma takiego slowa')
    # Co powinniśmy zrobić, jeśli słowo nie zostało znalezione