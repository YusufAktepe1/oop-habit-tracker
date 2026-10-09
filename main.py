from veritabani import veritabaniYoneticisi
from veritabani import aliskanlik_yardimcisi
from veritabani import GecersizGunHatasi    

from time import sleep as zmn


test_db=veritabaniYoneticisi.test_veritabani_olusturucu()
ay=aliskanlik_yardimcisi()
db =veritabaniYoneticisi()
def ana_menu():
    while True:
        print(db.durum_bilgisi())
        print(f"\n--- ALIŞKANLIK TAKİP SİSTEMİ (Toplam: {db.aliskanlik_sayisi}) ---")
        print("1. Yeni Alışkanlık Ekle")
        print("2. Alışkanlıkları Listele")
        print("3. Alışkanlığı Tamamla")
        print("4. Alışkanlık Sil")
        print("5. Çıkış")
        
        secim = input("Yapmak istediğiniz işlemin numarasını girin (1-5): ")

        if secim == "1":
            isim =input("lütfen alışkanlık ismini girin:")
            gun=input("lütfen gün sayısını belirtin:")

            #staticmetot ile kontrol yapalım:
            try:
                if ay.gun_kontrol(gun):
                    db.aliskanlik_ekle(isim,gun)
                    print("alışkanlık başarıyla eklendi.")
            except GecersizGunHatasi as e:
                print(f"hata yakalandı:{e}")
                    #kendi yazdığımız özel hatayı burada yakalarız
        

        elif secim == "2":
            listele =db.aliskanlik_getir()

            if not listele:
                print("kaydedilmiş alışkanlık bulunamadı.")
            else:
                for l in listele:
                    print(l)

        elif secim == "3":
            db.aliskanlik_getir()
            print("-"*25)
            guncelle_id=int(input("lütfen güncellenecek alikanlik durumunun id  numarasını girin:"))

            db.aliskanlik_guncelle(guncelle_id)
            print("alışkanlık durumu 'TAMAMLANDI' olarak güncellendi. ")

        elif secim == "4":
            db.aliskanlik_getir()
            print("-"*25)
            sil_id=int(input("silinecek alışkanlığın id numarasını girin:"))
            db.aliskanlik_sil(sil_id)
            print("alışkanlık başarıyla silindi.")

        elif secim =="5":
            print("uygulamadan başarıyla çıkış yapıldı iyi günler.")
            zmn(2)
            break

        else:
            print("hatalı seçim yaptınız")

if __name__=="__main__":
    ana_menu()
