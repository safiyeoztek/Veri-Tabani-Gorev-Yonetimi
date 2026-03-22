# Veri Tabanı Destekli Görev Yönetimi
### Bu proje, Python'un veri tabanı yeteneklerini kullanarak kullanıcı bazlı görev takibi yapan kapsamlı bir sistemdir. Verileri kalıcı ve düzenli bir şekilde saklamak için ilişkisel veri tabanı mantığını (muhtemelen sqlite3) kullanır.

## Ne Yapıyor?
* Kullanıcı Yönetimi: Yeni kullanıcılar oluşturur ve her kullanıcıyı benzersiz (unique) bir kimlikle veri tabanına kaydeder.

* İlişkisel Veri Saklama: Görevleri belirli kullanıcılarla eşleştirerek saklar (User-Task Relationship).

* Dinamik Sorgulama: Veri tabanından sadece ilgili kullanıcıya ait görevleri filtreleyerek getirir.

* Veri Bütünlüğü: Boş girdi kontrolü gibi basit doğrulama mekanizmalarıyla veri kalitesini korur.

## Hangi Konular Var?
* Database Integration: Harici bir database.py modülü üzerinden veri tabanı işlemleri (CRUD - Create, Read, Update, Delete).

* Schema Creation: Program başında otomatik tablo oluşturma (create_tables).

* Logic Separation: İş mantığı (Main UI) ile veri erişim katmanının (Database Layer) birbirinden ayrılması.

* Data Validation: .strip() ve boşluk kontrolleri ile temiz veri girişi sağlama.

## Nasıl Çalıştırılır?
* Bilgisayarınızda Python yüklü olduğundan emin olun.

* database.py dosyasının ana dizinde olduğundan emin olun.

* Terminalden uygulamayı başlatın:

```Bash
python main.py
```
* Önce bir kullanıcı oluşturun, ardından o kullanıcı için görevler ekleyip listelemeyi deneyin.
