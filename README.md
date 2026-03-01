BIL216 İşaretler ve Sitemler Ödev 2 - Grup 18
Bu proje, Türk alfabesindeki harfleri DTMF mantığıyla belirli frekans çiftlerine dönüştürerek ses dosyası oluşturur ve bu ses dosyasını FFT analizi ile tekrar metne çevirir.

Proje İçeriği
Karakter Tanımlama: Alfabedeki 29 harf ve boşluk karakteri için düşük ve yüksek frekans grupları oluşturulmuştur.

Ses Üretimi: Belirlenen frekanslar sinüs formülü kullanılarak sentezlenmiş ve .wav formatında kaydedilmiştir.

Sinyal Çözme: Kaydedilen işaretler Hamming penceresinden geçirilmiş ve Hızlı Fourier Dönüşümü (FFT) ile baskın frekanslar tespit edilerek metin geri elde edilmiştir.

Kullanım
Kodu çalıştırmadan önce gerekli kütüphanelerin yüklü olduğundan emin olun:
pip install numpy scipy matplotlib sounddevice

Ana programı çalıştırmak için:
python frekans.py

Grup Üyeleri
Ömer TANRIVERDİ - 240601023

Berfin Su EREN - 240601045

Fatma Gizem ŞENGÜL - 240601016
