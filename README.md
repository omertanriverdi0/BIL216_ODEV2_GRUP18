# BIL216_ODEV2_GRUP18
DTMF based character encoding and decoding system using FFT analysis in Python.
# DTMF Tabanlı Metin Kodlama ve Ses Analizi Sistemi (İSTÜN)

Bu proje, **İSTANBUL SAĞLIK VE TEKNOLOJİ ÜNİVERSİTESİ** İşaretler ve Sistemler dersi kapsamında geliştirilmiştir. Türk alfabesindeki 29 harf ve boşluk karakterini çift frekanslı tonlara (DTMF) dönüştürür ve kaydedilen ses sinyalini FFT (Fast Fourier Transform) kullanarak tekrar metne çevirir.

## 🚀 Proje Özellikleri
- **Karakter Seti:** Türk alfabesinin tamamını (ö, ç, ş, ı, ğ, ü dahil) destekler.
- **Sentezleme (Encoding):** Her karakter için benzersiz çift frekanslı sinüs dalgaları üretir.
- **Analiz (Decoding):** - **Hamming Pencereleme:** Spektral sızıntıyı önlemek için kullanılmıştır.
  - **FFT Analizi:** Frekans spektrumundan baskın tonları tespit eder.
- **Görselleştirme:** Analiz edilen her harf için modern bir spektrum grafiği sunar.

## 🛠️ Kurulum ve Çalıştırma
Projenin çalışması için sisteminizde Python yüklü olmalıdır. Gerekli kütüphaneleri yüklemek için:

```bash
pip install numpy scipy matplotlib sounddevice

## 👥 Ekip Üyeleri (Grup 18)
- **Ömer TANRIVERDİ**
- **Berfin Su EREN**
- **Fatma Gizem ŞENGÜL**
