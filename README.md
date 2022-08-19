# Turkce-Atasozu-ve-Deyimlerin-Duygu-Analizi-mAIn-Acıkhack2022TDDİ-Türkiye Açık Kaynak Platformu
TeknoFest #Acıkhack2022TDDİ “Türkiye Açık Kaynak Platformu”

Bu çalışmanın amacı Türkçe atasözleri ve deyimlerin duygu skorlarını içeren bir veri seti oluşturmaktır.
Deyimlerin ve atasözlerinin mecaz ve ironi içerdiği bilinmektedir. Bu nedenle yapılacak bir duygu analizi ve 
herhangi bir içerik analizinde bağlam anlaşılması noktasında sorun oluşmaktadır. Çalışmada Türkçe duygu analizi
yapılması durumunda yardımcı olması beklenen toplam 1308 deyim ve atasözünü ve duygu skorlarını içeren bir veri 
seti oluşturulmuştur. Bunlardan 276 adeti etiketlenerek doğruluk değerlendirilmesi yapılmıştır.

1308 atasözü ve deyim https://www.turkedebiyati.org/turkce-deyimler-sozlugu/2/ , https://turkceodevim.com/deyimler-ve-anlamlari-kisa/ 
ve https://www.dilbilgisi.net/a-harfi-deyimler-sozlugu/ sitelerinden seçilerek toplanmıştır. Bu veri setinde deyimler veya atasözleri 
ve bunların anlamları bulunmaktadır. Ardından bu sete yeni bir sütunda deyimlerin İngilizce anlamları eklenmiştir.

"sentistrength" kütüphanesi ile deyimlerin İngilizce anlamları kullanılarak duygu skorları elde edilmiştir. Kütüphaneyi 
kullanabilmek için jar ve data dosyalarını sırasıyla http://sentistrength.wlv.ac.uk/jkpop/ ve http://sentistrength.wlv.ac.uk/download.html 
linklerinden indirip bilgisayarınızda "C:/Users/Kevser Cansu/Documents/" dosyasının altına kaydetmelisiniz. Kütüphaneyi import ettikten 
sonra metodları kullanırken absolute path'i kullanmalısınız.

AVCI, Yıldız Yenen. TÜRKİYE TÜRKÇESİ DEYİMLERİNDE DUYGULARIN ANALİZİ. Turkish Studies (Elektronik), 2015, 10.7: 997-1020. DOI:http://dx.doi.org/10.7827/TurkishStudies.8198

Yukarıda referansı verilen yazarın çalışmasından yararlanılarak oluşturduğum veri setinden 276 tanesi negatif "N" ve pozitif "P" şeklinde etiketlenmiştir. Ardından doğruluk değerini hesaplamak adına sentistrength ile elden edilen skorlar ile etiketli veriler karşılaştırılmıştır. 
Bu çalışmada "0.77" doğruluk oranı elde edilmiştir.

Not: Çalşımada esas kodlar Codes klasörü içinde; veriler Data klasörü içerisinde yer almaktadır. Repository'yi indirdikten sonra path'lerde gerekli değişiklikleri yaparak kodları çalıştırabilirsiniz. Projede kullandığım tüm veri setlerine https://drive.google.com/drive/folders/1FJ0cxELG31qBWkuCwavcSF0TNgeKZFOn?usp=sharing linkinden ulaşabilirsiniz.
