# 🚀 OOP Temelli Konsol Tabanlı Alışkanlık Takip Sistemi (Habit Tracker)

Bu proje, **Nesne Yönelimli Programlama (Object-Oriented Programming - OOP)** prensiplerini, katmanlı mimariyi ve modern Python test süreçlerini (Unit Testing) pratik etmek amacıyla sıfırdan geliştirilmiş, SQLite veritabanı destekli konsol tabanlı bir uygulamadır.

---

## 🎯 Projenin Amacı ve Mimari Yaklaşım

Yazılım geliştirme süreçlerinde kod tekrarını önlemek, sürdürülebilirliği artırmak ve hataları en aza indirmek için saf fonksiyonel yaklaşım yerine **Nesne Yönelimli Programlama (OOP)** ilkeleri benimsenmiştir. Proje, mantıksal katmanlar (Veritabanı/İş Mantığı ve Kullanıcı Arayüzü) arasında sıkı bir sorumluluk ayrılığı (Separation of Concerns) gözetilerek tasarlanmıştır.

---

## 🏗️ Derinlemesine OOP Mimarisi ve Prensipler

Projede uygulanan teorik kavramların koddaki karşılıkları şunlardır:

### 1. Abstraction (Soyutlama)
* **Nasıl Kullanıldı:** Python'ın dahili `abc` (Abstract Base Classes) modülü kullanılarak bir `TemelVeritabani` soyut sınıfı oluşturuldu.
* **Amacı:** Doğrudan nesnesi üretilemeyen bu ana sınıf, alt sınıflar için bir mimari sözleşmedir. `@abstractmethod` ile işaretlenen `tablolari_olustur` metodu, bu sınıftan türeyen her alt sınıfın bu metodu kendine göre yazmasını **zorunlu kılar**.

### 2. Inheritance (Kalıtım) & `super()`
* **Nasıl Kullanıldı:** `veritabaniYoneticisi` sınıfı, `TemelVeritabani` sınıfından miras alır (`super().__init__()` kullanarak).
* **Amacı:** Bağlantı açma ve imleç (`cursor`) tanımlama gibi ortak veritabanı hazırlıkları tek bir yerde toplanarak kod tekrarı (Code Duplication) engellenmiştir.

### 3. Encapsulation (Kapsülleme)
* **Nasıl Kullanıldı:** Veritabanı bağlantı nesnesi `_baglanti` ve imleç `_cursor` korumalı (protected) olarak tanımlandı.
* **Amacı:** Dışarıdan doğrudan müdahale edilmesini önleyerek veri güvenliği ve kontrollü erişim sağlandı.

### 4. Method Overriding (Metot Ezme)
* **Nasıl Kullanıldı:** Ana sınıftaki `durum_bilgisi()` metodu, alt sınıf (`veritabaniYoneticisi`) tarafından ezilerek projeye özel metin dönecek şekilde özelleştirildi.

### 5. Magic / Dunder Methods (Sihirli Metotlar)
* **Nasıl Kullanıldı:** `Aliskanlik` model sınıfı içerisinde `__str__` ve `__repr__` metotları ezildi.
* **Amacı:** Bir alışkanlık nesnesi doğrudan `print()` ile ekrana bastırıldığında ham bellek adresi yerine kullanıcı dostu şık bir metin (`🌟 [DEVAM EDİYOR] ID: 1 | Alışkanlık: Python (Hedef: 30 Gün)`) çıktısı üretmesi sağlandı.

### 6. Static & Class Methods (`@staticmethod` & `@classmethod`)
* **Nasıl Kullanıldı:** 
  - `@staticmethod` (`gun_kontrol`): Sınıf veya nesne verilerine ihtiyaç duymayan, dışarıdan gelen gün verisinin pozitif bir tam sayı olup olmadığını denetleyen mantıksal bir "bekçi" olarak yazıldı.
  - `@classmethod` (`test_veritabani_olustur`): Bellek tabanlı (`:memory:`) geçici veritabanı nesneleri üreterek alternatif bir kurucu (Alternative Constructor) görevi üstlendi.

### 7. Custom Exceptions (Özel Hatalar ve İstisna Yönetimi)
* **Nasıl Kullanıldı:** Python'ın temel `Exception` sınıfından türetilen `GecersizGunHatasi` sınıfı yazıldı.
* **Amacı:** Kullanıcı negatif sayı, sıfır veya harf girdiğinde sistemin çökmesi engellenerek `try-except` bloklarıyla anlamlı hata mesajları yakalandı.

---

## 🧪 Birim Testleri (Unit Testing)

Projenin kalitesini güvence altına almak için Python'ın yerleşik **`unittest`** kütüphanesiyle kapsamlı bir test suite (`test_veritabani.py`) geliştirilmiştir. 
* Bellek tabanlı veritabanı mimarisi (`:memory:`) sayesinde testler gerçek veritabanı dosyasına dokunmadan saniyeler içinde çalışır.
* Soyut sınıf kısıtlamaları, CRUD (Ekle, Getir, Güncelle, Sil) operasyonları, dunder metot biçimlendirmeleri ve özel hata senaryoları tam bağımsız olarak doğrulanır.

Testleri çalıştırmak için terminale şu komut yazılır:

python -m unittest test_veritabani.py

📂 Proje Dosya Yapısı

habit-tracker/
│
├── veritabani.py        # OOP sınıfları, soyut yapılar, özel hatalar ve iş mantığı
├── main.py              # Konsol arayüzü ve kullanıcı akış döngüsü
├── test_veritabani.py   # Kapsamlı birim testleri (unittest)
├── .gitignore           # Git takibinden harici dosyaları gizleme ayarı
└── README.md            # Proje dokümantasyonu


Projeyi bilgisayarınıza klonlayın veya indirin:

git clone <https://github.com/YusufAktepe1/oop-habit-tracker.git>
cd habit-tracker

Ana konsol uygulamasını çalıştırın:
python main.py