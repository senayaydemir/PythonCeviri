from deep_translator import GoogleTranslator

def cevir():
    metin = input("ÇEVİRMEK İSTEDİĞİNİZ METNİ GİRİN: ")
    dil = int(input("Hangi Dile Çevirmek İstiyorsunuz?\n1-Korece\n2-Özbekçe\n3-Japonca\nSeçiminiz: "))

    diller = {
        1: "korean",
        2: "uzbek",
        3: "japanese"
    }

    if dil in diller:
        ceviri = GoogleTranslator(source='turkish', target=diller[dil]).translate(metin)
        print("Çeviri:", ceviri)
    else:
        print("Geçersiz seçim yaptınız.")

cevir()
