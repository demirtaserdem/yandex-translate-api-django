"""Yandex Translate Api Python Django
Erdem Demirtaş
demirtaserdem@gmail.com
https://github.com/demirtaserdem/yandex-translate-api-python-flask
https://app2.demirtas.biz
2019.01
"""
"""Bootstrap v4.2.1
ve Jinja Template Kullanularak Hazırlanmıştır. 
"""

"""''ytapi.wiews' de kullanılan fonksiyonlar
"""
import requests

def translate(input_word):
    "Ana Fonksiyon Çevirme işlemini yapar"
    #Url Oluşturulur
    url = create_url(input_word)
    #Yandex Api'ye request gönderilip kelime alınır.
    output_word = translateFunc(url)
    #Aranan Kelime
    return output_word

def create_url(input_word):
    """Yandex Api İçin Url Oluştutur Döner
    """
    #Yandex Apide Çeviri Url İsteğni oluşturmak için kısımlara ayrıldı.
    #https://tech.yandex.com/translate/doc/dg/reference/
    #translate-docpage/JSON
    #temel alınarak oluşturulmuştur.
    #Url'nin ilk değişmeeyen kısmı
    base_url ="https://translate.yandex.net/api/v1.5/tr.json/translate"
    # Api key yandex translate tarafından alınacak.
    # "https://translate.yandex.com/developers/keys"
    key = ("?key=trnsl.1.1.20190121T100542Z.4befbb4bba198843."
        +"b6081dd6370342a5c61258dbb83fb7b9a58dd523")
    #arama yapacağımız kelime - metindir. ilk url oluşturulurken 
    #"Merhaba" yazılmıştır, text = Str() oluşturulabilir.
    text = input_word
    #url'nin devamı kullanılan bir sabit
    base_text = "&text="
    #Çevirilmesi istenen dil değişkeni
    lang = "en" 
    #tr- kısmı çevrinmesi istenen dilin otomatik algılamasını kapatıp
    #türkçeden çeviri yapılmasını sağlıyor. örn. "&lang=tr-eng" ya da
    # otomatik: "&lang=eng" olarak yazılabilir.
    base_lang = "&lang=tr-"
    #oluşan temel url
    translate_url = (base_url + key+base_lang + lang + base_text
        + text)  
    return translate_url

def translateFunc(url):
    """Oluşturulan url'ye istek gönderir, alır, json objesine çevirir
    json objesinin içinden ilgili kısmı dataya yazar. Çevriyi Str 
    olarak döndürür.
    """
    data_get = requests.get(url)
    data_json = data_get.json()
    data = data_json["text"][0]
    return data
