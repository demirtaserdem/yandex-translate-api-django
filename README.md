# Yandex Translate API - Python - Django 

Yandex Translate Api kullanılarak,  
Türkçe - İngilizce çeviri yapan bir Django uygulamasıdır. 

- Html sayfası oluşturulurken Bootstrap v4.2.1 kullandım.

- Python 3 ve Django Kullandım.

Temel olarak Kullanıcının istediği kelimeyle, Yandex Translate Api'ye
uygun url oluşturulmuş. Çevirisi "request" modülü kullanarak, 
Yandex Translate Api'ye get request gönderilmiştir.
Dönen bilgi json verisi verisi olarak işlenmiş Djangola birlikle jinja
kullanılarak, html sayfası render edilmiştir.

Sunucu Trafında PostgreSQL, geliştirici tarafında sqlite veritabanı kullanılmıştır.
Son arananlar; veri tabanına Model olarak kaydedilip okunarak html sayfası içerisine 
gönderilmiştir. 

Tek sayfa uygulaması oldupu için Post/Redirect/Get Kullanılmıştır.

 
## Uygulamadan fotoğraf

![Imgur](https://i.imgur.com/2OvaDYg.png?1)

### Gereklilikler

```
Python 3
```

### Yükleme

Githubdan Verileri kopyalamak için
terminalde
```
git clone https://github.com/demirtaserdem/yandex-translate-api-django.git
```

virtualenv indirme
```
pip3 install virtualenv
```
Virtlenv oluşturma
```
virtualenv venv
```
Development ayarları 

- Windows için oluşan "venv\Scripts\activate.bat" dosyası sonuna eklenencek.

```diff
+ set "DJANGO_SETTINGS_MODULE=ytadj.settings.development"
```
Vindows için virtalenv atkif etme
```
venv\Scripts\activate
```
- Linux İçin oluşan "venv/bin/activate" dosyası sonuna eklenecek
```diff
+ DJANGO_SETTINGS_MODULE="ytadj.settings.development"
+ export DJANGO_SETTINGS_MODULE
```
Linux için virtalenv atkif etme
```
source venv/bin/activate
```

Eklentileri Yüklemek için:(venv aktif olmalı)

```
pip install -r requirements.txt

```

Lokalde çalıştırmak için (venv aktif olmalı)
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Sunucuda çalıştırmak için (venv aktiv olmalı)[1]
```
python manage.py collectstatic
pip install gunicorn psycopg2-binary
```

## Test İçin 
<a href="https://app2.erdemdemirtas.net" target="_blank">Çalışan Uygulama İçin Tıklayın</a>

Uygulamayı [1]'deki dökümantasyona uyarak
yyukarıdaki adreste yayınladım.

### Yayın ortamı:
Amazon Ec2 - PostgreSQL - Amazon Route 53 - Amazon Route 53 - Ubuntu 18.04 - nginx - 
gunicorn -  letsencrypt kullanılarak hazırlanmıştır.

## Kaynak
[1] : https://github.com/barissaslan/django-projesini-yayina-alma
[2] : https://tech.yandex.com/translate/