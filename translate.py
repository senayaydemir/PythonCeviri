import translate

def cevir():
    metin =str(input("ÇEVİRMEK İSTEDİĞİNİZ METNİ GİRİN:"))
    dil=int(input("Hangi Dile Çevirmek İstiyorsunuz?\n1-Korece\n2-Özbekçe\n3-Japonca"))

    if dil ==1:
        translator=translate.Translator(from_lang="tr",to_lang="ko")
        translation=translator.translate(metin)
        print(translation)

    elif dil==2:
        translator=translate.Translator(from_lang="tr",to_lang="uz")
        translation=translator.translate(metin)
        print(translation)

    elif dil==3:
        translator=translate.Translator(from_lang="tr",to_lang="ja")
        translation=translator.translate(metin)
        print(translation)
cevir()