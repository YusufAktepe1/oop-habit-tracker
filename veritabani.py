import sqlite3
from abc import ABC , abstractmethod #abstract  base classes modülü


# ana sınıf 
class TemelVeritabani:
    def __init__(self,db_adi="aliskanliklar.db"):
        self._baglanti=sqlite3.connect(db_adi)#protect yapmak :(_baglanti) tek alt çizgi ile sadece benim istediğim sınıflar bu özelliği miras alabilir.
        self._cursor=self._baglanti.cursor()
    #bu sınıftan türeyen herkes bbu metodu kendi içinde yazmak zorunda
    @abstractmethod
    def tablolari_olustur(self):
        pass

    def durum_bilgisi(self):
        return "genel veritabanı bağlantısı"
        


class veritabaniYoneticisi(TemelVeritabani):

    def __init__(self,db_adi="aliskanliklar.db"):
        super().__init__(db_adi)
        #super() diyerek ana sınıfın __init__ metodunu çalıştırırız.
        self.tablolari_olustur()

    #alternatif kurucu (class method)
    @classmethod
    def test_veritabani_olusturucu(cls):
        #testler için geçici,bellekte çalışan veritabanı yöneticisi üretiyor
        print("test modu aktif : bellek tabanlı veritabanı oluşturuluyor")
        #sınıfın kendisinden bir nesne üretip döndürüyoruz.
        return cls(":memory:")

    def durum_bilgisi(self):#ana sınıftaki durum bilgisini ezdik (override)
        return " Alışkanlık Takip sistemi Veritabanı (Aktif)"
    def tablolari_olustur(self):

        self._cursor.execute("""
            CREATE TABLE IF NOT EXISTS aliskanliklarim(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isim TEXT NOT NULL,
                hedef_gun TEXT,
                durum TEXT DEFAULT 'DEVAM EDİYOR'
            )

        """)
        self._baglanti.commit()

    def aliskanlik_ekle(self,isim,hedef_gun):
        self._cursor.execute("""
            INSERT INTO aliskanliklarim (isim,hedef_gun)
            VALUES (?,?)
        """,(isim,hedef_gun,))
        self._baglanti.commit()

    def aliskanlik_getir(self):
        self._cursor.execute("SELECT id,isim,hedef_gun,durum FROM aliskanliklarim")
        ham_veriler=self._cursor.fetchall()

        # her bir nesneyi alışkanlık nesnesine dönüştürelim(object mapping)
        aliskanliklar_listesi=[]
        for veri in ham_veriler:
            aliskanlik_nesnesi= Aliskanlik(veri[0], veri[1], veri[2], veri[3])
            aliskanliklar_listesi.append(aliskanlik_nesnesi)

        return aliskanliklar_listesi

    def aliskanlik_guncelle(self,aliskanlik_id):
        self._cursor.execute("""
        UPDATE aliskanliklarim
        SET durum = 'TAMAMLANDI'
        WHERE id =?

        """,(aliskanlik_id,))
        self._baglanti.commit()

    def aliskanlik_sil(self,aliskanlik_id):
        self._cursor.execute("""
            DELETE FROM aliskanliklarim
            WHERE id =?

        """,(aliskanlik_id,))

        self._baglanti.commit()

    @property
    def aliskanlik_sayisi(self):
        self._cursor.execute("SELECT COUNT (*) FROM aliskanliklarim")
        return self._cursor.fetchone()[0]


class Aliskanlik:
    def __init__(self,id,isim,hedef_gun,durum):
        self.id=id
        self.isim=isim
        self.hedef_gun=hedef_gun
        self.durum=durum

    #bu sihirli metot kullanıcı için çıktı üretir
    def __str__(self):
        return f"[{self.durum}] ID:{self.id} | Alışkanlık: {self.isim} | hedef: {self.hedef_gun} GÜN"
    #__repr__ geliştiriciler içindir __str__ yoksa anca çıktı verir genellikle(debugging) için kullanılır.
    def __repr__(self):
        return f"Aliskanliklar(id={self.id},isim={self.isim})"


class aliskanlik_yardimcisi:
    
    @staticmethod
    def gun_kontrol(gun_degeri):
    #gelen sayının pozitif mi negatiif mi olduğunu kontrol eder.
        try:
            sayi =int(gun_degeri)
            if sayi>0:
                return True
            else:
                #kendi özel hatamızı fırlattık
                raise GecersizGunHatasi("gün sayısı sıfırdan büyük olmalıdır!")
        except ValueError:
            #harf girilirse standart veya özel hata fırlatabiliriz
            raise GecersizGunHatasi("lütfen geçerli bir sayı girin (harf giremezsiniz)")

class GecersizGunHatasi(Exception):#custom exceptions kullanımı
    def __init__(
        self,mesaj="gün sayısı 0'dan büyük pozitif bir tam sayı olmalıdır!"
    ):
        self.mesaj=mesaj
        super().__init__(mesaj)
        


