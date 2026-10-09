import os
import unittest
from veritabani import (
    aliskanlik_yardimcisi,  
    TemelVeritabani,
    veritabaniYoneticisi,
    GecersizGunHatasi
)


class AliskanlikTakipTestleri(unittest.TestCase):

    def setUp(self):
        """Her testten önce test için özel bir veritabanı dosyası oluşturur."""
        self.test_db_adi = "test_aliskanliklar.db"
        if os.path.exists(self.test_db_adi):
            os.remove(self.test_db_adi)

        self.db = veritabaniYoneticisi(self.test_db_adi)

    def tearDown(self):
        """Her test bittikten sonra bağlantıyı kapatır ve test veritabanını siler."""
        self.db._baglanti.close()
        if os.path.exists(self.test_db_adi):
            os.remove(self.test_db_adi)

    def test_1_temel_sinif_baslatma(self):
        """TemelVeritabani sınıfı doğrudan başlatılabiliyor mu?">"""
        temel = TemelVeritabani()
        self.assertIsNotNone(temel)

    def test_2_durum_bilgisi_overriding(self):
        """Method Overriding: veritabaniYoneticisi doğru metin dönmeli."""
        bilgi = self.db.durum_bilgisi()
        # Başındaki boşluğu tolere ederek (.strip()) kontrol ediyoruz
        self.assertEqual(bilgi.strip(), "Alışkanlık Takip sistemi Veritabanı (Aktif)")

    def test_3_aliskanlik_ekle_ve_getir(self):
        """Yeni alışkanlık ekleme ve nesne eşleme (Aggregation) testi."""
        self.db.aliskanlik_ekle("Python Çalış", "30")

        self.assertEqual(self.db.aliskanlik_sayisi, 1)

        liste = self.db.aliskanlik_getir()
        self.assertEqual(len(liste), 1)

        aliskanlik = liste[0]
        self.assertEqual(aliskanlik.isim, "Python Çalış")
        self.assertEqual(aliskanlik.hedef_gun, "30")
        self.assertEqual(aliskanlik.durum, "DEVAM EDİYOR")

    def test_4_dunder_str_metodu(self):
        """Magic Method (__str__) düzgün format üretiyor mu?"""
        self.db.aliskanlik_ekle("Kitap Oku", "14")
        liste = self.db.aliskanlik_getir()
        aliskanlik = liste[0]

        cikti = str(aliskanlik)
        self.assertIn("Kitap Oku", cikti)
        self.assertIn("14", cikti)
        self.assertIn("DEVAM EDİYOR", cikti)

    def test_5_aliskanlik_guncelle(self):
        """Alışkanlık durumunu 'TAMAMLANDI' yapma testi."""
        self.db.aliskanlik_ekle("Spor Yap", "10")
        liste = self.db.aliskanlik_getir()
        id_degeri = liste[0].id

        self.db.aliskanlik_guncelle(id_degeri)

        guncel_liste = self.db.aliskanlik_getir()
        self.assertEqual(guncel_liste[0].durum, "TAMAMLANDI")

    def test_6_aliskanlik_sil(self):
        """Alışkanlık silme testi."""
        self.db.aliskanlik_ekle("Geçici Alışkanlık", "5")
        self.assertEqual(self.db.aliskanlik_sayisi, 1)

        liste = self.db.aliskanlik_getir()
        id_degeri = liste[0].id

        self.db.aliskanlik_sil(id_degeri)
        self.assertEqual(self.db.aliskanlik_sayisi, 0)

def test_7_statik_metot_kontrol(self):
    """Gün kontrol statik metot ve hata fırlatma testi."""
    # Doğru değer True dönmeli
    self.assertTrue(aliskanlik_yardimcisi.gun_kontrol("15"))

    # Negatif, sıfır veya harf verildiğinde GecersizGunHatasi fırlatmalı!
    with self.assertRaises(GecersizGunHatasi):
        aliskanlik_yardimcisi.gun_kontrol("-5")

    with self.assertRaises(GecersizGunHatasi):
        aliskanlik_yardimcisi.gun_kontrol("0")

    with self.assertRaises(GecersizGunHatasi):
        aliskanlik_yardimcisi.gun_kontrol("abc")


if __name__ == "__main__":
    unittest.main()